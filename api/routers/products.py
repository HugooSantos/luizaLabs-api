from fastapi import APIRouter, Depends
from api.schemas.paginated_response import PaginatedResponse
from api.schemas.products.create_product import ProductCreateSchema
from api.schemas.products.product_filter import ProductFilterSchema
from api.schemas.products.product import ProductSchema
from api.schemas.products.update_product import ProductUpdateSchema
from api.services import products_service
from sqlalchemy.orm import Session
from api.shared.dependencies import get_db
from fastapi import  Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

@router.get("/", response_model=PaginatedResponse, status_code=200)
def get_all(
    filters: ProductFilterSchema = Depends(),
    db: Session = Depends(get_db)
) -> PaginatedResponse:
    return products_service.get_all(filters=filters, db=db)

@router.get("/{id}", response_model=ProductSchema, status_code=200)
def find(
    id: int,
    db: Session = Depends(get_db)
) -> ProductSchema:
    return products_service.find(id=id, db=db)


@router.post("/", response_model=ProductSchema, status_code=200)
def create(
    schema: ProductCreateSchema,
    db: Session = Depends(get_db)
) -> ProductSchema:
    return products_service.create(schema=schema, db=db)
 
@router.put("/{id}", response_model=ProductSchema, status_code=200)
def update(
    id:int,
    schema: ProductUpdateSchema,
    db: Session = Depends(get_db)
) -> ProductSchema:
    return products_service.update(id=id, schema=schema, db=db)