from pprint import pprint
'''#part 1 comes from CatchingFire(codeName for Firebase)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("python-78039-firebase-adminsdk-mthis-6f5f1c843f.json")

def  extractFromFirebase(cred):
    firebase_admin.initialize_app(cred,{'databaseURL':'https://python-78039.firebaseio.com'})
    ref=db.reference()
    mydict=ref.get()
    return mydict

mydict=extractFromFirebase(cred)

#part 2 comes fom Monkey(codename for Mongodb)
import pymongo
from pymongo import MongoClient
def putIntoMongoDB(db,collection,mydict):
    collection.insert(mydict)

def get_db():
    client=MongoClient("mongodb://localhost:27017")
    db=client["users"]
    return db

mydb=get_db()
mycollection=mydb["customers"]
putIntoMongoDB(mydb,mycollection,mydict)
'''
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
        
import falcon#http://127.0.0.1:5000/meter
app=falcon.API()
#kiranacount = myarray
#print("kiranacount=>",kiranacount)
#read from mongoDb in the above line
app.add_route('/meter', kiranacountClass())


#kiranaOnboard = 
#read from mongoDb in the above line
#api.add_route('/metric/kiranaonboard', kiranaco
