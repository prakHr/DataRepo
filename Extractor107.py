import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")
def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)
#function takes reference of users collection as input and returns tuple(kiranaOwnerName,phoneNo)
def ExtractorOfKiranaNames(reference):
    docs=reference.get()
    Set=set()
    for doc in docs:
        mydict=doc.to_dict()
        if 'kiranaName' in mydict:
            if mydict['kiranaName']=='' or mydict['kiranaName']==' ':
                continue
            Set.add(mydict['kiranaName'])
    return Set

#function takes reference of users collection as input and returns tuple(kiranaOwnerName,phoneNo)
def ExtractorOfKiranaNamesAndCorrespondingPhones(reference):
    docs=reference.get()
    Set=set()

    for doc in docs:
        mydict=doc.to_dict()
        if 'kiranaName' in mydict:
            if mydict['kiranaName']=='' or mydict['kiranaName']==' ':
                continue
            Set.add((mydict['kiranaName'],doc.id))  
    return Set

#function saves id and data-fields into array from reference node of the tree in firestore and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array


ref=db.collection(u'users')

UsersArray=Extractor(ref)
kiranaNamesSet=ExtractorOfKiranaNames(ref)
#print(kiranaNamesSet)

def lengthOfCollection(collection):
    length=0
    for docs in collection:
        length+=1
    return length

arrayOflastUsedTimeAndtimeStamp=[]
print('---------KiranaName ,phoneNo---------------')
print('--------------------------------------')

kiranaNamesSet2=ExtractorOfKiranaNamesAndCorrespondingPhones(ref)
print(kiranaNamesSet2)

print('---------KiranaName ,timestamp ,lastUsed--------')
print('--------------------------------------')

ts,tss,current_owner,l,s=0,0,0,0,0
for doc in UsersArray:
    if 'kiranaName' in doc[1]:

        if 'timestamp' in doc[1]:
            ts=doc[1]['timestamp']
            if len(str(ts))==13:
                ts/=1000
                s=time.ctime(ts)
        
        if 'lastUsed' in doc[1]:
            tss=doc[1]['lastUsed']
            if len(str(tss))==13:
                tss/=1000
                l=time.ctime(tss)
        
        current_owner=doc[1]['kiranaName']

        print(current_owner,'=>',s,l)
        arrayOflastUsedTimeAndtimeStamp.append([current_owner,s,l])

#print(arrayOflastUsedTimeAndtimeStamp)
print('---------KiranaName ,barcodes ,bills ,speechItems--------')
print('-------------------------------------------')

arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItems=[]
#Total No of bills of kirana in kiranaNamesSet
for k in kiranaNamesSet:
    total,totalBarcodes,totalSpeechInventory=0,0,0
        
    for doc in UsersArray:
        
        barcode_inventory_collection=db.collection(u'users').document(doc[0]).collection(u'barcode_inventory').get()
        bills_collection=db.collection(u'users').document(doc[0]).collection(u'bills').get()
        speech_inventory_collection=db.collection(u'users').document(doc[0]).collection(u'speech_inventory').get()
        
        barcodes=lengthOfCollection(barcode_inventory_collection)
        bills=lengthOfCollection(bills_collection)
        speechItems=lengthOfCollection(speech_inventory_collection)
        
        if 'kiranaName' in doc[1]:
            current_owner=doc[1]['kiranaName']
        if k==current_owner:
            totalBarcodes+=barcodes
            total+=bills
            totalSpeechInventory+=speechItems
            
    print(k,total,totalBarcodes,totalSpeechInventory)
    #arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItems.append([k,total,totalBarcodes,totalSpeechInventory])
    
#ans1=print(arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItems)




