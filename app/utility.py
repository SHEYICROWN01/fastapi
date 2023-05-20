from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#this function is use to hash password using bcrypt 
def hash(password: str):
    return pwd_context.hash(password)


# this function get the hashed password and also get the user plain password. the function will first hash the user plain password then it will compare the two password to see if this match
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
