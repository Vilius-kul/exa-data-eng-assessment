from piccolo.columns.column_types import (
    UUID,
    Date,
    ForeignKey,
    Numeric,
    Real,
    Text,
    Varchar,
)
from piccolo.table import Table


class Patient(Table, tablename="patient_info"):
    patient_id = UUID(primary_key=True)
    name_use = Varchar(length=255)
    name_family = Varchar(length=255)
    name_given = Varchar(length=255)
    mothers_maiden_name = Varchar(length=255)
    birth_date = Date()
    deceased = Text()
    multiple_birth = Varchar(length=255)
    birth_sex = Varchar(length=2)
    gender = Varchar(length=255)
    us_core_race = Varchar(length=255)
    us_core_ethnicity = Varchar(length=255)
    marital_status = Varchar(length=255)
    birth_place_state = Varchar(length=255)
    birth_place_country = Varchar(length=255)
    birth_place_city = Varchar(length=255)
    home_address_line = Varchar(length=255)
    home_address_city = Varchar(length=255)
    home_address_state = Varchar(length=255)
    home_address_country = Varchar(length=255)
    home_address_latitude = Numeric(digits=(8, 6))
    home_address_longitude = Numeric(digits=(9, 6))
    disability_adjusted_life_years = Real()
    quality_adjusted_life_years = Real()


class Telecom(Table, tablename="telecom_info"):

    system = Varchar(length=50)
    phone_number = Varchar(length=30)
    use = Varchar(length=50)
    patient_uid = ForeignKey(references=Patient)
