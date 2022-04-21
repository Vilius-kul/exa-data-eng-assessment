import json
import os

# Opening JSON file
file_list = sorted(os.listdir("data"))
file_name = "data/" + file_list[0]
f = open(file_name)

# returns JSON object as
# a dictionary
data = json.load(f)


# digging for fields
# for i in data:
#     print(i)

# print(data["resourceType"])
# print(data["type"])
# print(data["entry"])
# print(type(data["entry"]))
# print(len(data["entry"]))
# print(type(data["entry"][0]))
print(data["entry"][0].keys())  # bingo

# Closing file
f.close()
