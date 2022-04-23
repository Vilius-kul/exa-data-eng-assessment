from sys import prefix
from typing import Optional

from pydantic import BaseModel


class Name(BaseModel):
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
    birthDate: str  # to patient_table
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
