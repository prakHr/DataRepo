import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")
'''
Name,Bills,Barcodes,SpeechItems,Date last used and kirana timestamp

chouhan kirana 24 4 1778 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Vinodji 1 1024 589 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
RadheShyam 5 4298 589 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Kamlesh Kirana 14 118 600 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Kanha Store 15 1149 742 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
SB Enterprises 15 659 543 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
sagar provision store 106 1294 2099 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Shubham Kira 36 1201 1830 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Chawla Store 9 434 1319 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Sample Bills 1 1 442 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Mahesh Kirana 7 279 595 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Variety Grain 43 4 1917 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
vardhman 47 365 1803 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Kumawat Store 16 610 718 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Nishant Store 2 1 0 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Apni Kirana 24 4429 589 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Saral Store 13 576 597 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
Jain Departmental 23 1628 581 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018
awesome 169 8 124 Sat Oct  6 08:19:51 2018 Sat Aug 25 11:42:05 2018

'''
def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)

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

def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

def lengthOfCollection(collection):
    length=0
    for docs in collection:
        length+=1
    return length

ref=db.collection(u'users')

UsersArray=Extractor(ref)
kiranaNamesSet=ExtractorOfKiranaNames(ref)
#print(kiranaNamesSet)
#{ 'vardhman', 'Saral Store', 'Mahesh Kirana', 'Variety Grain', 'Kumawat Store', 'Nishant Store', 'Jain Departmental', 'Sample Bills', 'Kanha Store', 'Kamlesh Kirana', 'RadheShyam', 'Shubham Kira', 'sagar provision store', 'Apni Kirana', 'Chawla Store', 'chouhan kirana', 'SB Enterprises', 'Vinodji', 'awesome'}

arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItemsAndlastUsedTimeAndtimeStamp=[]
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
            if 'lastUsed' in doc[1]:
                lastUsedTime=doc[1]['lastUsed']
                if len(str(lastUsedTime))==13:
                    lastUsedTime//=1000
                    l=time.ctime(lastUsedTime)

            if 'timestamp' in doc[1]:
                timeStamp=doc[1]['timestamp']
                if len(str(timeStamp))==13:
                    timeStamp//=1000
                    s=time.ctime(timeStamp)

            current_owner=doc[1]['kiranaName']
        if k==current_owner:
            totalBarcodes+=barcodes
            total+=bills
            totalSpeechInventory+=speechItems
            
    print(k,total,totalBarcodes,totalSpeechInventory,l,s)
    arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItemsAndlastUsedTimeAndtimeStamp.append([k,total,totalBarcodes,totalSpeechInventory,l,s])
    #find the length of bills collection for users
print(arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItemsAndlastUsedTimeAndtimeStamp)



