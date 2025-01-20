from api.models.product import Product
from api.schemas.paginated_response import PaginatedResponse
from api.schemas.products.product_filter import ProductFilterSchema
from sqlalchemy.orm import Session


def get_all(filters: ProductFilterSchema, db: Session) -> tuple:
    page = filters.page if filters.page is not None else 1
    page_size = filters.page_size if filters.page_size is not None else 10
    is_active = filters.is_active
    search = filters.search
    sales_location = filters.sales_location
    
    query = db.query(Product).order_by(Product.id.desc())
    
    if is_active is not None:
        query = query.filter(Product.active == is_active)
    if search is not None:
        query = query.filter(Product.name.ilike(f"%{search}%"))
    if sales_location is not None:
        query = query.filter(Product.sales_location == sales_location)
    
    total_items = query.count()
    total_pages = (total_items + page_size - 1) // page_size
    offset = (page - 1) * page_size
    products = query.offset(offset).limit(page_size).all()
    return total_items, total_pages, products

def get_by_id(db: Session, id: int) -> Product:
    return db.query(Product).get(id)

def get_by_ean(db: Session, ean: str) -> Product:
    return db.query(Product).filter(Product.ean == ean).first()

def create(db: Session, product_dict) -> Product:
    product = Product(**product_dict)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update(db: Session, product: Product) -> Product:
    db.commit()
    db.refresh(product)
    return product