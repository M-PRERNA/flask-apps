import pandas as pd
from sqlalchemy import create_engine
my_db=create_engine('mysql://root:davidpro12@localhost')
df=pd.read_sql_query("select * from prod.items",my_db)
all_items=[]

def turn2dict(row):
    all_items.append({"itemname":row.itemname,"price":row.price})
df=df.apply(lambda row:turn2dict(row),axis=1)

print(all_items)