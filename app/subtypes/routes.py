
from fastapi import APIRouter, Depends
from . import functions as funcs
from .doc_info import doc_get_subtype, doc_get_subtypes

from app.helpers import Pag

subtypes_router = APIRouter()


@subtypes_router.get('/subtypes', **doc_get_subtypes)
def get_subtypes(pag: Pag = Depends()):
    return funcs.get_subtypes(**pag.dict())


@subtypes_router.post('/subtypes')
def create_subtype():
    pass


@subtypes_router.get('/subtypes/{subtype_id}', **doc_get_subtype)
def get_subtype(subtype_id: str):
    return funcs.get_subtype(subtype_id)


@subtypes_router.put('/subtypes/{subtype_id}')
def update_subtype(subtype_id):
    pass


@subtypes_router.delete('/subtypes/{subtype_id}')
def delete_subtype(subtype_id):
    pass
