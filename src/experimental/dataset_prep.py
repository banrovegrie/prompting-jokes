import json
import uuid

# Load the JSON data
with open('output_dataset.json', 'r') as file:
    data = json.load(file)

# Add a unique ID to every headline in item["headlines"]
for item in data:
    for headline in item["headlines"]:
        headline["unique_id"] = str(uuid.uuid4())

# Save the modified data back to the JSON file
with open('modified_dataset.json', 'w') as file:
    json.dump(data, file, indent=4)

# Provide the path to the modified JSON file
modified_file_path = 'modified_dataset.json'

new_data = {}
for item in data:
    for headline in item["headlines"]:
        unique_id = headline["unique_id"]
        new_data[unique_id] = {
            "Output": headline["Output"],
            "Human": headline["Human"],
            "Headline ID": headline["Headline ID"],
            "Prompt ID": item["prompt_id"],
            "description": item["description"]
        }

# Save the new structure to a JSON file
new_file_path = 'organized_dataset.json'
with open(new_file_path, 'w') as file:
    json.dump(new_data, file, indent=4)
    
# Random Shuffle
import random

with open('organized_dataset.json', 'r') as file:
    organized_data = json.load(file)

# Convert the dictionary to a list of items
items_list = list(organized_data.items())

# Shuffle the list randomly
random.shuffle(items_list)

# Convert the shuffled list back to a dictionary
shuffled_data = dict(items_list)

# Save the shuffled data to a new JSON file
shuffled_file_path = 'shuffled_dataset.json'
with open(shuffled_file_path, 'w') as file:
    json.dump(shuffled_data, file, indent=4)

