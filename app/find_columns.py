import json
import os
import pprint

from fhir.resources.bundle import Bundle

file_list = sorted(os.listdir("data"))

# parse one file
file_name = "data/" + file_list[0]
with open(file_name, "r") as f:
    # data = json.load(f)
    data = Bundle.parse_file(file_name)


# Unique resource possibly as table names
types = set()
unique_resources = set()
for item in data.entry:
    unique_resources.add(item.resource.resource_type)  # type: ignore
print(unique_resources)
