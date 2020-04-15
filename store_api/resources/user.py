from sqlalchemy import create_engine
import pandas as pd
from flask_restful import Resource,reqparse
from models.user import UserModel
my_db=create_engine('mysql://root:davidpro12@localhost')

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help='This field cannot be left blank')
    parser.add_argument('password',type=str,required=True,help='This field cannot be left blank')      

    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"This user name is already exsists, please change user name"},409        
        else:
            my_db.execute(f"""INSERT INTO prod.users (username,password) VALUES('{data['username']}','{data['password']}') """)
            return {"message":"user has been sucssefuly created!"},201









