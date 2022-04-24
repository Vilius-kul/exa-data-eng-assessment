import datetime
import json
import os

from db.tables import Patient as Table  # TODO: name better
from schema import Fhir, Patient

# Opening JSON file
file_list = sorted(os.listdir("data"))
file_name = "data/" + file_list[0]
f = open(file_name)


# returns JSON object as a dictionary
data = json.load(f)


one_file = Fhir(**data)


def add_patient(data_model):
    for i in range(len(one_file.entry)):
        if one_file.entry[i].request.url == "Patient":
            patient_info = one_file.entry[i].resource
            patient = Patient(**patient_info)
            id = patient.id
            family_name = patient.name[0].family
            given_name = patient.name[0].given[0]  # type: ignore
            dob = patient.birthDate
            gender = patient.gender

            Table.insert(
                Table(patient_uid=id),
                Table(family_name=family_name),
                Table(name_given=given_name),
                Table(dob=datetime.date(dob.year, dob.month, dob.day)),
                Table(gender=gender),
            ).run_sync()


add_patient(one_file)
