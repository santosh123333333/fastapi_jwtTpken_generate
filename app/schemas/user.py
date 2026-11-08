from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class Usercreate(BaseModel):
    full_name:str
    email:str
    password:str




# user Response
class UserResponse(BaseModel):
    id :int
    full_name:str

    email:str
    created_at:datetime



model_config = ConfigDict(
        from_attributes=True
    )



#Login 


class Userlogin(BaseModel):
    email:str
    password:str