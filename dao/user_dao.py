from tortoise.queryset import QuerySet
from models.schema import User

class UserDAO:
    @staticmethod
    async def create_user(data: dict) -> User:
        return await User.create(**data)

    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        return await User.get(pk=user_id)

    @staticmethod
    async def get_all_users() -> QuerySet[User]:
        return User.all()

    @staticmethod
    async def update_user(user: User, data: dict) -> None:
        await user.update_from_dict(data)
        await user.save()

    @staticmethod
    async def delete_user(user: User) -> None:
        await user.delete()
