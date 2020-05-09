
from pydantic import BaseModel, Field
from typing import List, Optional
from app.products.schemes import ProductForGetProduct
from app.helpers import ObjectIdStr, PaginatedResult


class BaseFields:
    id: ObjectIdStr = Field(title='ID of subtype')
    id_required: ObjectIdStr = Field(..., title='ID of subtype')
    title: str = Field(title='Title of subtype')
    title_required: str = Field(..., title='Title of subtype')
    status: bool = Field(title='Active subtype or not')
    status_required: bool = Field(..., title='Active subtype or not')
    products: List[ProductForGetProduct] = Field(title='list of products')
    products_required: List[ProductForGetProduct] = Field(..., title='list of products')


class SubtypeForGetSubtype(BaseModel):
    id: ObjectIdStr = BaseFields.id_required
    title: str = BaseFields.title_required
    status: bool = BaseFields.status_required
    products: List[ProductForGetProduct] = BaseFields.products_required

    class Config:
        orm_mode = True


class SubtypeForGetSubtypes(BaseModel):
    id: ObjectIdStr = BaseFields.id_required
    title: Optional[str] = BaseFields.title
    status: Optional[bool] = BaseFields.status
    products: Optional[List[ProductForGetProduct]] = BaseFields.products

    class Config:
        orm_mode = True


class ListOfSubtypes(PaginatedResult):
    result: List[SubtypeForGetSubtypes]
