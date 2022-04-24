import datetime
import json
import os

from db.tables import Patient as patient_table
from db.tables import Telecom as telecom_table
from schema import Fhir

# Opening JSON file
file_list = os.listdir("data")


def load_json_files(file_list):
    for j_file in range(len(file_list)):
        f = open("data/" + file_list[j_file])
        data = json.load(f)
        one_file = Fhir(**data)
        add_patient(one_file)
        f.close()


def add_patient(data_model):
    for entry in data_model.entry:
        if entry.resource.resourceType == "Patient":

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

            print(deceased)
            print(multiple_birth)
            print(home_address_line)
            print(home_address_city)
            print(home_address_state)
            print(home_address_country)
            print(home_address_longitude)
            print(home_address_longitude)
            print(name_use)
            print(name_family)
            print(name_given)
            print(gender)
            print(marital_status)
            print(birth_date)
            print(us_core_race)
            print(us_core_ethnicity)
            print(mothers_maiden_name)
            print(birth_place_state)
            print(birth_place_country)
            print(birth_place_city)
            print(disability_adjusted_life_years)
            print(quality_adjusted_life_years)
            print(birth_sex)


load_json_files(file_list)

# add_telecom(one_file)


# from piccolo.table import drop_tables

# drop_tables(patient_table, telecom_table)
