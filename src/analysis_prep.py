import json
with open('shuffled_dataset.json', 'r') as file:
    shuffled_data = json.load(file)
    
# Correcting the keys and creating the desired format for the text file
formatted_text = []

for idx, (unique_id, details) in enumerate(shuffled_data.items(), start=1):
    joke_entry = (
        f"{idx}. Joke ID = {unique_id}\n"
        f"Headline: {details['Human']}\n"
        f"Reinterpretation: {details['Output']}\n\n"
    )
    formatted_text.append(joke_entry)

# Save the formatted text to a .txt file
txt_file_path = 'results.txt'
with open(txt_file_path, 'w') as file:
    file.writelines(formatted_text)