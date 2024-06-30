import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
import sys
cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")
# database extraction using the credential
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db1=extractDatabase(cred1)
# variables to store the collection names
collection1,collection8=u'barcode_inventory',u'users'
ref1,ref8=db1.collection(collection1),db1.collection(collection8)
#titleCasing the barcodeName iff(if and only if) present in dictionary
def updateBarcodeNames(collection,reference,database):
    docs,array=reference.get(),[]
    for doc in docs:
        my_dict=doc.to_dict()
        if 'barcodeName' not in my_dict:
            continue
        else:
            barcodeName=my_dict['barcodeName'].title()
            database.collection(collection).document(doc.id).update(
                {
                    'barcodeName':barcodeName
                })
updateBarcodeNames(collection1,ref1,db1)
#input is main_collection and output is ids of random documents stored in a array
def storesDocumentIdIntoArrayAndSetsDatabase(collection,reference,database):
    docs,array=reference.get(),[]
    for doc in docs:
        array.append(doc.id)
        database.collection(collection).document(doc.id).set(doc.to_dict())
    return array
usersArray=storesDocumentIdIntoArrayAndSetsDatabase(collection8,ref8,db1)
#iterating through usersArray same process is repeated for barcode_inventory inside it
for randomId in usersArray:
    BarcodeInventoryCollection=db1.collection(collection8).document(randomId).collection(collection1)
    ref=BarcodeInventoryCollection.get()
    for doc in ref:
        my_dict=doc.to_dict()
        if 'barcodeName' not in my_dict:
            continue
        else:
            barcodeName=my_dict['barcodeName'].title()
            db1.collection(collection8).document(randomId).collection(collection1).document(doc.id).update(
                {
                    'barcodeName':barcodeName
                })
        
        
    
