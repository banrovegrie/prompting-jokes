import json
import random
import pickle

with open("output_dataset.json", "r") as f:
    data = json.load(f)

jokes = []
for i in data:
    for j in i["headlines"]:
        if ids:
            c = random.choice(list(ids))
            ids = set(ids).remove(c)
            jokes.append((c, j["Output"]))
with open("og_order.pkl", "wb") as f:
    pickle.dump(jokes, f)
jokes = sorted(jokes, key=lambda x: x[0])
jokes = [i[1] for i in jokes]
for joke in jokes:
    print(joke)
