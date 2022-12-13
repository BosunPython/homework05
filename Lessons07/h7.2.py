import json
import csv

with open("dict_json.json") as f:
    dict = json.loads(f.read())
    keys = list(dict.keys())
    keys.append("Telefon")
    values = list(dict.values())
    print(keys)
    print(values)
    with open("data.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quotechar="\n")

        writer.writerow(keys)
        writer.writerow(values)
