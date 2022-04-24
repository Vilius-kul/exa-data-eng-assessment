from datetime import date, datetime
from typing import Literal, Optional, Union

from pydantic import BaseModel, Field, parse_obj_as
from typing_extensions import Annotated


class Name(BaseModel):  # to patient_table
    family: Optional[str]
    given: Optional[list[str]]
    prefix: Optional[list[str]]
    use: Optional[str]


class Telecom(BaseModel):
    system: Optional[str]
    value: Optional[str]
    use: Optional[str]


class Condition(BaseModel):
    resourceType: Literal["Condition"]
    id: str


class Patient(BaseModel):
    resourceType: Literal["Patient"]
    id: str
    meta: dict
    text: dict
    extension: list[dict]
    identifier: list[dict]
    name: list[Name]
    telecom: list[Telecom]
    gender: str
    birthDate: date
    deceasedDateTime: Optional[datetime]
    address: list[dict]
    maritalStatus: dict
    multipleBirthBoolean: Optional[str]
    communication: list[dict]  # patient language


class DiagnosticReport(BaseModel):
    resourceType: Literal["DiagnosticReport"]
    id: str


class Observation(BaseModel):
    resourceType: Literal["Observation"]
    id: str


class EntryRequest(BaseModel):
    method: str
    url: str


class Medication(BaseModel):
    resourceType: Literal["Medication"]
    id: str


class Claim(BaseModel):
    resourceType: Literal["Claim"]
    id: str


class CareTeam(BaseModel):
    resourceType: Literal["CareTeam"]
    id: str


class Provenance(BaseModel):
    resourceType: Literal["Provenance"]
    id: str


class MedicationRequest(BaseModel):
    resourceType: Literal["MedicationRequest"]
    id: str


class CarePlan(BaseModel):
    resourceType: Literal["CarePlan"]
    id: str


class Procedure(BaseModel):
    resourceType: Literal["Procedure"]
    id: str


class Immunization(BaseModel):
    resourceType: Literal["Immunization"]
    id: str


class ImagingStudy(BaseModel):
    resourceType: Literal["ImagingStudy"]
    id: str


class DocumentReference(BaseModel):
    resourceType: Literal["DocumentReference"]
    id: str


class MedicationAdministration(BaseModel):
    resourceType: Literal["MedicationAdministration"]
    id: str


class ExplanationOfBenefit(BaseModel):
    resourceType: Literal["ExplanationOfBenefit"]
    id: str


class Encounter(BaseModel):
    resourceType: Literal["Encounter"]
    id: str


class AllergyIntolerance(BaseModel):
    resourceType: Literal["AllergyIntolerance"]
    id: str


class Device(BaseModel):
    resourceType: Literal["Device"]
    id: str


class SupplyDelivery(BaseModel):
    resourceType: Literal["SupplyDelivery"]
    id: str


class Entry(BaseModel):
    fulUrl: Optional[str]
    resource: Union[
        Patient,
        Condition,
        DiagnosticReport,
        Observation,
        Medication,
        Claim,
        CareTeam,
        Provenance,
        MedicationRequest,
        CarePlan,
        Procedure,
        Immunization,
        ImagingStudy,
        DocumentReference,
        MedicationAdministration,
        ExplanationOfBenefit,
        Encounter,
        AllergyIntolerance,
        Device,
        SupplyDelivery,
    ] = Field(..., discriminator="resourceType")
    request: EntryRequest


class Fhir(BaseModel):
    resourceType: str
    type: str
    entry: list[Entry]
