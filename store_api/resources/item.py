from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import pandas as pd
from sqlalchemy import create_engine
my_db=create_engine('mysql://root:davidpro12@localhost')


class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='This field cannot be left blank')

    @classmethod
    def find_by_name(self,itemname):
        item_row=pd.read_sql_query(f"""select * from prod.items where itemname='{itemname}' """,my_db)
        if len(item_row)==1:
            return item_row
        else: return None    

    @jwt_required() #when we do this it means now we need to authenticate before we can do the get requests
    def get(self,name):
        item_row=Item.find_by_name(name)
        if len(item_row)==1:
            return {"item":{"item name":item_row['itemname'][0],"price":item_row["price"][0]}}
        else:
            return {"message":"item was not found"},404  

    def post(self,name):
        item_row=Item.find_by_name(name)
        if item_row:
            return {'message':"An item with the name '{}' already exsists.".format(name)},400
        else:
            data=Item.parser.parse_args()
            my_db.execute(f"""INSERT INTO prod.items (itemname,price)VALUES ('{name}',{data["price"]})""")    
            return {"message":f"""item '{name}' with the price {data["price"]} was successfuly created!"""},201 #seconed parameter returns the status code. 201= CREATED

    def delete(self,name):
        my_db.execute(f"""delete from prod.items where itemname='{name}' """)        
        return {'message':f"""Item "{name}" has been deleted!"""}

    def put(self, name):
        data=Item.parser.parse_args()
        item=self.find_by_name(name)
        try:
            if item is None:
                my_db.execute(f"""INSERT INTO prod.items (itemname,price)VALUES ('{name}',{data["price"]})""")
                return{"message":f"""new item {name} with the price {data["price"]} was created """},201
            else:
                my_db.execute(f"""update prod.items set price={data["price"]} where itemname='{name}' """)
                return{"message":f"""item '{name}' was succesfully updated with new price: '{data["price"]}' """},200
        except:
            return{"message":"something went wrong with the inserting"},500

class Items(Resource):
    @classmethod
    def turn2dict(self,row,all_items):
        all_items.append({"itemname":row.itemname,"price":row.price})
    def get(self):
        all_items=[]
        df=pd.read_sql_query("select * from prod.items",my_db)
        df=df.apply(lambda row:self.turn2dict(row,all_items),axis=1)
        return {'items':all_items}
