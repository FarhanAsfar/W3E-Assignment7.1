import os
from dotenv import load_dotenv

load_dotenv()

# a configuration container. to populate app.config dict.
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# the key 'SQLALCHEMY_DATABASE_URI' has to be exactly like this. Flask expects as it is.