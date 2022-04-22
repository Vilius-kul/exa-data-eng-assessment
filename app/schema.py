from pydantic import BaseModel


class ResourceType(BaseModel):
    resourceType: str
