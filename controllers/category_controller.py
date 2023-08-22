from typing import List
from dao.category_dao import CategoryDAO
from models.schema import Category

class CategoryController:
    @staticmethod
    async def create_category(data: dict) -> Category:
        return await CategoryDAO.create_category(data)

    @staticmethod
    async def get_category_by_id(category_id: int) -> Category:
        return await CategoryDAO.get_category_by_id(category_id)

    @staticmethod
    async def get_all_categories() -> List[Category]:
        return await CategoryDAO.get_all_categories()

    @staticmethod
    async def update_category(category: Category, data: dict) -> None:
        await CategoryDAO.update_category(category, data)

    @staticmethod
    async def delete_category(category: Category) -> None:
        await CategoryDAO.delete_category(category)
