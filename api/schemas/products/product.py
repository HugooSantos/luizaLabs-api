from pydantic import BaseModel
import datetime

class ProductSchema(BaseModel):
    id: int
    name: str
    ean: str
    price: float
    description: str
    path_image: str
    active: bool
    sales_location: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True 