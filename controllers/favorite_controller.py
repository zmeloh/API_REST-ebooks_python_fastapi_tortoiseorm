from typing import List
from dao.favorite_dao import FavoriteDAO
from models.schema import Favorite

class FavoriteController:
    @staticmethod
    async def create_favorite(data: dict) -> Favorite:
        return await FavoriteDAO.create_favorite(data)

    @staticmethod
    async def get_favorite_by_id(favorite_id: int) -> Favorite:
        return await FavoriteDAO.get_favorite_by_id(favorite_id)

    @staticmethod
    async def get_all_favorites() -> List[Favorite]:
        return await FavoriteDAO.get_all_favorites()

    @staticmethod
    async def update_favorite(favorite: Favorite, data: dict) -> None:
        await FavoriteDAO.update_favorite(favorite, data)

    @staticmethod
    async def delete_favorite(favorite: Favorite) -> None:
        await FavoriteDAO.delete_favorite(favorite)
