import sys
import time
import random
import json
import copy
import argparse

from langchain import OpenAI

from langchain.chains.llm import LLMChain
from langchain import PromptTemplate, FewShotPromptTemplate

from langchain.chat_models import ChatOpenAI

import tiktoken
random.seed(123)
from sqlalchemyWrapper import schema_worldcup_db_postgres
import os

import pandas as pd
import csv


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def zero_shot_template():
    # input_to_template={
    #     "input":question,
    #     "table_info":table_info,
    #     "dialect":dialect,
    #     "top_k":top_k
    # }
    prompt_1 = '''
    Given an input question and create only a syntactically correct {dialect} query.
    Never query for all the columns from a specific table, only ask for the few relevant columns given the question.
    Pay attention to using only the column names that you can see in the schema description. 
    Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    If more than one table participates use the JOIN.

    Use the following format:
    #### For the given question, use the provided tables, columns, foreign keys, and primary keys to fixing the 
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
    prompt_2 = '''
    This is a task converting text into SQL statement. We will first given the dataset schema and then ask a question in
    text. You are asked to generate SQL statement.
    [Schema]:\n {table_info}
    [Q]: {input}
    [SQL]: 
    '''
    zero_shot_prompt_template = PromptTemplate(
        input_variables=["input", "table_info", "dialect"],
        # input_variables=["input", "table_info"],
        template=prompt_1,
    )
    return zero_shot_prompt_template


def few_shot_template(few_shot_examples, few_shot_example_prompt):
    prefix = '''
    Given an input question and create only a syntactically correct {dialect} query.
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

    Please include the following exampes for better understanding.

    [Example]:
    '''

    few_shot_qdmr_prompt = FewShotPromptTemplate(
        # These are the examples we want to insert into the prompt.
        examples=few_shot_examples,
        # This is how we want to format the examples when we insert them into the prompt.
        example_prompt=few_shot_example_prompt,
        # The prefix is some text that goes before the examples in the prompt.
        # Usually, this consists of intructions.
        prefix=prefix,
        # The suffix is some text that goes after the examples in the prompt.
        # Usually, this is where the user input will go
        suffix="\n" + "[Q]: {input}\n [SQL]:",
        # The input variables are the variables that the overall prompt expects.
        input_variables=["input", "table_info", "dialect"],
        # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
        example_separator="\n\n",
    )
    return few_shot_qdmr_prompt
    zero_shot_prompt_template = PromptTemplate(
        input_variables=["input", "table_info", "dialect"],
        template=prompt,
    )
    return zero_shot_prompt_template


def get_args():
    parse = argparse.ArgumentParser()
    parse.add_argument("--api-key", type=str,
                       help="openai api key", required=False)
    parse.add_argument("--prompt-file", type=str,
                       help="path to the prompt file",
                       default='/home/ubuntu/nl2sql_openai/src/prompt_with_teamplate_schema_linking.json')
    parse.add_argument("--data-path", type=str, default="/home/ubuntu/nl2sql_openai/data/worldcup/worldcup_dev_only",
                       help="path to the spider folder")

    parse.add_argument("--selected-items", type=int, default=5,
                       help="how many item would you like to pass into openai api")

    # model parameters
    parse.add_argument("--temperature", type=float, default=0)
    parse.add_argument("--model-name", type=str, default="gpt-3.5-turbo-16k",
                       help="form openai code-davinci-002,gpt-3.5-turbo ")
    parse.add_argument("--max-tokens", type=int, default=256)

    parse.add_argument("--sample-rows", type=int, default=5)

    # outputs
    parse.add_argument("--results-file", type=str,
                       default="/home/ubuntu/nl2sql_openai/data/worldcup/worldcup_dev_only/final_/gpt-3.5-turbo")
    return parse.parse_args()


def main():
    args = get_args()
    world_cup_path = args.data_path
    project_key = "OPENAI_API_KEY"
    os.environ["OPENAI_API_KEY"] = project_key

    llm = OpenAI(temperature=args.temperature,
                 model_name=args.model_name,
                 n=1,
                 stream=False,
                 max_tokens=1500,
                 top_p=1.0,
                 frequency_penalty=0.0,
                 presence_penalty=0.0)

    ## v3, 30-shots, 1

    version = "v3"
    shot = '30_shots'
    set = 2

    results_file = f"{args.results_file}_{str(set)}set_{shot}_{version}.json"

    few_shot_examples = []
    with open(F"/home/ubuntu/nl2sql_openai/data/worldcup/worldcup_dev_only/{version}/300_exp_{version}.json") as f:
        examples = json.load(f)

    # selection=[966, 1037, 523, 107, 590, 927,413,976,304,738,262,764,439,1057,1065,652,504,337,85,940,223,710,164,757,252,1040,232,299,288,1070,363,978,532,527,432, 628, 165, 479]
    # selection = [573, 927, 263, 180, 610, 439, 1037, 652, 852, 304]+[459, 103, 822, 358, 172, 687, 1008, 643, 390, 178]+[612, 380, 409, 725, 1059, 736, 375, 922, 962, 695]

    shots = {'10_shots': [[439, 252, 966, 809, 90, 913, 107, 490, 764, 540],
                          [199, 1068, 940, 439, 265, 590, 878, 809, 920, 102],
                          [940, 757, 809, 85, 333, 633, 1071, 590, 1037, 1057],
                          [479, 940, 252, 757, 590, 278, 413, 199, 232, 658]],
             '20_shots': [
                 [439, 252, 966, 809, 90, 913, 107, 490, 764, 540, 390, 385, 334, 600, 101, 131, 848, 1025, 459, 688],
                 [199, 1068, 940, 439, 265, 590, 878, 809, 920, 102, 879, 441, 688, 390, 983, 350, 178, 600, 338, 808],
                 [940, 757, 809, 85, 333, 633, 1071, 590, 1037, 1057, 382, 687, 618, 703, 1048, 805, 579, 350, 916,
                  839],
                 [479, 940, 252, 757, 590, 278, 413, 199, 232, 658, 372, 688, 687, 627, 103, 334, 310, 879, 110, 848]],
             '30_shots': [
                 [439, 252, 966, 809, 90, 913, 107, 490, 764, 540, 390, 385, 334, 600, 101, 131, 848, 1025, 459, 688,
                  446, 736,
                  4, 366, 115, 78, 170, 386, 423, 566],
                 [199, 1068, 940, 439, 265, 590, 878, 809, 920, 102, 879, 441, 688, 390, 983, 350, 178, 600, 338, 808,
                  456, 12,
                  575, 446, 380, 189, 650, 366, 258, 704],
                 [940, 757, 809, 85, 333, 633, 1071, 590, 1037, 1057, 382, 687, 618, 703, 1048, 805, 579, 350, 916, 839,
                  575,
                  725, 359, 550, 922, 99, 189, 21, 456, 12],
                 [479, 940, 252, 757, 590, 278, 413, 199, 232, 658, 372, 688, 687, 627, 103, 334, 310, 879, 110, 848,
                  1017, 575,
                  1020, 725, 724, 190, 4, 245, 456, 826]]}

    for example in examples:
        if example['id'] in shots[shot][set]:
            few_shot_examples.append({"prompt": f"[Q]: {example['question']}\n[SQL]:{example['query']}"})

    few_prompt_template = """
        {prompt}
        """
    few_shot_example_prompt = PromptTemplate(
        input_variables=["prompt"],
        template=few_prompt_template,
    )

    print(f"-----------Reading the file: {results_file}---------")

    with open(f"{world_cup_path}/{version}/dev.json") as f, open(results_file, "r+") as output:
        d = json.load(f)
        all_results = json.load(output)
        i = 0

        for e in d[i:]:
            # for i in range(len(df)):
            #     print(df.loc[i, "Name"], df.loc[i, "Age"])
            question = e['question']
            query = e['query']
            db_id = f'exp_{version}'

            # prompt_template= zero_shot_template() #divorces_duration_of_marriage_age_classes.json
            prompt_template = few_shot_template(few_shot_examples, few_shot_example_prompt)
            llm_chain = LLMChain(llm=llm, prompt=prompt_template)
            sql = None

            ddl = schema_worldcup_db_postgres(schema=db_id, sample_number=args.sample_rows)
            # ddl = schema_worldcup_db_postgres(sample_number=args.sample_rows)
            llm_inputs = {
                "input": question,
                "dialect": "Postgres",
                # "top_k": args.sample_rows,
                "table_info": ddl,
            }

            prompts = llm_chain.prep_prompts([llm_inputs])
            prompt_strings = [p.to_string() for p in prompts[0]]
            # check the length:
            # Write function to take string input and return number of tokens
            num_tokens = num_tokens_from_string(prompt_strings[0], args.model_name)

            print(f"Starting  generation: #input-tokens {num_tokens}")
            while sql is None:
                try:
                    sql = llm_chain.run(**llm_inputs)
                    print(sql)
                except Exception as e:
                    print(str(e))
                    time.sleep(3)
                    pass

            r = {
                "i": i,
                "question": question,
                "gth": query,
                "db_id": db_id,
                "generated_query": sql.replace("\n", " ").replace("\n\n", " ").replace(" ", " ").replace("  ", " "),
                "prompt": prompt_strings,
            }

            all_results.append(r)
            i += 1

            # Sets file's current position at offset.
            output.seek(0)
            json.dump(all_results, output, indent=2)

    with open(results_file) as f:
        all_results = json.load(f)

    with open(f'{args.data_path}/final_/{str(set)}set_{shot}_{version}.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for item in all_results:
            gth = item['gth'].replace("\r", " ").replace("\r\r", " ").replace("\n", " ").replace("\n\n", " ").replace(
                " ", " ").replace("  ", " ")
            pred = item['generated_query'].replace("\n", " ").replace("\n\n", " ").replace(" ", " ").replace("  ", " ")
            writer.writerow([item["question"], gth.strip(), pred.strip()])


if __name__ == '__main__':
    main()
