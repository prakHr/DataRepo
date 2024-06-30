import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import json

cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

def extractFromFirstProjectOfFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirstProjectOfFirebase(cred1)
db1=extractFromFirstProjectOfFirebase(cred2)
users_ref=db.collection(u'Kiranas')
docs = users_ref.get()
ArrayToBeKeepedIn,flags=[],[]
for doc in docs:
    ArrayToBeKeepedIn.append(doc.id)
    dictionaryOfDoc=doc.to_dict()
    flags.append(dictionaryOfDoc['check'])
#print(ArrayToBeKeepedIn)
#print(flags)
flagLen,num=0,0
for i in (ArrayToBeKeepedIn):
    num+=1
    if flags[flagLen]=='false' or flags[flagLen]=='False' or flags[flagLen]==0 or flags[flagLen]=='0':
        flagLen+=1
        continue
    flagLen+=1
    BarcodesCollections=db.collection(u'Kiranas').document(i).collection(u'Barcodes').get()
    for docu in BarcodesCollections:
        db1.collection(u'Kiranas').document(i).collection(u'Barcodes').document(docu.id).set(docu.to_dict())

           




