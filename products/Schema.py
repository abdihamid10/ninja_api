from ninja import Schema, Field
from .models import Product, Tag,Category
from decimal import Decimal
from typing import Optional, List



class TagSchema(Schema):
    id: int
    name: str


class ProductSchema(Schema):
    id: int
    name: str
    price: Decimal
    tags: List[TagSchema]
    image: str

class ProductCreateSchema(Schema):
    name: str = Field(max_length=100, min_length=2)
    price: Decimal = Field(max_digits=10, decimal_places=2, gt=0)
    tags: List[int]  


class ProductPatchSchema(Schema):
    name: Optional[str] = Field(None,max_length=100, min_length=2)
    price: Optional[Decimal] = Field(None,max_digits=10, decimal_places=2, gt=0)
    tags_ids: Optional[List[int]] = None  
