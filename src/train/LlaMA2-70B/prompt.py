zero_shot_prompt= '''
Given an input question, Please create only a syntactically correct postgres SQL query.
Never query for all the columns from a specific table, only ask for the few relevant columns given the question.
Pay attention to using only the column names that you can see in the schema description.
Be careful to not query for columns that do not exist.
Also, pay attention to which column is in which table. 
If more than one table participates use the JOIN.
Use the provided tables, columns, foreign keys, and primary keys to generate the Postgres SQL query.
Use the database values that are explicitly mentioned in the question.
Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
Use DESC and DISTINCT when needed.
Pay attention to the columns that are used for the GROUP BY statement.
Pay attention to the columns that are used for the SELECT statement.
Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
Use GROUP BY on one column only.

Only use the tables listed in the schema information.

[Schema]:\n{table_info}
[Q]: {input}
[SQL]: '''

few_shot_prompt = '''Given an input question, Please create only a syntactically correct postgres SQL query.
Never query for all the columns from a specific table, only ask for the few relevant columns given the question.
Pay attention to using only the column names that you can see in the schema description.
Be careful to not query for columns that do not exist.
Also, pay attention to which column is in which table. 
If more than one table participates use the JOIN.
Use the provided tables, columns, foreign keys, and primary keys to generate the Postgres SQL query.
Use the database values that are explicitly mentioned in the question.
Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
Use DESC and DISTINCT when needed.
Pay attention to the columns that are used for the GROUP BY statement.
Pay attention to the columns that are used for the SELECT statement.
Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
Use GROUP BY on one column only.

Only use the tables listed in the schema information.

[Schema]:\n{table_info}

Please include the following examples for better understanding.

[Example]:\n{examples}
[Q]: {input}
[SQL]: '''

