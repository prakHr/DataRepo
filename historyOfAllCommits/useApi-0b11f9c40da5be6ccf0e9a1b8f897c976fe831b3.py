from pprint import pprint
#part 1 comes from CatchingFire(codeName for Firebase)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("python-78039-firebase-adminsdk-mthis-6f5f1c843f.json")

#function takes ssl credentials =>filename.json
#using  firebase_admin module => converts between json and native data types in this case python dictionary 
def  extractFromFirebase(cred):
    firebase_admin.initialize_app(cred,{'databaseURL':'https://python-78039.firebaseio.com'})
    ref=db.reference()
    mydict=ref.get()
    return mydict

mydict=extractFromFirebase(cred)

#part 2 comes fom Monkey(codename for Mongodb)
import pymongo
from pymongo import MongoClient
#function takes mydict from firebase and puts it into the db
#db=>users,collection =>customers
def putIntoMongoDB(db,collection,mydict):
    collection.insert(mydict)

#function takes db=>users,admin,local from mongodb
def get_db():
    client=MongoClient("mongodb://localhost:27017")
    db=client["users"]
    return db

mydb=get_db()
mycollection=mydb["customers"]
putIntoMongoDB(mydb,mycollection,mydict)

#part 3 comes from here i.e. Avenger(codeName for Falcon)
cursor=mycollection.find({})#mycollection comes from part 2
myarray=[]
for content in cursor:
    myarray.append(content)
pprint(myarray)

import json
from bson import Binary,Code
from bson.json_util import dumps
class kiranacountClass:
    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200
        resp.body=dumps(myarray)

#ip address to use on ,give terminal command (gunicorn -b 0.0.0.0.5000 Avenger:app --reload)
#owner's server => http://127.0.0.1:5000/meter
#on other's laptop=> <myserverip>/meter(ex. 192.168.31.315000/meter)
import falcon
app=falcon.API()
app.add_route('/meter', kiranacountClass())



