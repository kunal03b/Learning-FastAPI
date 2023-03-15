from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User,Gender,Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),first_name="Kunal",
         last_name="Sharma",
         Gender=Gender.male,
         roles = [Role.admin,Role.user]
         ),
    User(id=uuid4(),first_name="Sushant",
         last_name="Dhiman",
         Gender=Gender.male,
         roles = [Role.student]
         )     
]


@app.get("/")
async def read_root():
    return {"Hello": "Kunal"}