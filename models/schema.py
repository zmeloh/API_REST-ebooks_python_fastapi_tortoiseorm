from tortoise import fields, models
from pydantic import BaseModel

class Category(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

class Ebook(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    category = fields.ForeignKeyField('models.Category', related_name='ebooks')

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)

class Favorite(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='favorites')
    ebook = fields.ForeignKeyField('models.Ebook', related_name='favorites')

# Modèles Pydantic pour la validation des données
class CategoryIn(BaseModel):
    name: str

class CategoryOut(CategoryIn):
    id: int
    class Config:
        from_attributes = True 

class EbookIn(BaseModel):
    title: str
    author: str
    category_id: int

class EbookOut(EbookIn):
    id: int
    class Config:
        from_attributes = True 

class UserIn(BaseModel):
    username: str
    email: str
    password: str

class UserOut(UserIn):
    id: int
    class Config: 
        from_attributes = True 
        
class FavoriteIn(BaseModel):
    user_id: int
    ebook_id: int

class FavoriteOut(FavoriteIn):
    id: int
    class Config:
        from_attributes = True 