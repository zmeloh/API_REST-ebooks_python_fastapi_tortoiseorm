from tortoise.queryset import QuerySet
from models.schema import Category

class CategoryDAO:
    @staticmethod
    async def create_category(data: dict) -> Category:
        return await Category.create(**data)

    @staticmethod
    async def get_category_by_id(category_id: int) -> Category:
        return await Category.get(pk=category_id)

    @staticmethod
    async def get_all_categories() -> QuerySet[Category]:
        return Category.all()

    @staticmethod
    async def update_category(category: Category, data: dict) -> None:
        await category.update_from_dict(data)
        await category.save()

    @staticmethod
    async def delete_category(category: Category) -> None:
        await category.delete()
