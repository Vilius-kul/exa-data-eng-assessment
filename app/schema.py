from typing import Optional

from pydantic import BaseModel


class Entry(BaseModel):
    fulUrl: Optional[str]  # uuid for later
    resource: dict
    request: dict


class Bundle(BaseModel):
    resourceType: str
    type: str
    entry: list[Entry]
