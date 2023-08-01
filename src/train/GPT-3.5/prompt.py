zero_shot_prompt = '''
   Given an input question and create only a syntactically correct Postgres query.
    Never query for all the columns from a specific table, only ask for the few relevant columns given the question.
    Pay attention to using only the column names that you can see in the schema description. 
    Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    If more than one table participates use the JOIN.

    Use the following format:
    #### For the given question, use the provided tables, columns, foreign keys, and primary keys in the [Schema]  to fixing the 
    given Postgres SQL query for any issues.
    #### Use the following instructions for fixing the SQL query:
    1) Use the database values that are explicitly mentioned in the question.
    2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
    3) Use DESC and DISTINCT when needed.
    4) Pay attention to the columns that are used for the GROUP BY statement.
    5) Pay attention to the columns that are used for the SELECT statement.
    6) Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
    7) Use GROUP BY on one column only.

    Only use the tables listed in the schema information.

    [Schema]:\n{table_info}
    [Q]: {input}
    [SQL]: 
    '''

few_shot_prompt = '''
    Given an input question and create only a syntactically correct Postgres query.
    Never query for all the columns from a specific table, only ask for the few relevant columns given the question.
    Pay attention to using only the column names that you can see in the schema description. 
    Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    If more than one table participates use the JOIN.
    Use the following format:
    #### For the given question, use the provided tables, columns, foreign keys, and primary keys in the [Schema] to fixing the given 
    Postgres SQL query for any issues.
    #### Use the following instructions for fixing the SQL query:
    1) Use the database values that are explicitly mentioned in the question.
    2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
    3) Use DESC and DISTINCT when needed.
    4) Pay attention to the columns that are used for the GROUP BY statement.
    5) Pay attention to the columns that are used for the SELECT statement.
    6) Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
    7) Use GROUP BY on one column only.

    [Schema]:\n{table_info}

    Please include the following examples for better understanding.

    [Examples]: \n{examples}
    [Q]: {input} 
    [SQL]:
    '''

