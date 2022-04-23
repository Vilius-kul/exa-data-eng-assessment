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


for i in range(len(one_file.entry)):
    if one_file.entry[i].request.url == "Patient":
        patient = one_file.entry[i].resource

patient_model = Patient(**patient)

print(patient_model.meta)

# print(type(one_pat.entry[5].request.url))

# print(one_pat.entry[5].request.url == "MedicationRequest")


# test = json.loads(one_pat.entry[5].json())
# pp(test)


f.close()
