import os

DATABASE_NAME = "learning.db"
DATABASE_DRIVER = "sqlite"

DATABASE_PATH = os.path.abspath(DATABASE_NAME)
DATABASE_URL = "{0}:///{1}".format(DATABASE_DRIVER, DATABASE_PATH.replace("\\", "/"))

