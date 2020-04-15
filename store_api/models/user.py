import pandas as pd
from sqlalchemy import create_engine

my_db=create_engine('mysql://root:davidpro12@localhost')

class UserModel:
    def __init__(self, _id,username,password):
        self.id=_id
        self.username=username
        self.password=password

    def __str__(self):
        return f"({self.id},{self.username},{self.password})"

    @classmethod
    def find_by_username(cls,username):
        df=pd.read_sql_query(f"""select * from prod.users where username='{username}'""",con=my_db)
        if len(df)==1:
            user=cls(int(df['id'][0]),df['username'][0],df['password'][0])
            return user
        else:
            user=None
            return user    

    @classmethod
    def find_by_id(cls,_id):   
        df=pd.read_sql_query(f"""select * from prod.users where id={_id}""",con=my_db)
        if len(df)==1:
            user=cls(df['id'][0],df['username'][0],df['password'][0])
            return user
        else:
            user=None
            return user         
