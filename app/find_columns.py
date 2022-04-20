import json
import os

file_list = sorted(os.listdir("data"))
# file_list.sort()

file_name = "data/" + file_list[0]
print(file_name)

with open(file_name, "r") as f:
    data = json.loads(f.read())

print(data.keys())


print(data["resourceType"])
print(data["type"])
# print(data["entry"])
