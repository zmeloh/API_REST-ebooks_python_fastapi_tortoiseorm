from fastapi import FastAPI
from routers import router
from tortoise.contrib.fastapi import register_tortoise
from decouple import config

app = FastAPI()

# Inclure le routeur principal
app.include_router(router.router)

# Récupérer les valeurs du fichier .env
DB_TYPE = config("DB_TYPE")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")

# Configuration de la base de données avec Tortoise ORM
if DB_TYPE == "sqlite":
    db_url = f"sqlite://{DB_NAME}.sqlite3"
elif DB_TYPE == "mysql":
    db_url = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
elif DB_TYPE == "postgresql":
    db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    raise ValueError("Invalid DB_TYPE in .env")

register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["models.schema"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
