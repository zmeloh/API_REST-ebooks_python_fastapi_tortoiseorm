from fastapi import APIRouter
from typing import List
from models.schema import Favorite, FavoriteIn, FavoriteOut, UserOut, EbookOut
from .exceptions_handler import NotFoundError

router = APIRouter()

@router.post("/", response_model=FavoriteOut)
async def create_favorite(favorite: FavoriteIn):
    favorite_obj = await Favorite.create(**favorite.dict())
    return FavoriteOut.from_orm(favorite_obj)

@router.get("/{favorite_id}", response_model=FavoriteOut)
async def get_favorite(favorite_id: int):
    favorite_obj = await Favorite.filter(id=favorite_id).first()
    if not favorite_obj:
        raise NotFoundError(detail={"message": "Favorite not found"})
    return FavoriteOut.from_orm(favorite_obj)

@router.get("/", response_model=List[FavoriteOut])
async def get_all_favorites():
    favorites = await Favorite.all()
    return [FavoriteOut.from_orm(favorite) for favorite in favorites]

@router.put("/{favorite_id}", response_model=FavoriteOut)
async def update_favorite(favorite_id: int, favorite: FavoriteIn):
    await Favorite.filter(id=favorite_id).update(**favorite.dict())
    favorite_obj = await Favorite.filter(id=favorite_id).first()
    return FavoriteOut.from_orm(favorite_obj)

@router.delete("/{favorite_id}")
async def delete_favorite(favorite_id: int):
    deleted_count = await Favorite.filter(id=favorite_id).delete()
    if not deleted_count:
        raise NotFoundError(detail={"message": "Favorite not found"})
    return {"message": "Favorite deleted"}
