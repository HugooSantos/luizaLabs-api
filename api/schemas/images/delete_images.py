from pydantic import BaseModel

class DeleteImage(BaseModel):
    filename: str