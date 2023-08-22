from tortoise.queryset import QuerySet
from models.schema import Favorite

class FavoriteDAO:
    @staticmethod
    async def create_favorite(data: dict) -> Favorite:
        return await Favorite.create(**data)

    @staticmethod
    async def get_favorite_by_id(favorite_id: int) -> Favorite:
        return await Favorite.get(pk=favorite_id)

    @staticmethod
    async def get_all_favorites() -> QuerySet[Favorite]:
        return Favorite.all()

    @staticmethod
    async def update_favorite(favorite: Favorite, data: dict) -> None:
        await favorite.update_from_dict(data)
        await favorite.save()

    @staticmethod
    async def delete_favorite(favorite: Favorite) -> None:
        await favorite.delete()
