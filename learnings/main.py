from dotenv import  load_dotenv
import os

load_dotenv(".env")

username: str = os.getenv('USER_NAME')
password: str = os.getenv('PASSWORD')
print(username)
print(password)