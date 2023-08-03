"""SQLAlchemy wrapper around a database."""
from __future__ import annotations
from pathlib import Path
from typing import Any, Iterable, List, Optional

from sqlalchemy import MetaData, create_engine, inspect, select, text, func
from sqlalchemy.engine import Engine
from sqlalchemy.exc import ProgrammingError, SQLAlchemyError
from sqlalchemy.schema import CreateTable


class SQLDatabase:
    """SQLAlchemy wrapper around a database."""
    def __init__(
        self,
        engine: Engine,
        schema: Optional[str] = None,
        metadata: Optional[MetaData] = None,
        ignore_tables: Optional[List[str]] = None,
        include_tables: Optional[List[str]] = None,
        sample_rows_in_table_info: int = 3,
        custom_table_info: Optional[dict] = None,
        only_bind_include_tables: bool = False,
    ):
        """Create engine from database URI."""
        self._engine = engine
        self._schema = schema
        if include_tables and ignore_tables:
            raise ValueError("Cannot specify both include_tables and ignore_tables")
        if only_bind_include_tables and not include_tables:
            raise ValueError("Must specify which tables to bind")

        self._inspector = inspect(self._engine)
        self._all_tables = set(self._inspector.get_table_names(schema=schema))
        self._include_tables = set(include_tables) if include_tables else set()
        if self._include_tables:
            missing_tables = self._include_tables - self._all_tables
            if missing_tables:
                raise ValueError(
                    f"include_tables {missing_tables} not found in database"
                )
        self._ignore_tables = set(ignore_tables) if ignore_tables else set()
        if self._ignore_tables:
            missing_tables = self._ignore_tables - self._all_tables
            if missing_tables:
                raise ValueError(
                    f"ignore_tables {missing_tables} not found in database"
                )

        if not isinstance(sample_rows_in_table_info, int):
            raise TypeError("sample_rows_in_table_info must be an integer")

        self._sample_rows_in_table_info = sample_rows_in_table_info

        self._custom_table_info = custom_table_info
        if self._custom_table_info:
            if not isinstance(self._custom_table_info, dict):
                raise TypeError(
                    "table_info must be a dictionary with table names as keys and the "
                    "desired table info as values"
                )
            # only keep the tables that are also present in the database
            intersection = set(self._custom_table_info).intersection(self._all_tables)
            self._custom_table_info = dict(
                (table, self._custom_table_info[table])
                for table in self._custom_table_info
                if table in intersection
            )

        self._metadata = metadata or MetaData()
        tables_to_bind = (
            self._include_tables if only_bind_include_tables else self._all_tables
        )
        self._metadata.reflect(
            bind=self._engine, schema=self._schema, only=tables_to_bind
        )



    @classmethod
    def from_uri(cls, database_uri: str, **kwargs: Any) -> SQLDatabase:
        """Construct a SQLAlchemy engine from URI."""
        return cls(create_engine(database_uri), **kwargs)

    @property
    def dialect(self) -> str:
        """Return string representation of dialect to use."""
        return self._engine.dialect.name

    def get_table_names(self) -> Iterable[str]:
        """Get names of tables available."""
        if self._include_tables:
            return self._include_tables
        return self._all_tables - self._ignore_tables

    @property
    def table_info(self) -> str:
        """Information about all tables in the database."""
        return self.get_table_info()

    def get_table_info(self, table_names: Optional[List[str]] = None) -> str:
        """Get information about specified tables.

        Follows best practices as specified in: Rajkumar et al, 2022
        (https://arxiv.org/abs/2204.00498)

        If `sample_rows_in_table_info`, the specified number of sample rows will be
        appended to each table description. This can increase performance as
        demonstrated in the paper.
        """
        all_table_names = self.get_table_names()
        if table_names is not None:
            missing_tables = set(table_names).difference(all_table_names)
            if missing_tables:
                raise ValueError(f"table_names {missing_tables} not found in database")
            all_table_names = table_names

        meta_tables = [
            tbl
            for tbl in self._metadata.sorted_tables
            if tbl.name in set(all_table_names)
               and not (self.dialect == "sqlite" and tbl.name.startswith("sqlite_"))
        ]

        tables = []
        for table in meta_tables:
            if self._custom_table_info and table.name in self._custom_table_info:
                tables.append(self._custom_table_info[table.name])
                continue

            # add create table command
            create_table = str(CreateTable(table).compile(self._engine))

            if self._sample_rows_in_table_info:
                # build the select command
                command = select(table).limit(self._sample_rows_in_table_info)

                # save the command in string format
                select_star = (
                    f"SELECT * FROM '{table.name}' LIMIT "
                    f"{self._sample_rows_in_table_info}"
                )

                # save the columns in string format
                columns_str = "\t".join([col.name for col in table.columns])

                # get the sample rows
                try:
                    with self._engine.connect() as connection:
                        try:
                            sample_rows = connection.execute(command)
                            # shorten values in the sample rows

                            sample_rows = list(
                                map(lambda ls: [str(i)[:100]
                                                for i in ls], sample_rows)
                            )
                        except TypeError as e:
                            # print("***Back to literal querying...***")
                            sample_rows = connection.exec_driver_sql(select_star)
                            # shorten values in the sample rows
                            sample_rows = list(
                                map(lambda ls: [str(i)[:100]
                                                for i in ls], sample_rows)
                            )

                    # save the sample rows in string format
                    sample_rows_str = "\n".join(
                        ["\t".join(row) for row in sample_rows])
                except ProgrammingError:
                    sample_rows_str = ""
                # in some dialects when there are no rows in the table a
                # 'ProgrammingError' is returned

                # build final info for table
                tables.append(
                    create_table
                    + select_star
                    + ";\n"
                    + columns_str
                    + "\n"
                    + sample_rows_str
                )

            else:
                tables.append(create_table)

        final_str = "\n\n".join(tables)
        return final_str

    def get_table_info_dict(self, table_names: Optional[List[str]] = None) -> dict:
        all_table_names = self.get_table_names()
        if table_names is not None:
            missing_tables = set(table_names).difference(all_table_names)
            if missing_tables:
                raise ValueError(
                    f"table_names {missing_tables} not found in database")
            all_table_names = table_names

        meta_tables = [
            tbl
            for tbl in self._metadata.sorted_tables
            if tbl.name in set(all_table_names)
               and not (self.dialect == "sqlite" and tbl.name.startswith("sqlite_"))
        ]

        tables = []

        for table in meta_tables:
            if self._custom_table_info and table.name in self._custom_table_info:
                tables.append(self._custom_table_info[table.name])
            else:
                tables.append(table)
        tables_dict = {}
        for table in tables:
            cols = []
            col_details = []
            pk = []
            fks = []
            sample_rows = self.get_tbl_samples_dict(table)
            num_rows = self.get_rows_of_a_table(table)
            for col in table.columns:
                # distinct_values = self.count_distinct_values_of_a_col(table, col)
                distinct_values = list(range(10)) # to solve the error
                # cardinality = len(distinct_values) / num_rows
                cols.append([col.name, str(col.type).split('.')[-1]])
                if col.primary_key:
                    pk.append(col.name)
                if len(col.foreign_keys) > 0:
                    for fk in list(col.foreign_keys):
                        fks.append([f'{table.name}.{col.name}', fk.target_fullname])
                # here we use 3 simple conditions to filterout the categorical values:
                # 1. cardinality < 0.3
                # 2. total len(distinct_values) < 20
                # 3. '_id' not in name or name is not equal to 'id'
                # if cardinality < 0.5 and len(distinct_values) < 20 and (
                #         '_id' not in col.name.lower() or col.name.lower() == 'id'):  # maybe a categorical value
                #     col_details.append(
                #         {'is_categorical': True, 'cardinality': cardinality, 'distinct_values': distinct_values})
                # else:
                #     col_details.append(
                #         {'is_categorical': False, 'cardinality': cardinality, 'distinct_values': distinct_values[:20]})
            tables_dict[table.name] = {
                'COL': cols,
                'COL_DETAILS': col_details,
                'PK': pk,
                'FK': fks,
                'sample_rows': sample_rows
            }
        return tables_dict

    def get_tbl_samples_dict(self, table):
        sample_rows_dict = {}
        if self._sample_rows_in_table_info:
            # build the select command
            command = select(table).limit(self._sample_rows_in_table_info)

            # save the command in string format
            select_star = (
                f"SELECT * FROM '{table.name}' LIMIT "
                f"{self._sample_rows_in_table_info}"
            )

            # save the columns
            columns = [col.name for col in table.columns]

            # get the sample rows
            try:
                with self._engine.connect() as connection:
                    try:
                        sample_rows = connection.execute(command)
                        # shorten values in the sample rows

                        sample_rows = list(
                            map(lambda ls: [str(i)[:100]
                                            for i in ls], sample_rows)
                        )
                    except TypeError as e:
                        # print("***Back to literal querying...***")
                        sample_rows = connection.exec_driver_sql(select_star)
                        # shorten values in the sample rows
                        sample_rows = list(
                            map(lambda ls: [str(i)[:100]
                                            for i in ls], sample_rows)
                        )
                sample_rows_T = list(map(list, zip(*sample_rows)))
                for col, rows in zip(columns, sample_rows_T):
                    sample_rows_dict[col] = rows
            except ProgrammingError as e:
                print(f'Warning: sampling error:{table.name},{str(e)}')
                sample_rows_dict = {}
        return sample_rows_dict

    def get_rows_of_a_table(self, table):
        command = select(func.count()).select_from(table)
        try:
            with self._engine.connect() as connection:
                num_rows = connection.execute(command)
                # print(table.name)
                return num_rows.scalar()
        except ProgrammingError:
            print('Warning: categorical error')
            return None

    def count_distinct_values_of_a_col(self, table, column, num_limit=100):
        command = select(func.count(column), column).group_by(column).order_by(func.count(column).desc()).limit(
            num_limit)
        try:
            with self._engine.connect() as connection:
                sample_rows = connection.execute(command).fetchall()
                # print(table.name, column.name)
                return [list(r) for r in sample_rows]
        except ProgrammingError:
            print('Warning: categorical error')
            return []

    def run(self, command: str, fetch: str = "all") -> str:
        """Execute a SQL command and return a string representing the results.

        If the statement returns rows, a string of the results is returned.
        If the statement returns no rows, an empty string is returned.
        """
        with self._engine.begin() as connection:
            if self._schema is not None:
                connection.exec_driver_sql(
                    f"SET search_path TO {self._schema}")
            cursor = connection.execute(text(command))
            if cursor.returns_rows:
                if fetch == "all":
                    result = cursor.fetchall()
                elif fetch == "one":
                    result = cursor.fetchone()[0]
                else:
                    raise ValueError(
                        "Fetch parameter must be either 'one' or 'all'")
                return str(result)
        return ""

    def get_table_info_no_throw(self, table_names: Optional[List[str]] = None) -> str:
        """Get information about specified tables.

        Follows best practices as specified in: Rajkumar et al, 2022
        (https://arxiv.org/abs/2204.00498)

        If `sample_rows_in_table_info`, the specified number of sample rows will be
        appended to each table description. This can increase performance as
        demonstrated in the paper.
        """
        try:
            return self.get_table_info(table_names)
        except ValueError as e:
            """Format the error message"""
            return f"Error: {e}"

    def run_no_throw(self, command: str, fetch: str = "all") -> str:
        """Execute a SQL command and return a string representing the results.

        If the statement returns rows, a string of the results is returned.
        If the statement returns no rows, an empty string is returned.

        If the statement throws an error, the error message is returned.
        """
        try:
            return self.run(command, fetch)
        except SQLAlchemyError as e:
            """Format the error message"""
            return f"Error: {e}"

    def dict2str(self, d):
        text = []
        for t, v in d.items():
            _tbl = f'{t}:'
            cols = []
            pks = ['PK:']
            fks = ['FK:']
            for col in v['COL']:
                cols.append(f'{col[0]}:{self.aliastype(col[1])}')
            for pk in v['PK']:
                pks.append(pk)
            for fk in v['FK']:
                fks.append('='.join(list(fk)))

            tbl = '\n'.join([_tbl, ', '.join(cols), ' '.join(pks), ' '.join(fks)])
            text.append(tbl)
        return '\n'.join(text)

    def aliastype(self, t):
        _t = t[:3].lower()
        if _t in ['int', 'tin', 'sma', 'med', 'big', 'uns', 'rea', 'dou', 'num', 'dec']:
            res = 'N'  # numerical value
        elif _t in ['tex', 'var', 'cha', 'nch', 'nat', 'nva', 'clo']:
            res = 'T'  # text value
        elif _t in ['boo']:
            res = 'B'
        elif _t in ['dat']:
            res = 'D'
        else:
            raise ValueError('Unsupported data type')
        return res

def aliastype(t):
    _t = t[:3].lower()
    if _t in ['int', 'tin', 'sma', 'med', 'big', 'uns', 'rea', 'dou', 'num', 'dec','flo']:
        res = 'N'  # numerical value
    elif _t in ['tex', 'var', 'cha', 'nch', 'nat', 'nva', 'clo','tim']:
        res = 'T'  # text value
    elif _t in ['boo']:
        res = 'B'
    elif _t in ['dat']:
        res = 'D'
    else:
        print(t)
        raise ValueError('Unsupported data type')
    return res

def posrtgresql_db():
    host = 'testbed.inode.igd.fraunhofer.de'
    port = 18001
    database = 'world_cup'
    username = 'inode_readonly'
    password = 'W8BYqhSemzyZ64YD'
    database_uri = f'postgresql://{username}:{password}@{host}:{str(port)}/{database}'
    db = SQLDatabase.from_uri(database_uri)
    print(db.get_table_info_no_throw())
    print(db.run('SELECT * FROM player LIMIT 5'))

def formatting(ddl, alias=False):

    schema_prompt = ""
    for k, v in ddl.items():
        # print(k)
        schema_prompt += f"[Table]: {k}" + "\n[Column names, Type]:\n"
        for l in v['COL']:
            # print(f"{l[0]}, {l[-1]}" )
            schema_prompt += f"{l[0]}, {aliastype(l[-1]) if alias else l[-1] }" + "\n"
        # print("PKs:",",". join(v['PK']))
        schema_prompt += "\n[PKs]: " + ", ".join(v['PK']) + "\n"
        if v['FK'] != []:
            fk_string = []
            for fk in v['FK']:
                fk_string.append(f"{fk[0].strip()},{fk[-1]}")
            # print("FKs:", "; ".join(fk_string))
            schema_prompt += "\n[FKs]: " + "; ".join(fk_string) + "\n"
        else:
            schema_prompt += '\n[FKs]: "" '
        # print("Rows")
        if len(v['sample_rows']) > 0:
            schema_prompt += "\n[Sample rows]:\n"
            for column,values in v['sample_rows'].items():
                # print(",".join(row))
                schema_prompt += column+":\t" + "\t".join(values) + "\n"
        schema_prompt += "\n"
    return schema_prompt

def schema_db_sqllite(url, include_tables=None, sample_number=0, alias=False):
    db = SQLDatabase.from_uri(url,sample_rows_in_table_info=sample_number)
    return formatting(db.get_table_info_dict())


def schema_db_postgres(include_tables=None, sample_number=0, alias=False):
    host = '160.85.252.185'
    port = 18001
    database = 'postgres'
    username = 'dbadmin@sdbpstatbot01'
    password = '579fc314a8f73e881a9146901971d5b9'
    schema = 'experiment'
    database_uri = f'postgresql://{username}:{password}@{host}:{str(port)}/{database}'
    db = SQLDatabase.from_uri(database_uri, schema=schema,
                              include_tables= include_tables,
                              sample_rows_in_table_info=sample_number)

    return formatting(db.get_table_info_dict())


def schema_worldcup_db_postgres(include_tables=None, sample_number=0, schema=None, alias=False):

    host = 'testbed.inode.igd.fraunhofer.de'
    port = 18001
    database = 'world_cup'
    username = 'postgres'
    password = 'vdS83DJSQz2xQ'
    schema = schema
    database_uri = f'postgresql://{username}:{password}@{host}:{str(port)}/{database}'
    db = SQLDatabase.from_uri(database_uri, schema=schema,
                              include_tables= include_tables,
                              sample_rows_in_table_info=sample_number)

    return formatting(db.get_table_info_dict())