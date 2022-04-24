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

pprint(one_file.entry[0].resource.telecom)


# for i in range(len(one_file.entry)):
#     if one_file.entry[i].request.url == "Patient":
#         one_entry = one_file.entry[i].resource
#         one_patient = Patient(**one_entry)
#         pprint(one_patient.extension)


f.close()
