import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time

cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)#instance of app is deleted to reuse again
    return db

db= extractDatabase(cred1)
db1=extractDatabase(cred2)

collection1,collection2,collection3,collection4,collection5,collection6,collection7,collection8=u'barcode_inventory',u'barcode_repeats',u'bills',u'customers',u'speech_inventory',u'tags',u'unlisted_barcode_inventory',u'users'
usersCollection1,usersCollection2,usersCollection3,usersCollection4=collection1,collection3,collection4,collection5
billsCollection1=u'sold'
collectionsOfUsersCollection3=[u'payment',u'paid',u'udhaar']
collectionOfUsersCollection2=u'sold'
collectionsOfUsersCollection4=u'speechInventoryPrice'
collectionOfSpeechInventoryPrice=u'records'
collectionOfRecords=[u'price',u'stock']
ref1,ref2,ref3,ref4,ref5,ref6,ref7,ref8=db.collection(collection1),db.collection(collection2),db.collection(collection3),db.collection(collection4),db.collection(collection5),db.collection(collection6),db.collection(collection7),db.collection(collection8)

def SimplePutIntoCollection(collection,reference,database):
    docs=reference.get()
    for doc in docs:
        database.collection(collection).document(doc.id).set(doc.to_dict())

def storesDocumentIdIntoArrayAndSetsDatabase(collection,reference,database):
    docs,array=reference.get(),[]
    for doc in docs:
        array.append(doc.id)
        database.collection(collection).document(doc.id).set(doc.to_dict())
    return array
#collection3 is remaining
'''
#SimplePutIntoCollection(collection1,ref1,db1)
#SimplePutIntoCollection(collection2,ref1,db1)
#SimplePutIntoCollection(collection4,ref1,db1)
#SimplePutIntoCollection(collection5,ref1,db1)
#SimplePutIntoCollection(collection6,ref1,db1)
#SimplePutIntoCollection(collection7,ref1,db1)
'''
billsArray=storesDocumentIdIntoArrayAndSetsDatabase(collection3,ref3,db1)
for randomID in billsArray:
    DocumentsOfBillsCollection=db.collection(collection3).document(randomID).collection(billsCollection1).get()
    for doc in DocumentsOfBillsCollection:
        db1.collection(collection3).document(randomID).collection(billsCollection1).document(doc.id).set(doc.to_dict())
    
usersArray=storesDocumentIdIntoArrayAndSetsDatabase(collection8,ref8,db1)

for randomID in usersArray:
    DocumentsOfBarcodeInventoryCollection=db.collection(collection8).document(randomID).collection(usersCollection1).get()
    for doc in DocumentsOfBarcodeInventoryCollection:
        db1.collection(collection8).document(randomID).collection(usersCollection1).document(doc.id).set(doc.to_dict())
    
    DocumentsOfBillsCollection=db.collection(collection8).document(randomID).collection(usersCollection2).get()
    for doc in DocumentsOfBillsCollection:
        db1.collection(collection8).document(randomID).collection(usersCollection2).document(doc.id).set(doc.to_dict())
        
        DocumentsOfSoldCollection=db.collection(collection8).document(randomID).collection(usersCollection2).document(doc.id).collection(collectionOfUsersCollection2).get()
        for docu11 in DocumentsOfSoldCollection:
            db.collection(collection8).document(randomID).collection(usersCollection2).document(doc.id).collection(collectionOfUsersCollection2).document(docu11.id).set(docu11.to_dict())

    customers_ref=db.collection(collection8).document(randomID).collection(usersCollection3)
    DocumentsOfCustomersCollection=customers_ref.get()
    for doc in DocumentsOfCustomersCollection:
        db1.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).set(doc.to_dict())
        
        DocumentsOfPaymentCollection=db.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).collection(collectionsOfUsersCollection3[0]).get()
        for docu in DocumentsOfPaymentCollection:
            db1.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).collection(collectionsOfUsersCollection3[0]).document(docu.id).set(docu.to_dict())

        DocumentsOfPaymentCollection1=db.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).collection(collectionsOfUsersCollection3[1]).get()
        for docu in DocumentsOfPaymentCollection1:
            db1.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).collection(collectionsOfUsersCollection3[1]).document(docu.id).set(docu.to_dict())

        DocumentsOfPaymentCollection2=db.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).collection(collectionsOfUsersCollection3[2]).get()
        for docu in DocumentsOfPaymentCollection2:
            db1.collection(collection8).document(randomID).collection(usersCollection3).document(doc.id).collection(collectionsOfUsersCollection3[2]).document(docu.id).set(docu.to_dict())

        

    DocumentsOfSpeechInventoryCollection=db.collection(collection8).document(randomID).collection(usersCollection4).get()
    for doc in DocumentsOfSpeechInventoryCollection:
        db1.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).set(doc.to_dict())
        
        speechInventoryPriceDocuments=db.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).get()
        
        for docuDash in speechInventoryPriceDocuments:
            db1.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).set(docuDash.to_dict())
            RecordsDocuments=db.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).get()
            for docuDashDash in RecordsDocuments:
                db1.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).set(docuDashDash.to_dict())
                PriceDocuments=db.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).collection(collectionOfRecords[0]).get()
                for docuDashDashDash in PriceDocuments:
                    db1.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).collection(collectionOfRecords[0]).document(docuDashDashDash.id).set(docuDashDashDash.to_dict())
                    
                StockDocuments=db.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).collection(collectionOfRecords[1]).get()
                for docuDashDashDash2 in StockDocuments:
                    db1.collection(collection8).document(randomID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).collection(collectionOfRecords[0]).document(docuDashDashDash2.id).set(docuDashDashDash2.to_dict())
                
                
        
    
