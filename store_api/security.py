from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username,password):
    user=UserModel.find_by_username(username)
    print(user)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload): # the payload is the contents of the jwt tokens and we will extract the user id from the payload
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)
    

