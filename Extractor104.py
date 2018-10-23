import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
import sys
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")
# database extraction using the credential
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db1=extractDatabase(cred2)
# variables to store the collection names
collection1,collection2,collection3,collection4,collection5,collection6,collection7,collection8,collection9=u'barcode_inventory',u'barcode_repeats',u'bills',u'customers',u'speech_inventory',u'tags',u'unlisted_barcode_inventory',u'users',u'barcode_repeats'
usersCollection1,usersCollection2,usersCollection3,usersCollection4=collection1,collection3,collection4,collection5
billsCollection1=u'sold'
collectionsOfUsersCollection3=[u'payment',u'paid',u'udhaar']
collectionOfUsersCollection2=u'sold'
collectionsOfUsersCollection4=u'speechInventoryPrice'
collectionOfSpeechInventoryPrice=u'records'
collectionOfRecords=[u'price',u'stock']
ref1,ref2,ref3,ref4,ref5,ref6,ref7,ref8,ref9=db1.collection(collection1),db1.collection(collection2),db1.collection(collection3),db1.collection(collection4),db1.collection(collection5),db1.collection(collection6),db1.collection(collection7),db1.collection(collection8),db1.collection(collection9)
# variables to decide what all collections we have to transfer
transferBarcode=False
transferSpeech=True
transferBill=False
transferCustomer=False
# from ID and to ID - retrieved from the command
# first argument is the from ID and the second argument is the to ID
toID = sys.argv[2]#run it as python scriptName.py arg1 arg2,where argv[0]=scriptName,argv[1]=arg1,argv[2]=arg2
fromID = sys.argv[1]
# transfer the barcode collection data if transferBarcode value is true
if(transferBarcode):
    DocumentsOfBarcodeInventoryCollection=db1.collection(collection8).document(fromID).collection(usersCollection1).get()
# DocumentsOfBarcodeInventoryCollection=db1.collection(usersCollection1).get()
    for doc in DocumentsOfBarcodeInventoryCollection:
        db1.collection(collection8).document(toID).collection(usersCollection1).document(doc.id).set(doc.to_dict())
# transfer the bill collection data if transferBill value is true
if(transferBill):
    DocumentsOfBillsCollection=db1.collection(collection8).document(fromID).collection(usersCollection2).get()
    for doc in DocumentsOfBillsCollection:
        db1.collection(collection8).document(toID).collection(usersCollection2).document(doc.id).set(doc.to_dict())
        DocumentsOfSoldCollection=db1.collection(collection8).document(fromID).collection(usersCollection2).document(doc.id).collection(collectionOfUsersCollection2)
        for docu11 in DocumentsOfSoldCollection:
            db1.collection(collection8).document(toID).collection(usersCollection2).document(doc.id).collection(collectionOfUsersCollection2).document(docu11.id).set(docu11.to_dict())
# transfer the customer collection data if transferCustomer value is true
if(transferCustomer):
    customers_ref=db1.collection(collection8).document(fromID).collection(usersCollection3)
    DocumentsOfCustomersCollection=customers_ref.get()
    for doc in DocumentsOfCustomersCollection:
        db1.collection(collection8).document(toID).collection(usersCollection3).document(doc.id).set(doc.to_dict())
        for c in collectionsOfUsersCollection3:
            DocumentsOfPaymentCollection=db1.collection(collection8).document(fromID).collection(usersCollection3).document(doc.id).collection(c).get()
            for docu in DocumentsOfPaymentCollection:
                db1.collection(collection8).document(toID).collection(usersCollection3).document(doc.id).collection(c).document(docu.id).set(docu.to_dict())
# transfer the speech collection data if transferSpeech value is true
if(transferSpeech):
    DocumentsOfSpeechInventoryCollection=db1.collection(collection8).document(fromID).collection(usersCollection4).get()
    for doc in DocumentsOfSpeechInventoryCollection:
        db1.collection(collection8).document(toID).collection(usersCollection4).document(doc.id).set(doc.to_dict())
        speechInventoryPriceDocuments=db1.collection(collection8).document(fromID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).get()
        for docuDash in speechInventoryPriceDocuments:
            db1.collection(collection8).document(toID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).set(docuDash.to_dict())
            RecordsDocuments=db1.collection(collection8).document(fromID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).get()
            for docuDashDash in RecordsDocuments:
                db1.collection(collection8).document(toID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).set(docuDashDash.to_dict())
                for c in collectionOfRecords:
                    PriceDocuments=db1.collection(collection8).document(fromID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).collection(c).get()
                    for docuDashDashDash in PriceDocuments:
                        db1.collection(collection8).document(toID).collection(usersCollection4).document(doc.id).collection(collectionsOfUsersCollection4).document(docuDash.id).collection(collectionOfSpeechInventoryPrice).document(docuDashDash.id).collection(c).document(docuDashDashDash.id).set(docuDashDashDash.to_dict())


