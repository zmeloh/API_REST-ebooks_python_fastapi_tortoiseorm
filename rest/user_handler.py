from fastapi import APIRouter, HTTPException
from typing import List
from models.schema import User, UserIn, UserOut
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create_user(user: UserIn):
    user_obj = await User.create(**user.dict())
    return UserOut.from_orm(user_obj)

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    user_obj = await User.filter(id=user_id).first()
    if not user_obj:
        raise HTTPNotFoundError(detail="User not found")
    return UserOut.from_orm(user_obj)

@router.get("/", response_model=List[UserOut])
async def get_all_users():
    users = await User.all()
    return [UserOut.from_orm(user) for user in users]

@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    await User.filter(id=user_id).update(**user.dict())
    user_obj = await User.filter(id=user_id).first()
    return UserOut.from_orm(user_obj)

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPNotFoundError(detail="User not found")
    return {"message": "User deleted"}
