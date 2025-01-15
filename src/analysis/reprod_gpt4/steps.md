# steps
1. examples2json.py: extract prompts of examples and store them separately in json file query_dict.json
2. get_response.py: feed query_dict.json to gpt-4 to obtain responses stored in response_dict.json
3. get_py_from_resp.py: get python code blocks from response_dict.json

# misc
* scanpy_examples.py, ehrapy_examples.py: examples corresponding to each library
* reprod_gpt4.ipynb: testing