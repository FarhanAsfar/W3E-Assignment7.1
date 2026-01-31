import os
from dotenv import load_dotenv

load_dotenv()


class config:
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")