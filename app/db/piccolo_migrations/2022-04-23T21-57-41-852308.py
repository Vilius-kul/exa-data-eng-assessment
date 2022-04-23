from piccolo.apps.migrations.auto.migration_manager import MigrationManager

ID = "2022-04-23T21:57:41:852308"
VERSION = "0.74.1"
DESCRIPTION = "rename columns names"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="db", description=DESCRIPTION)

    manager.rename_column(
        table_class_name="Patient",
        tablename="patient_info",
        old_column_name="DoB",
        new_column_name="dob",
        old_db_column_name="DoB",
        new_db_column_name="dob",
    )

    manager.rename_column(
        table_class_name="Patient",
        tablename="patient_info",
        old_column_name="Gender",
        new_column_name="family_name",
        old_db_column_name="Gender",
        new_db_column_name="family_name",
    )

    manager.rename_column(
        table_class_name="Patient",
        tablename="patient_info",
        old_column_name="NameFamily",
        new_column_name="gender",
        old_db_column_name="NameFamily",
        new_db_column_name="gender",
    )

    manager.rename_column(
        table_class_name="Patient",
        tablename="patient_info",
        old_column_name="NameGiven",
        new_column_name="name_given",
        old_db_column_name="NameGiven",
        new_db_column_name="name_given",
    )

    manager.rename_column(
        table_class_name="Patient",
        tablename="patient_info",
        old_column_name="PatientUID",
        new_column_name="patient_uid",
        old_db_column_name="PatientUID",
        new_db_column_name="patient_uid",
    )

    return manager
