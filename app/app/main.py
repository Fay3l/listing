import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from .database.db import DB
from .database.session import init_db
from .models.products import Products
from .models.lists import Lists
from .models.users import Users

load_dotenv()

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv('DATABASE_URL')
database = DB(DATABASE_URL)
database.connect()
init_db(database)


@app.get("/")
async def root():
    return {"message": "Hello World"}










