from ninja import Field, Router
from typing import List, Optional
from .models import Product,Tag
from .Schema import ProductSchema, ProductCreateSchema, ProductPatchSchema,TagSchema
from ninja import File, Form
from ninja.files import UploadedFile
from decimal import Decimal
import json
from pydantic import TypeAdapter
from django.shortcuts import get_object_or_404
from .FilterSchema import ProductFilterSchema
from ninja import Query
router = Router()

@router.get("/tags", response=List[TagSchema])
def listTags(request):
    tags = Tag.objects.all()
    return tags


@router.get("/products", response=List[ProductSchema])
def listProducts(request, filters: ProductFilterSchema=Query(...)):
    products = Product.objects.all().order_by("-id")
    products = filters.filter(products)
    return products


@router.post("/products", response=ProductSchema)
def createProduct(request, name: str = Form(...), 
                  price: Decimal = Form(...), 
                  tags_ids: str = Form(...), 
                  image: UploadedFile = File(...)):
    product = Product.objects.create(
        name = name,
        price = price,
        image = image,
    )
    clean_ids = TypeAdapter(List[int]).validate_python(json.loads(tags_ids))
    product.tags.set(clean_ids)
    return product

@router.post("/products/{product_id}", response=ProductSchema)
def createProduct(request,product_id: int, name: Optional[str] = Form(None), 
                  price: Optional[Decimal] = Form(None), 
                  tags_ids: Optional[str] = Form(None), 
                  image: Optional[UploadedFile] = File(None)):

    product = get_object_or_404(Product, id=product_id)
    if name is not None:
        product.name = name

    if price is not None:
        product.price = price

    if image:
        product.image = image

    if tags_ids is not None:
        clean_ids = TypeAdapter(List[int]).validate_python(json.loads(tags_ids))
        product.tags.set(clean_ids)
    return product

@router.delete("/product/{product_id}")
def deleteProduct(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"message": "deleted successfully"}

