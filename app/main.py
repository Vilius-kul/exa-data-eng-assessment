import datetime
import json
import os

from db.tables import Patient as patient_table
from db.tables import Telecom as telecom_table
from schema import Fhir, Patient

# Opening JSON file
file_list = sorted(os.listdir("data"))
file_name = "data/" + file_list[3]
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

            patient_table.insert(
                patient_table(
                    patient_uid=id,
                    family_name=family_name,
                    name_given=given_name,
                    dob=datetime.date(dob.year, dob.month, dob.day),
                    gender=gender,
                )
            ).run_sync()


def add_telecom(data_model):
    for i in range(len(one_file.entry)):
        if one_file.entry[i].request.url == "Patient":
            patient_info = one_file.entry[i].resource
            patient = Patient(**patient_info)
            system = patient.telecom[0].system
            phone_number = patient.telecom[0].value
            use = patient.telecom[0].use
            id = patient.id
            telecom_table.insert(
                telecom_table(
                    system=system, phone_number=phone_number, use=use, patient_uid=id
                ),
            ).run_sync()


add_patient(one_file)
add_telecom(one_file)


# from piccolo.table import drop_tables

# drop_tables(patient_table)
