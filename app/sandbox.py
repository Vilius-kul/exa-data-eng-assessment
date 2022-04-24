import json
import os
from pprint import pprint

from schema import Fhir, Patient

# Opening JSON file
file_list = sorted(os.listdir("data"))
file_name = "data/" + file_list[0]
f = open(file_name)


# returns JSON object as a dictionary
data = json.load(f)

one_file = Fhir(**data)


request_urls = set()
for i in range(len(one_file.entry)):
    request_urls.add(one_file.entry[i].request.url)

print(request_urls)

f.close()
