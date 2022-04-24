from piccolo.columns.column_types import UUID, Date, Text, Varchar
from piccolo.table import Table


class Patient(Table, tablename="patient_info"):

    patient_uid = UUID(primary_key=True)
    family_name = Varchar(length=100)
    name_given = Varchar(length=100)
    dob = Date()
    gender = Text(length=50)
