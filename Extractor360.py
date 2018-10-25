import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
import sys
#13 length and 14 length barcodes if it is substring then delete from 14 length collection
cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

# database extraction using the credential
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db1=extractDatabase(cred1)

collection1,collection8=u'barcode_inventory',u'users'
ref1,ref8=db1.collection(collection1),db1.collection(collection8)
'''
#update timestamp
def updateTimestamp(collection,reference):
    docs=reference.get()
    for doc in docs:
        RandomId,my_dict=doc.id,doc.to_dict()
        if 'timestamp' not in my_dict:
            field_updates={
                'timestamp':1514745000000,
            }
            db1.collection(collection).document(RandomId).update(field_updates)

updateTimestamp(collection1,ref1)
'''
#input is main_collection and output is ids of random documents stored in a array
def storesDocumentIdIntoArrayAndSetsDatabase(collection,reference,database):
    docs,array=reference.get(),[]
    for doc in docs:
        array.append(doc.id)
        database.collection(collection).document(doc.id).set(doc.to_dict())
    return array

usersArray=storesDocumentIdIntoArrayAndSetsDatabase(collection8,ref8,db1)

for randomId in usersArray:
    
    BarcodeInventoryCollection=db1.collection(collection8).document(randomId).collection(collection1)
    ref=BarcodeInventoryCollection.get()
    for doc in ref:
        ids=doc.id
        my_dict=doc.to_dict()
        if 'timestamp' not in my_dict:
            field_updates={
                'timestamp':1514745000000,
            }
            #BarcodeInventoryCollection..document(ids).update(field_updates)
            db1.collection(collection8).document(randomId).collection(collection1).document(ids).update(field_updates)

            
'''
#remove spaces from barcode_inventory
def removeSpaces(collection,reference):
    docs=reference.get()
    for doc in docs:
        ids,my_dict=doc.id,doc.to_dict()
        if 'barcodeNumber' not in my_dict:
            continue
        else:
            b=(my_dict['barcodeNumber'])
            if (' ' in b):
                my_dict['barcodeNumber']=b.strip(' ')#key-value in my_dict is changed
                b1=b.strip(' ')#b is striped of spaces
                reference.document(b1).set(my_dict)
                reference.document(ids).delete()#deletes the document
                
removeSpaces(collection1,ref1)

def totalLenInBarcodeInventory(reference,digit):
    barcodes=[]
    docs,total=reference.get(),0
    for doc in docs:
        my_dict=doc.to_dict()
        if 'barcodeNumber' not in my_dict:
            continue
        else:
            b=(my_dict['barcodeNumber'])
            if len(b)==digit:
                barcodes.append(b)
    return barcodes
len14,len13=totalLenInBarcodeInventory(ref1,14),totalLenInBarcodeInventory(ref1,13)
print(len(len14),len(len13))#8 259
#for b in len14:print(b)
#print('---------|------------|------')
#for b in len13:print(b)
 
def substringDelete(array1,array2):
    for len14 in array1:
        for len13 in array2:
            if len14[1:]==len13:
                db1.collection(collection1).document(len14).delete()
            if len14[:-1]==len13:
                db1.collection(collection1).document(len14).delete()
    
'''
