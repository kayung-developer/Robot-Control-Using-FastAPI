from pydantic import BaseModel

class Command(BaseModel):
    action: str
