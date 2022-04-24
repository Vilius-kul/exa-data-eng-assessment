import json
import os
from pprint import pp, pprint

from schema import Fhir, Patient

# Opening JSON file
file_list = sorted(os.listdir("data"))
file_name = "data/" + file_list[0]
f = open(file_name)


# returns JSON object as a dictionary
data = json.load(f)

one_file = Fhir(**data)


for entry in one_file.entry:
    if entry.resource.resourceType == "Patient":
        dead = entry.resource.deceasedDateTime
        print(
            dead.year,
            dead.month,
            dead.day,
            dead.hour,
            dead.minute,
            dead.second,
            dead.tzname(),
        )


# for i in range(len(one_file.entry)):
#     if one_file.entry[i].request.url == "Patient":
#         one_entry = one_file.entry[i].resource
#         one_patient = Patient(**one_entry)
#         pprint(one_patient.extension)


f.close()
