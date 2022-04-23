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


def add_patient(one_file):
    for i in range(len(one_file.entry)):
        if one_file.entry[i].request.url == "Patient":
            patient_info = one_file.entry[i].resource
            patient = Patient(**patient_info)

    id = patient.id
    family_name = patient.name[0].family
    given_name = patient.name[0].given[0]
    dob = patient.birthDate
    gender = patient.gender

    return id, family_name, given_name, dob, gender


print(add_patient(one_file))


f.close()
