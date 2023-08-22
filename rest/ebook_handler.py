from fastapi import APIRouter
from typing import List
from models.schema import Ebook, EbookIn, EbookOut, CategoryOut
from .exceptions_handler import NotFoundError

router = APIRouter()

@router.post("/", response_model=EbookOut)
async def create_ebook(ebook: EbookIn):
    ebook_obj = await Ebook.create(**ebook.dict(exclude={"category_id"}))
    return EbookOut.from_orm(ebook_obj)

@router.get("/{ebook_id}", response_model=EbookOut)
async def get_ebook(ebook_id: int):
    ebook_obj = await Ebook.filter(id=ebook_id).first()
    if not ebook_obj:
        raise NotFoundError(detail={"message": "Ebook not found"})
    return EbookOut.from_orm(ebook_obj)

@router.get("/", response_model=List[EbookOut])
async def get_all_ebooks():
    ebooks = await Ebook.all()
    return [EbookOut.from_orm(ebook) for ebook in ebooks]

@router.put("/{ebook_id}", response_model=EbookOut)
async def update_ebook(ebook_id: int, ebook: EbookIn):
    await Ebook.filter(id=ebook_id).update(**ebook.dict(exclude={"category_id"}))
    ebook_obj = await Ebook.filter(id=ebook_id).first()
    return EbookOut.from_orm(ebook_obj)

@router.delete("/{ebook_id}")
async def delete_ebook(ebook_id: int):
    deleted_count = await Ebook.filter(id=ebook_id).delete()
    if not deleted_count:
        raise NotFoundError(detail={"message": "Ebook not found"})
    return {"message": "Ebook deleted"}
