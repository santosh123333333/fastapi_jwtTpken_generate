from datetime import datetime, timedelta, timezone
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.model.user import User
from app.db.database import get_db


from pwdlib import PasswordHash
from jose import JWTError, jwt

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")
# hashing password

password_hash=PasswordHash.recommended()



SECRET_KEY="My secrete key"

ALGORITHM="HS256"

# creating function to hashpassword


def hash_password(password:str):
    return password_hash.hash(password)



# password="123"

# print(hash_password(password))

#  Verify password
def verify_password(
    plain_password: str,
    hashed_password: str
) :
    return password_hash.verify(
        plain_password,
        hashed_password
    )




# create JWT token


# def cerate_access_token


def cerate_access_token(data:dict):
    to_encode=data.copy()
    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=30
    )

    to_encode.update({
        "exp": expire,
        
    })


    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

#Verify JWT and current user
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        # Find user using email from JWT sub
        user = db.query(User).filter(User.email == email).first()
        if not user:
                raise HTTPException(
                    status_code=401, 
                    detail="Invalid token"
                    )
        return user
    except JWTError:
         raise HTTPException(status_code=401,
                             detail="Invalid or expired token")




    
  
    
    
   








    


    


  


    



        

    




    

    


                         