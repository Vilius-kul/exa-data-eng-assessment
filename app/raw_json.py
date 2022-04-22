import json
import os
from textwrap import indent

from schema import Bundle

# Opening JSON file
file_list = sorted(os.listdir("data"))
file_name = "data/" + file_list[0]
f = open(file_name)

# returns JSON object as
# a dictionary
data = json.load(f)

test = Bundle(**data)
# print(test.entry[0].keys())
# dict_keys(['fullUrl', 'resource', 'request'])
# dict_keys(['resourceType', 'id', 'meta', 'text', 'extension', 'identifier', 'name', 'telecom', 'gender', 'birthDate', 'deceasedDateTime', 'address', 'maritalStatus', 'multipleBirthBoolean', 'communication'])
print(test.entry[0].resource.keys())
# print(type(data["entry"]))
# print(len(data["entry"]))
# print(type(data["entry"][0]))
# print(data["entry"][0].keys())  # bingo
# print(type(data["entry"][0]["fullUrl"]))  # full Url


# print(data["entry"][0]["request"]) # method Url etc
# print(data["entry"][0]["resource"].keys())


# key value pairs from data["entry"][0]["resource"]
# list_of_keys = data["entry"][0]["resource"].keys()
# my_dict = data["entry"][0]["resource"]
# for key in list_of_keys:
#     print(f"Key =  {key} --->value = {my_dict[key]}")


# all request per 1 person
# for i in range(len(data["entry"])):
#     print(data["entry"][i]["request"])


# # all url's per 1 person
# for i in range(len(data["entry"])):
#     print(data["entry"][i]["fullUrl"])


# Closing file
f.close()
