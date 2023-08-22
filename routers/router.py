from fastapi import APIRouter
from rest import category_handler, ebook_handler, user_handler, favorite_handler


router = APIRouter()

router.include_router(category_handler.router, prefix="/categories", tags=["categories"])
router.include_router(ebook_handler.router, prefix="/ebooks", tags=["ebooks"])
router.include_router(user_handler.router, prefix="/users", tags=["users"])
router.include_router(favorite_handler.router, prefix="/favorites", tags=["favorites"])
