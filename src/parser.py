import json

# Read the content of the .txt file
with open("dataset.txt", "r") as file:
    lines = file.readlines()

# Ensure we have 20 lines
if len(lines) != 20:
    result = {"error": "The provided file does not contain exactly 20 lines."}
else:
    # Convert the lines to a JSON object
    json_object = json.dumps(lines, indent=4)

# Saving the JSON object to a file named 'dataset.json'
output_file_path = "dataset.json"

with open(output_file_path, "w") as json_file:
    json.dump(lines, json_file, indent=4)
