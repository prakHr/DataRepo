import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
#import time

cred=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db=extractDatabase(cred)

def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array
#(if possible put into mongodb) First after extracting or in this case printing
collection1,collection2=u'Kiranas',u'Mehboobs'

ref1,ref2=db.collection(collection1),db.collection(collection2)
kiranasList,mehboobsList=Extractor(ref1),Extractor(ref2)

#print('kiranasList=>',kiranasList)
#print('mehboobsList=>',mehboobsList)

myarray=kiranasList

import json
from bson import Binary,Code
from bson.json_util import dumps

class KiranasClass:
    def on_get(self,req,resp):
        resp.body=dumps(myarray)
        resp.status=falcon.HTTP_200#request maybe overridden as needed
        
import falcon
app=application=api=falcon.API()
app.add_route('/Kiranas',KiranasClass())
#myarray needs to be added here
myarray=mehboobsList

class MehboobsClass:
    def on_get(self,req,resp):
        resp.body=dumps(myarray)
        resp.status=falcon.HTTP_200
        
#go to http://127.0.0.1:5000/Mehboobs using gunicorn -b 0.0.0.0:5000 Extractor105:app --reload
app.add_route('/Mehboobs',MehboobsClass())
