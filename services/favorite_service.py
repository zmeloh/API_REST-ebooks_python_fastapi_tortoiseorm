from typing import List
from controllers.favorite_controller import FavoriteController
from models.schema import Favorite

class FavoriteService:
    @staticmethod
    async def create_favorite(data: dict) -> Favorite:
        return await FavoriteController.create_favorite(data)

    @staticmethod
    async def get_favorite_by_id(favorite_id: int) -> Favorite:
        return await FavoriteController.get_favorite_by_id(favorite_id)

    @staticmethod
    async def get_all_favorites() -> List[Favorite]:
        return await FavoriteController.get_all_favorites()

    @staticmethod
    async def update_favorite(favorite: Favorite, data: dict) -> None:
        await FavoriteController.update_favorite(favorite, data)

    @staticmethod
    async def delete_favorite(favorite: Favorite) -> None:
        await FavoriteController.delete_favorite(favorite)
