from flask import Flask,request
from flask_restful import Resource,Api,reqparse #resource is a thing that api can return, for example if our api concerned(מתייחס/קשור) to students so resource will return students
#with reqparse we can determine what will be get in the request(some specific elements will be passed in the json payload) 
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,Items

app=Flask(__name__)
app.secret_key='david' #for encryption the data
api=Api(app)#allow easialy add resource to the api
#api works with resources and every resource has to be a class! and each class inherents(יורש) Resource

jwt=JWT(app,authenticate,identity)
"""JWT creates new end-point /auth, when we call /auth we send it username and pass.
then jwt exctension gets and username and pass and sends it over to authentication function,
if the authentication passed good it will return the user and that becomes sort of identity, 
so what happned next is the auth end-point returns a jwt-token, 
the jw-token doesnt do anything but we can send it to the next request we make(so when we send a jw-token, 
what the jwt does: it calls to identity function and it uses the jwt-token to get the user id and with that 
it gets the correct user for that user id that jwt-token represents,
and if it cant do that it means that the user was authenticated the jwt-token is valid and all is good)"""


api.add_resource(Item,'/item/<string:name>') #the seconed parameter equals to this: @app.route('/item/<string:name>')        
api.add_resource(Items,'/items')
api.add_resource(UserRegister,'/register')
if __name__ == "__main__":
    app.run(port=5000,debug=True)



 # users_table.to_sql(name='users',schema='prod',con=my_db,if_exists='append')


