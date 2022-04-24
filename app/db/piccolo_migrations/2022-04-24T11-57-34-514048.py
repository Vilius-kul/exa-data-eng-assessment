from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import UUID, Date, Text, Varchar
from piccolo.columns.defaults.date import DateNow
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod

ID = "2022-04-24T11:57:34:514048"
VERSION = "0.74.1"
DESCRIPTION = "New table with corret data column"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="db", description=DESCRIPTION)

    manager.add_table("Patient", tablename="patient_info")

    manager.add_column(
        table_class_name="Patient",
        tablename="patient_info",
        column_name="patient_uid",
        db_column_name="patient_uid",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": True,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Patient",
        tablename="patient_info",
        column_name="family_name",
        db_column_name="family_name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Patient",
        tablename="patient_info",
        column_name="name_given",
        db_column_name="name_given",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Patient",
        tablename="patient_info",
        column_name="dob",
        db_column_name="dob",
        column_class_name="Date",
        column_class=Date,
        params={
            "default": DateNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Patient",
        tablename="patient_info",
        column_name="gender",
        db_column_name="gender",
        column_class_name="Text",
        column_class=Text,
        params={
            "length": 50,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
