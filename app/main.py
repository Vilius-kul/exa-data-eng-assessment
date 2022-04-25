import datetime
import json
import os
from decimal import Decimal

from db.tables import Patient as patient_table
from db.tables import Telecom as telecom_table
from schema import Fhir

file_list = os.listdir("data")


def load_json_files_to_db(file_list):
    for j_file in range(len(file_list)):
        f = open("data/" + file_list[j_file])
        data = json.load(f)
        # pydantic model
        one_file = Fhir(**data)
        # parse obj
        add_patient(one_file)
        add_telecom(one_file)
        f.close()


def add_patient(data_model):
    for entry in data_model.entry:
        if entry.resource.resourceType == "Patient":

            patient_id = entry.resource.id
            deceased = entry.resource.deceasedDateTime
            home_address_line = entry.resource.address[0]["line"][0]
            home_address_city = entry.resource.address[0]["city"]
            home_address_state = entry.resource.address[0]["state"]
            home_address_country = entry.resource.address[0]["country"]
            home_address_longitude = entry.resource.address[0]["extension"][0][
                "extension"
            ][0]["valueDecimal"]
            home_address_latitude = entry.resource.address[0]["extension"][0][
                "extension"
            ][1]["valueDecimal"]

            birth_date = entry.resource.birthDate
            name_use = entry.resource.name[0].use
            name_given = entry.resource.name[0].given[0]
            name_family = entry.resource.name[0].family
            marital_status = entry.resource.maritalStatus["text"]
            gender = entry.resource.gender
            us_core_race = entry.resource.extension[0]["extension"][0]["valueCoding"][
                "display"
            ]
            us_core_ethnicity = entry.resource.extension[1]["extension"][0][
                "valueCoding"
            ]["display"]
            mothers_maiden_name = entry.resource.extension[2]["valueString"]
            birth_place_state = entry.resource.extension[4]["valueAddress"]["state"]
            birth_place_country = entry.resource.extension[4]["valueAddress"]["country"]
            birth_place_city = entry.resource.extension[4]["valueAddress"]["city"]
            disability_adjusted_life_years = entry.resource.extension[5]["valueDecimal"]
            quality_adjusted_life_years = entry.resource.extension[6]["valueDecimal"]
            birth_sex = entry.resource.extension[3]["valueCode"]
            multiple_birth = entry.resource.multipleBirthBoolean

            patient_table.insert(
                patient_table(
                    patient_id=patient_id,
                    deceased=deceased,
                    home_address_line=home_address_line,
                    home_address_city=home_address_city,
                    home_address_state=home_address_state,
                    home_address_country=home_address_country,
                    home_address_latitude=Decimal(home_address_latitude),
                    home_address_longitude=Decimal(home_address_longitude),
                    birth_date=datetime.date(
                        birth_date.year, birth_date.month, birth_date.day
                    ),
                    name_use=name_use,
                    name_given=name_given,
                    name_family=name_family,
                    marital_status=marital_status,
                    gender=gender,
                    us_core_race=us_core_race,
                    us_core_ethnicity=us_core_ethnicity,
                    mothers_maiden_name=mothers_maiden_name,
                    birth_place_country=birth_place_country,
                    birth_place_state=birth_place_state,
                    birth_place_city=birth_place_city,
                    disability_adjusted_life_years=disability_adjusted_life_years,
                    quality_adjusted_life_years=quality_adjusted_life_years,
                    birth_sex=birth_sex,
                    multiple_birth=multiple_birth,
                )
            ).run_sync()


def add_telecom(data_model):
    for entry in data_model.entry:
        if entry.resource.resourceType == "Patient":

            system = entry.resource.telecom[0].system
            phone_number = entry.resource.telecom[0].value
            use = entry.resource.telecom[0].use
            id = entry.resource.id
            telecom_table.insert(
                telecom_table(
                    system=system, phone_number=phone_number, use=use, patient_uid=id
                ),
            ).run_sync()


# load_json_files_to_db(file_list)

print("Working?")

# from piccolo.table import drop_tables

# drop_tables(patient_table)
