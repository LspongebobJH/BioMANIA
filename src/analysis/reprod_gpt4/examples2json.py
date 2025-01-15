"""
codes are adapted from resprod_gpt4.ipynb
"""

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

import re

scanpy_query, ehrapy_query = {}, {}
# Specify the path to your Python file
for file_path in ['scanpy_examples.py', 'ehrapy_examples.py']:

    # Read the content of the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Use regular expression to extract example indices and their corresponding Prompts
    matches = re.findall(r'### Example(\d+):.*?### Prompt\s*(.*?)\s*###', text, re.DOTALL)
    
    # Print the extracted example indices and prompts
    for example_index, prompt in matches:
        if 'scanpy' in file_path:
            scanpy_query['scanpy:' + example_index] = prompt
        else:
            ehrapy_query['ehrapy:' + example_index] = prompt

# index error, example 5 has no prompt, it uses prompt of example 6
scanpy_query['scanpy:6'] = scanpy_query['scanpy:5']
scanpy_query.pop('scanpy:5')

# preprocess some strings
scanpy_query['scanpy:3'] = "Provide the python code for plotting the ranking of genes with the API only from Scanpy. Apply it to the built-in pbmc3k processed dataset."

import json
with open("query_dict.json", 'w+') as json_file:
    json.dump(scanpy_query, json_file)
    json.dump(ehrapy_query, json_file)
