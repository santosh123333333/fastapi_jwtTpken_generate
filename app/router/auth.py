from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt

from app.db.database import get_db
from app.schemas import user
from app.schemas.user import UserResponse, Usercreate,Userlogin
from sqlalchemy.orm import Session
from app.model.user import User
from app.security.security import cerate_access_token, hash_password, verify_password

router=APIRouter()

#creating user registration

@router.post("/Register",response_model=UserResponse)

def register(user_data:Usercreate,db:Session=Depends(get_db)):


    existing_user=db.query(User).filter(User.email==user_data.email).first()

    if existing_user:
        raise HTTPException(status_code=400,
                            detail="User already exixsts ")

    hashed_password=hash_password(
        user_data.password
    )

    new_user=User(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password= hashed_password


    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
    

    except Exception:
        db.rollback()

    return new_user




# Login Api
@router.post("/login")
def login(user:Userlogin,db:Session=Depends(get_db)):

    db_user=db.query(User).filter(User.email==user.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="Invalid email and password")

    
# user in db we need to verify pass word

#password varify
   
    valid_password=verify_password(user.password,db_user.hashed_password)

    if not valid_password:
        raise HTTPException(
            status_code=404,
            detail="Invalid email or password"
        )


    # Token Generation 
    data={
        "sub":db_user.email
    }

    access_token=cerate_access_token(
        data


    )

    return{
        "message":"Login successfull",
        "access_token":access_token
    }






    
  



