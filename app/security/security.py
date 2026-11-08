from datetime import datetime, timedelta, timezone

from pwdlib import PasswordHash
from jose import jwt


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




    


                         