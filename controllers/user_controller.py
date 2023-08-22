from typing import List
from dao.user_dao import UserDAO
from models.schema import User

class UserController:
    @staticmethod
    async def create_user(data: dict) -> User:
        return await UserDAO.create_user(data)

    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        return await UserDAO.get_user_by_id(user_id)

    @staticmethod
    async def get_all_users() -> List[User]:
        return await UserDAO.get_all_users()

    @staticmethod
    async def update_user(user: User, data: dict) -> None:
        await UserDAO.update_user(user, data)

    @staticmethod
    async def delete_user(user: User) -> None:
        await UserDAO.delete_user(user)
