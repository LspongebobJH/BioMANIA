from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import json
from tqdm import tqdm

def generate_res(query: str):
    client = OpenAI()
    
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        stream=True
    )
    
    response = ""
    for chunk in completion:
        _content = chunk.choices[0].delta.content 
        print(_content, end='', flush=True)
        if _content is not None:
            response += _content
    return response

if __name__ == '__main__':

    # load json file query_list.json
    with open('src/analysis/reprod_gpt4/query_dict.json', 'r') as f:
        query_dict = json.load(f)

    response_dict = {}
    for idx, query in tqdm(query_dict.items()):
        response = generate_res(query)
        response_dict[idx] = response

    with open('src/analysis/reprod_gpt4/response_dict.json', 'w') as f:
        json.dump(response_dict, f)
    