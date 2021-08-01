from sys import version
from fastapi import FastAPI
from sqlalchemy.sql.expression import desc
from routes.user import user

app = FastAPI(
    title="my first API",
    description="My primera API con fast",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)
app.include_router(user)

