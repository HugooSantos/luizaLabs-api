import os
from fastapi import HTTPException
from api.models.product import Product
from api.repositories import product_repository
from api.schemas.paginated_response import PaginatedResponse
from api.schemas.products.create_product import ProductCreateSchema
from api.schemas.products.product_filter import ProductFilterSchema
from sqlalchemy.orm import Session
from api.schemas.products.product import ProductSchema

from api.schemas.products.update_product import ProductUpdateSchema

def get_all(filters: ProductFilterSchema, db: Session) -> PaginatedResponse:
    try:
        total_items, total_pages, products = product_repository.get_all(filters, db)
        products_response = [ProductSchema.from_orm(product) for product in products]

        return PaginatedResponse(
            current_page=filters.page,
            page_size=filters.page_size,
            total_pages=total_pages,
            total_items=total_items,
            items=products_response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
    

def find(id: int, db: Session) -> Product:
    product = product_repository.get_by_id(db=db, id=id) 
    
    if product is None:
        raise HTTPException(status_code=404, detail="product not found")
    
    return product

def create(schema: ProductCreateSchema, db: Session) -> Product:
    product_dict = schema.dict()
    check_ean(product_dict['ean'], db=db)
    return product_repository.create(db=db, product_dict=product_dict) 

def update(id:int, schema: ProductUpdateSchema, db: Session) -> Product:
    product_dict = schema.dict()
    product = find(id,db=db)
    
    if product_dict['ean'] is not None:
        check_ean(product_dict['ean'], db=db)
    
    if product_dict['path_image'] is not None:
        delete_old_image(product, db=db)
        
    for key, value in product_dict.items():
        if value is not None and hasattr(product, key):
            setattr(product, key, value)
            
    product_repository.update(db=db, product=product)
    
    return product
    
def check_ean(ean:str, db:Session):
    product_check = product_repository.get_by_ean(db=db, ean=ean)
    
    if product_check is not None:
        raise HTTPException(status_code=422, detail="EAN already taken")

def delete_old_image(product: Product, db: Session) -> None:
    
    image_path = os.path.join('static/', product.path_image)

    if os.path.exists(image_path):
        os.remove(image_path)