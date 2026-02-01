import os
from dotenv import load_dotenv

load_dotenv()

# a configuration container. to populate app.config dict.
class Config:
    # the key 'SQLALCHEMY_DATABASE_URI' has to be exactly like this. Flask expects as it is.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False