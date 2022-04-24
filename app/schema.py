from datetime import date
from typing import Optional

from pydantic import BaseModel

# TODO: base models to create ['Medication', 'Claim', 'CareTeam', 'Provenance', 'MedicationRequest', 'CarePlan', 'Condition', 'DiagnosticReport', 'Procedure', 'Immunization', 'ImagingStudy', 'DocumentReference', 'MedicationAdministration', 'ExplanationOfBenefit', 'Observation', 'Encounter']


class Name(BaseModel):  # to patient_table
    family: Optional[str]
    given: Optional[list[str]]
    prefix: list[str]
    use: Optional[str]


class Patient(BaseModel):
    resourceType: str
    id: str  # to patient_table
    meta: dict
    text: dict
    extension: list[dict]
    identifier: list[dict]
    name: list[Name]  # to base model
    telecom: list[dict]
    gender: str  # to patient_table
    birthDate: date  # to patient_table
    deceasedDateTime: Optional[str]  # dateTime?
    address: list[dict]
    maritalStatus: dict
    multipleBirthBoolean: bool
    communication: list[dict]


class EntryRequest(BaseModel):
    method: str
    url: str


class Entry(BaseModel):
    fulUrl: Optional[str]
    resource: dict
    request: EntryRequest


class Fhir(BaseModel):
    resourceType: str
    type: str
    entry: list[Entry]
