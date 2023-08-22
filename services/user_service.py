from typing import List
from controllers.user_controller import UserController
from models.schema import User

class UserService:
    @staticmethod
    async def create_user(data: dict) -> User:
        return await UserController.create_user(data)

    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        return await UserController.get_user_by_id(user_id)

    @staticmethod
    async def get_all_users() -> List[User]:
        return await UserController.get_all_users()

    @staticmethod
    async def update_user(user: User, data: dict) -> None:
        await UserController.update_user(user, data)

    @staticmethod
    async def delete_user(user: User) -> None:
        await UserController.delete_user(user)
