
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class saleslocationEnum(str, Enum):
    EVENT = "event"
    STORE = "store"

class ProductFilterSchema(BaseModel):
    page: int = 1
    page_size: int = 20
    is_active: Optional[bool] = None
    search: Optional[str] = None
    sales_location: Optional[saleslocationEnum] = Field(None, description="Location. Can be 'event' or 'store'.")

    class Config:
        json_schema_extra = {
            "example": {
                "page": 1,
                "page_size": 20,
                "is_active": True,
                "search": "laptop"
            }
        }

