from typing import List, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    current_page: int
    page_size: int
    total_pages: int
    total_items: int
    items: List[T]