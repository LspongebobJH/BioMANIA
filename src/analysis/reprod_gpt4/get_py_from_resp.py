import json
from tqdm import tqdm

# Function to extract and concatenate Python code blocks
def extract_and_concatenate_python_code(text):
    # Load the JSON file
    code_blocks = []
    lines = text.split('\n')
    inside_code_block = False
    code_block = []
    
    for line in lines:
        if line.strip().startswith("```python"):
            inside_code_block = True
            code_block = []
        elif line.strip().startswith("```") and inside_code_block:
            inside_code_block = False
            code_blocks.append('\n'.join(code_block))
        elif inside_code_block:
            code_block.append(line)
    
    # Concatenate all code blocks into a single block
    return '\n'.join(code_blocks)

if __name__ == '__main__':

    with open('/Users/jiahang/Documents/BioMANIA/src/analysis/reprod_gpt4/response_dict.json', 'r') as file:
        response_dict = json.load(file)

    # Extract and concatenate Python code blocks from each value in the dictionary
    extracted_code = {}
    for key, value in tqdm(response_dict.items()):
        extracted_code[key] = extract_and_concatenate_python_code(value)

    # store the extracted code blocks in a JSON file
    with open('/Users/jiahang/Documents/BioMANIA/src/analysis/reprod_gpt4/extracted_code.json', 'w') as file:
        json.dump(extracted_code, file)