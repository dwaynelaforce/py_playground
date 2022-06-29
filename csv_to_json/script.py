"""
Environment to mess around with the CSV encryption table and come up with POC
"""

import csv
import json

with open("encryption_table.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

table = {}

for row in rows:
    method = row['#Method']
    path = row['URI Resource Path'].replace("{", "").replace("}", "")
    path_params = [x for x in row['Path Parameter'].split("|") if not x == "NA"]
    query_params = [y for y in row['Query Parameter'].split("|") if not y == "NA"]

    temp = {
        method: {
            "query_params": query_params,
            "path_params": path_params
        }
    }

    if table.get(path, None):
        table[path].update(temp)
    else:
        table.update({path: temp})

with open("encryption_table.json", mode="w+", encoding="utf-8") as file:
    file.write(json.dumps(table))
