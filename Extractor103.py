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

#Function has same functionality as Extractor function
def iterator(collection):
    array=[]
    for documents in collection:
        array.append([document.id,document.to_dict()])
    return array

ref1,ref2,ref3,ref4,ref5=db.collection(u'barcode_inventory'),db.collection(u'barcode_repeats'),db.collection(u'speech_inventory'),db.collection(u'tags'),db.collection(u'unlisted_barcode_inventory')
BarcodesList,BarcodeRepeatsList,SpeechInventoryList,tagsList,UnlistedBarcodesList=Extractor(ref1),Extractor(ref2),Extractor(ref3),Extractor(ref4),Extractor(ref5)
#print(BarcodesList,BarcodeRepeatsList,SpeechInventoryList,tagsList,UnlistedBarcodesList)
ref6=db.collection(u'users')#documents=>collections(barcode_inventory,bills,customers_speech_inventory)
UserLists=Extractor(ref6)
docsOfRef6=ref6.get()
=[],[],[],[]
for doc in docsOfRef6:
    a_collection,b_collection,c_collection,d_collection=db.collection(u'users').doc(doc.id).collection(u'barcode_inventory').get(),db.collection(u'users').doc(doc.id).collection(u'bills').get(),db.collection(u'users').doc(doc.id).collection(u'customers').get(),db.collection(u'users').doc(doc.id).collection(u'speech_inventory').get()
    arrayA,arrayB,arrayC,arrayD=iterator(a_collection),iterator(b_collection),iterator(c_collection),iterator(d_collection)
    #print(arrayA,arrayB,arrayC,arrayD)    
    
