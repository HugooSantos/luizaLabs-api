import os
from fastapi import HTTPException
from api.models.product import Product
from api.repositories import product_repository
from api.schemas.paginated_response import PaginatedResponse
from api.schemas.products.create_product import ProductCreateSchema
from api.schemas.products.product_filter import ProductFilterSchema
from sqlalchemy.orm import Session
from api.schemas.products.product import ProductSchema


def validate_ean(ean: str, db: Session) -> None:
    product = product_repository.get_by_ean(db=db, ean=ean)
    if product is not None:
        raise HTTPException(status_code=422, detail="Product already ean taken")

