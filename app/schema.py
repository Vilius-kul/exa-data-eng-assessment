from typing import Optional

from pydantic import BaseModel


class Patient(BaseModel):
    resourceType: str
    id: str  # uuid?
    meta: dict
    text: dict
    extension: list[dict]
    identifier: list[dict]
    name: list[dict]
    telecom: list[dict]
    gender: str
    birthDate: str  # date?type
    deceasedDateTime: str  # dateTime?
    address: list[dict]
    maritalStatus: dict
    multipleBirthBoolean: bool
    communication: list[dict]


class Request(BaseModel):
    method: str
    url: str


class Entry(BaseModel):
    fulUrl: Optional[str]
    resource: dict
    request: Request  # one Patient per Entry


class Fhir(BaseModel):
    resourceType: str
    type: str
    entry: list[Entry]
