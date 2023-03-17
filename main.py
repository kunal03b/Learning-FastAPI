from typing import List
from uuid import uuid4,UUID
from fastapi import FastAPI,HTTPException
from models import User,Gender,Role,UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(id=UUID("fe622abc-15a3-4476-8faa-a8b8a99d68e5"),
         first_name="Kunal",
         last_name="Sharma",
         Gender=Gender.male,
         roles = [Role.admin,Role.user]
         ),
    User(id=UUID("0d5e3b16-ad53-41e4-aad4-f62f5549804a"),first_name="Sushant",
         last_name="Dhiman",
         Gender=Gender.male,
         roles = [Role.student]
         )     
]


@app.get("/")
async def read_root():
    return {"Hello": "Kunal"}

@app.get("/api/v1/users")
async def fetch_users():
    return db; 

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return{"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail = f"user with id:{user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}")
async def update_uder(user_update: UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            # if user_update.gender is not None:
            #     user.gender = user_update.gender
            return
    raise HTTPException(
        status_code=404,
        detail="user with id: {user_id} does not exist"
    )