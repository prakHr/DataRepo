import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import json

cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

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
        print('...Saving')
        array.append([doc.id,doc.to_dict()])
    return array

ref1=db.collection(u'barcode_inventory')
Barcodes=Extractor(ref1)
#print(Barcodes)
ref2=db.collection(u'barcode_repeats')
BarcodeRepeats=Extractor(ref2)
#print(BarcodeRepeats)
ref3=db.collection(u'speech_inventory')
SpeechInventory=Extractor(ref3)
ref4=db.collection(u'tags_inventory')

ref5=db.collection(u'unlisted_barcode_inventory')
UnlistedBarcodes=Extractor(ref5)

ref6=db.collection(u'users')#documents=>barcode_inventory,bills,customers_speech_inventory
