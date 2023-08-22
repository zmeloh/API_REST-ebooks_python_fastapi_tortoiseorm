from typing import List
from controllers.category_controller import CategoryController
from models.schema import Category

class CategoryService:
    @staticmethod
    async def create_category(data: dict) -> Category:
        return await CategoryController.create_category(data)

    @staticmethod
    async def get_category_by_id(category_id: int) -> Category:
        return await CategoryController.get_category_by_id(category_id)

    @staticmethod
    async def get_all_categories() -> List[Category]:
        return await CategoryController.get_all_categories()

    @staticmethod
    async def update_category(category: Category, data: dict) -> None:
        await CategoryController.update_category(category, data)

    @staticmethod
    async def delete_category(category: Category) -> None:
        await CategoryController.delete_category(category)
