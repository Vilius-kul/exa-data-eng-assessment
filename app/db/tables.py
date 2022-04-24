from piccolo.columns.column_types import UUID, Date, ForeignKey, Text, Varchar
from piccolo.table import Table


class Patient(Table, tablename="patient_info"):

    patient_uid = UUID(primary_key=True)
    family_name = Varchar(length=100)
    name_given = Varchar(length=100)
    dob = Date()
    gender = Text(length=50)


class Telecom(Table, tablename="telecom_info"):

    system = Varchar(length=50)
    phone_number = Varchar(length=30)
    use = Varchar(length=50)
    patient_uid = ForeignKey(references=Patient)
