import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time

start_time=time.time()

cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-9bb70771f8.json")
def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)
Calculations_ref=db.collection(u'Calculations')

#function takes reference of users collection as input and returns tuple(kiranaOwnerName,phoneNo)
def ExtractorOfKiranaNamesAndCorrespondingPhones(reference):
    docs=reference.get()
    Set2=set()
    for doc in docs:
        mydict=doc.to_dict()
        if 'kiranaName' in mydict:
            if mydict['kiranaName']=='' or mydict['kiranaName']==' ':
                continue
            Set2.add(mydict['kiranaName'])
    return Set2

#function saves id and data-fields into array from reference node of the tree in firestore and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

def lengthOfCollection(reference):
    docs=reference.get()
    length=0
    for doc in docs:
        length+=1
    return length

ref=db.collection(u'users')
usersArray=Extractor(ref)

kiranaNamesSet=ExtractorOfKiranaNamesAndCorrespondingPhones(ref)

arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItems=[]

for k in kiranaNamesSet:
    total,totalBarcodes,totalSpeechInventory=0,0,0
    for doc in usersArray:
        barcode_inventory_collection=db.collection(u'users').document(doc[0]).collection(u'barcode_inventory')
        bills_collection=db.collection(u'users').document(doc[0]).collection(u'bills')
        speech_inventory_collection=db.collection(u'users').document(doc[0]).collection(u'speech_inventory')

        barcodes=lengthOfCollection(barcode_inventory_collection)
        bills=lengthOfCollection(bills_collection)
        speechItems=lengthOfCollection(speech_inventory_collection)

        if 'kiranaName' in doc[1]:
            current_owner=doc[1]['kiranaName']
        if k==current_owner:
            totalBarcodes+=barcodes
            total+=bills
            totalSpeechInventory+=speechItems
    Calculations_ref.document(k).set({
        'totalBills':total,
        'totalBarcodes':totalBarcodes,
        'totalSpeechInventory':totalSpeechInventory
        })
    
end_time=time.time()-start_time
print(end_time)
