import json

with open('output_dataset.json', 'r') as file:
    data = json.load(file)

headlines = ["" for i in range(20)]
outputs = [[] for i in range(20)]
for item in data:
    for headline in item["headlines"]:
        headlines[int(headline["Headline ID"]) - 1] = headline["Human"]
        outputs[int(headline["Headline ID"]) - 1].append(headline["Output"])

for i in range(20):
    print(f"Headline {i + 1}: {headlines[i]}")
    for j in range(len(outputs[i])):
        print(f"Reinterpretation {j + 1}: {outputs[i][j]}")
    print()