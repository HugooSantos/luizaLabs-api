from pydantic import BaseModel, Field, validator
from typing import Optional

class ProductUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=150, description="Product name (alphanumeric, up to 150 characters).")
    ean: Optional[str] = Field(None, description="EAN code (numeric, up to 13 digits).")
    price: Optional[float] = Field(None, gt=0, description="Price (numeric, greater than 0).")
    description: Optional[str] = Field(None, max_length=250, description="Description (alphanumeric, up to 250 characters).")
    sales_location: Optional[str] = Field(None, description="Sales location (event or store).")
    path_image: Optional[str] = Field(None, description="Path image.")
    active: Optional[bool] = Field(None, description="Product availability (True or False).")
    
    @validator('ean', always=True)
    def validate_ean(cls, v):
        if v and (len(v) != 13 or not v.isdigit()):
            raise ValueError('EAN must be exactly 13 digits and numeric')
        return v
    
    @validator('sales_location', always=True)
    def validate_sales_location(cls, v):
        if v and v not in ['event', 'store']:
            raise ValueError('Sales location must be either "event" or "store".')
        return v
    
    class Config:
        from_attributes = True