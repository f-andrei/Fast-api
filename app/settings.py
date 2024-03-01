import os

DATABASE_URL = os.getenv('DATABASE_URL').replace("://", "ql://", 1)