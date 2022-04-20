import json
import os

from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient

file_list = sorted(os.listdir("data"))

file_name = "data/" + file_list[0]
with open(file_name, "r") as f:
    data = json.load(f)


one_bundle = Bundle.parse_obj(data)
resources = []
if one_bundle.entry is not None:
    for entry in one_bundle.entry:
        resources.append(entry.resource)  # type: ignore
one_resource = []
for j in range(len(resources)):
    one_resource.append(type(resources[j]))

# print(len(one_resource))

uniq_resource = set(one_resource)
# print(len(uniq_resource))
# for i in uniq_resource:
#     print(i)

# print(type(resources[0]))

one_patient = Patient.parse_obj(resources[0])

# print(dir(one_patient))
# print(one_patient.name[0])
print(one_patient.id)
print(one_patient.name[0].family)  # type: ignore
print(one_patient.name[0].given[0])  # type: ignore
print(one_patient.birthDate)
print(one_patient.gender)
