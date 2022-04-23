from piccolo.columns.column_types import UUID, Text, Varchar
from piccolo.table import Table


class Patient(Table, tablename="patient_info"):

    PatientUID = UUID(primary_key=True)
    NameFamily = Varchar(length=100)
    NameGiven = Varchar(length=100)
    DoB = Text(length=50)
    Gender = Text(length=50)
