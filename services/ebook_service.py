from typing import List
from controllers.ebook_controller import EbookController
from models.schema import Ebook

class EbookService:
    @staticmethod
    async def create_ebook(data: dict) -> Ebook:
        return await EbookController.create_ebook(data)

    @staticmethod
    async def get_ebook_by_id(ebook_id: int) -> Ebook:
        return await EbookController.get_ebook_by_id(ebook_id)

    @staticmethod
    async def get_all_ebooks() -> List[Ebook]:
        return await EbookController.get_all_ebooks()

    @staticmethod
    async def update_ebook(ebook: Ebook, data: dict) -> None:
        await EbookController.update_ebook(ebook, data)

    @staticmethod
    async def delete_ebook(ebook: Ebook) -> None:
        await EbookController.delete_ebook(ebook)
