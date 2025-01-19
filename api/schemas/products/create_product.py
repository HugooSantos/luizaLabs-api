from pydantic import BaseModel, Field, validator
from datetime import datetime

class ProductCreateSchema(BaseModel):
    name: str = Field(..., max_length=150, description="Product name (alphanumeric, up to 150 characters).")
    ean: str = Field(..., description="EAN code (numeric, up to 13 digits).")
    price: float = Field(..., gt=0, description="Price (numeric, greater than 0).")
    description: str = Field(..., max_length=250, description="Description (alphanumeric, up to 250 characters).")
    sales_location: str = Field(..., description="Sales location (event or store).")
    path_image: str = Field(..., description="Path image.")
    
    @validator('ean')
    def validate_ean(cls, v):
        if len(v) != 13 or not v.isdigit():
            raise ValueError('EAN must be exactly 13 digits and numeric')
        return v
    
    @validator('sales_location')
    def validate_sales_location(cls, v):
        if v and v not in ['event', 'store']:
            raise ValueError('Sales location must be either "event" or "store".')
        return v
    
    class Config:
        from_attributes = True 