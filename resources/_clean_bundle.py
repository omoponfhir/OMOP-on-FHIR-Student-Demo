#!/usr/bin/env python

import sys
import json

types_to_remove=["Claim", "ExplanationOfBenefit", "CareTeam", "CarePlan", "ImagingStudy"]
types_to_remove.append("Condition")
types_to_remove.append("Observation")

resource = open(sys.argv[1], 'r')
delete_index_cache = []

json_data = json.load(resource)
print(len(json_data["entry"]))

for idx, x in enumerate(json_data["entry"]):
    if x["resource"]["resourceType"] in types_to_remove:
        delete_index_cache.insert(0, idx)

for i in delete_index_cache:
    del json_data["entry"][i]


print(len(json_data["entry"]))

with open("test.json", "w") as outfile:
    json.dump(json_data, outfile)