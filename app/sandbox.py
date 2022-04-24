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

        deceased = entry.resource.deceasedDateTime

        home_address_line = entry.resource.address[0]["line"][0]
        home_address_city = entry.resource.address[0]["city"]
        home_address_state = entry.resource.address[0]["state"]
        home_address_country = entry.resource.address[0]["country"]
        home_address_longitude = entry.resource.address[0]["extension"][0]["extension"][
            0
        ]["valueDecimal"]
        home_address_latitude = entry.resource.address[0]["extension"][0]["extension"][
            1
        ]["valueDecimal"]

        birth_date = entry.resource.birthDate
        name_use = entry.resource.name[0].use
        name_given = entry.resource.name[0].given[0]
        name_family = entry.resource.name[0].family
        marital_status = entry.resource.maritalStatus["text"]
        gender = entry.resource.gender
        us_core_race = entry.resource.extension[0]["extension"][0]["valueCoding"][
            "display"
        ]
        us_core_ethnicity = entry.resource.extension[1]["extension"][0]["valueCoding"][
            "display"
        ]
        mothers_maiden_name = entry.resource.extension[2]["valueString"]
        birth_place_state = entry.resource.extension[4]["valueAddress"]["state"]
        birth_place_country = entry.resource.extension[4]["valueAddress"]["country"]
        birth_place_city = entry.resource.extension[4]["valueAddress"]["city"]
        disability_adjusted_life_years = entry.resource.extension[5]["valueDecimal"]
        quality_adjusted_life_years = entry.resource.extension[6]["valueDecimal"]
        birth_sex = entry.resource.extension[3]["valueCode"]
        multiple_birth = entry.resource.multipleBirthBoolean

        pprint(deceased)
        pprint(multiple_birth)
        pprint(home_address_line)
        pprint(home_address_city)
        pprint(home_address_state)
        pprint(home_address_country)
        pprint(home_address_longitude)
        pprint(home_address_longitude)

        pprint(name_use)
        pprint(name_family)
        pprint(name_given)

        pprint(gender)
        pprint(marital_status)
        pprint(birth_date)
        pprint(us_core_race)
        pprint(us_core_ethnicity)
        pprint(mothers_maiden_name)
        pprint(birth_place_state)
        pprint(birth_place_country)
        pprint(birth_place_city)
        pprint(disability_adjusted_life_years)
        pprint(quality_adjusted_life_years)
        pprint(birth_sex)


# for i in range(len(one_file.entry)):
#     if one_file.entry[i].request.url == "Patient":
#         one_entry = one_file.entry[i].resource
#         one_patient = Patient(**one_entry)
#         pprint(one_patient.extension)


f.close()
