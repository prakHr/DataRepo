import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
from datetime import timedelta

cred1=credentials.Certificate("?????????.json")

def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)

#Function saves Id And data-fields Into array From reference node and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append(doc.id)
    return array

#takes reference of collection named Calculations and sets total number of things in mainCollection using Extractor method 
ref6=db.collection(u'Calculations')

ref6.document(u'BarcodesList').set({'BarcodesList':len(BarcodesList)})
ref6.document(u'BarcodeRepeatsList').set({'BarcodeRepeatsList':len(BarcodeRepeatsList)})
ref6.document(u'SpeechInventoryList').set({'SpeechInventoryList':len(SpeechInventoryList)})
ref6.document(u'tagsList').set({'tagsList':len(tagsList)})
ref6.document(u'unlistedBarcodesList').set({'unlistedBarcodesList':len(unlistedBarcodesList)})



