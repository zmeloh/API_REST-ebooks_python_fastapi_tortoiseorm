from typing import List
from dao.ebook_dao import EbookDAO
from models.schema import Ebook

class EbookController:
    @staticmethod
    async def create_ebook(data: dict) -> Ebook:
        return await EbookDAO.create_ebook(data)

    @staticmethod
    async def get_ebook_by_id(ebook_id: int) -> Ebook:
        return await EbookDAO.get_ebook_by_id(ebook_id)

    @staticmethod
    async def get_all_ebooks() -> List[Ebook]:
        return await EbookDAO.get_all_ebooks()

    @staticmethod
    async def update_ebook(ebook: Ebook, data: dict) -> None:
        await EbookDAO.update_ebook(ebook, data)

    @staticmethod
    async def delete_ebook(ebook: Ebook) -> None:
        await EbookDAO.delete_ebook(ebook)
