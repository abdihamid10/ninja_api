from ninja import Field, FilterSchema
from decimal import Decimal
from typing import Optional
class ProductFilterSchema(FilterSchema):
    name: str|None = Field(None, q="name__icontains")
    min_price: Decimal|None = Field(None, q="price__gte")
    max_price: Optional[Decimal] = Field(None, q="price__lte")
    

