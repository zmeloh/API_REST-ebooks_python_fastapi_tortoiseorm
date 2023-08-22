from fastapi import APIRouter, HTTPException
from typing import List
from models.schema import Category, CategoryIn, CategoryOut
from .exceptions_handler import NotFoundError

router = APIRouter()

@router.post("/", response_model=CategoryOut)
async def create_category(category: CategoryIn):
    category_obj = await Category.create(**category.dict())
    return CategoryOut.from_orm(category_obj)

@router.get("/{category_id}", response_model=CategoryOut)
async def get_category(category_id: int):
    category_obj = await Category.filter(id=category_id).first()
    if not category_obj:
        raise NotFoundError(detail={"message": "Category not found"})
    return CategoryOut.from_orm(category_obj)

@router.get("/", response_model=List[CategoryOut])
async def get_all_categories():
    categories = await Category.all()
    return [CategoryOut.from_orm(category) for category in categories]

@router.put("/{category_id}", response_model=CategoryOut)
async def update_category(category_id: int, category: CategoryIn):
    await Category.filter(id=category_id).update(**category.dict())
    category_obj = await Category.filter(id=category_id).first()
    return CategoryOut.from_orm(category_obj)

@router.delete("/{category_id}")
async def delete_category(category_id: int):
    deleted_count = await Category.filter(id=category_id).delete()
    if not deleted_count:
        raise NotFoundError(detail={"message": "Category not found"})
    return {"message": "Category deleted"}
