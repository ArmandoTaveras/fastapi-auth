from typing import Union

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from auth import oauth2_scheme, get_current_active_user

app = FastAPI()

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
@app.get("/protected-route/")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    print(current_user)