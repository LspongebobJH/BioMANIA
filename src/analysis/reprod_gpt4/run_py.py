import json
with open('src/analysis/reprod_gpt4/extracted_code.json', 'r') as f:
    code_dict = json.load(f)

exec(code_dict['scanpy:1'])