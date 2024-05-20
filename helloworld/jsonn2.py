import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("js2.json", "w") as write_file:
    json.dump(data, write_file)
