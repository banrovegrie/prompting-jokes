"""
Part One: This parse the dataset.
"""
import json

# Read the content of the .txt file
with open("dataset.txt", "r") as file:
    lines = file.readlines()

# Ensure we have 20 lines
if len(lines) != 20:
    result = {"error": "The provided file does not contain exactly 20 lines."}
else:
    json_data = [{"id": i+1, "text": line.strip()} for i, line in enumerate(lines)]

# Saving the JSON object to a file named 'dataset.json'
output_file_path = "dataset.json"

with open(output_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)
    
"""
Part Two: This parses the prompts.
"""
import os
import json

def txt_to_json(folder_path):
    json_data = []
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    
    for idx, txt_file in enumerate(txt_files, start=1):
        with open(os.path.join(folder_path, txt_file), 'r') as f:
            content = f.read().strip()
            json_data.append({"id": idx, "text": content})
    
    with open("combined_data.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    return "combined_data.json"

output_file = txt_to_json('prompts/')

