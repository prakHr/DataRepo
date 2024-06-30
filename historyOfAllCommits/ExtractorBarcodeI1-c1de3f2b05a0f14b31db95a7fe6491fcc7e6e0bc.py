import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
from datetime import timedelta

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

#function takes the credentials(=>input) and gives reference address to database(=>db)
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db1=extractDatabase(cred1)
barcode_inventory_docs=db1.collection(u'barcode_inventory').get()
barcode_inventory_ref=db1.collection(u'barcode_inventory')

#for loop takes distinct barcodes using lower method of string in a set
barcodes_set,barcodes_array=set(),[]
first_two_digit_barcodes_array=[]

#for loop takes first 2 digits of barcodes in an array(not set to use for count),and a array of barcodes for similar purpose 
fourteenDigitsBarcodesSet,fourteenDigitsBarcodesArray,TwoDigits=set(),[],set()
for doc in barcode_inventory_docs:
    b=doc.id
    b=b.lower()
    if len(b)==14:
        fourteenDigitsBarcodesSet.add(b)
        fourteenDigitsBarcodesArray.append(b)

for b in fourteenDigitsBarcodesSet:
    if b[0]==b[1]:
        TwoDigits.add(b[:2])
     
CountArraySet,count=set(),0
for same in TwoDigits:
    count=0
    for b in fourteenDigitsBarcodesArray:
        if b[:2]==same:
            count+=1
            print(b)
    print('total 14 length=>',count)
    

