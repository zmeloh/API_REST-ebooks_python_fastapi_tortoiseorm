from tortoise.queryset import QuerySet
from models.schema import Ebook

class EbookDAO:
    @staticmethod
    async def create_ebook(data: dict) -> Ebook:
        return await Ebook.create(**data)

    @staticmethod
    async def get_ebook_by_id(ebook_id: int) -> Ebook:
        return await Ebook.get(pk=ebook_id)

    @staticmethod
    async def get_all_ebooks() -> QuerySet[Ebook]:
        return Ebook.all()

    @staticmethod
    async def update_ebook(ebook: Ebook, data: dict) -> None:
        await ebook.update_from_dict(data)
        await ebook.save()

    @staticmethod
    async def delete_ebook(ebook: Ebook) -> None:
        await ebook.delete()
