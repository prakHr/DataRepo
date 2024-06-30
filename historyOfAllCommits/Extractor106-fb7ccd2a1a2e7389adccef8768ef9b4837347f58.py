import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")
#timestamp and lastUsed apparently is calculated wrong or needed to fix

'''
PhoneNos,Name,Bills,Barcodes,SpeechItems,Date last used and kirana timestamp

+917742466334 chouhan kirana 24 4 1778 
+919166025226 Vinodji 1 1024 589 
+918290023496 RadheShyam 5 4298 589 
+919610789692 Kamlesh Kirana 14 118 600 
+919777688002 Kanha Store 15 1149 742 
+916378824851 SB Enterprises 15 659 543 
+916378867751 sagar provision store 106 1294 2099 
+919782216504 Shubham Kira 36 1201 1830 
+91901175999 Chawla Store 9 434 1319 
+918249403101 Sample Bills 1 1 442  
+916378731893 Mahesh Kirana 7 279 595 
+919167287597 Variety Grain 43 4 1917 
+919664087863 vardhman 47 365 1803 
+919777688001 Kumawat Store 16 610 718 
+919982204792 Nishant Store 2 1 0 
+919809258989 Apni Kirana 24 4429 589 
+919777688003 Saral Store 13 576 597 
+919011752453 Jain Departmental(has 2 phones) 23 1628 581(need to work here)
(+919829931177)
+919777688639 awesome 169 8 124 
'''
def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)
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
kiranaNamesSet=ExtractorOfKiranaNamesAndCorrespondingPhones(ref)
print(kiranaNamesSet)#20 names and corresponding phones
#{ 'vardhman', 'Saral Store', 'Mahesh Kirana', 'Variety Grain', 'Kumawat Store', 'Nishant Store', 'Jain Departmental', 'Sample Bills', 'Kanha Store', 'Kamlesh Kirana', 'RadheShyam', 'Shubham Kira', 'sagar provision store', 'Apni Kirana', 'Chawla Store', 'chouhan kirana', 'SB Enterprises', 'Vinodji', 'awesome'}
'''
arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItemsAndlastUsedTimeAndtimeStamp=[]
#Total No of bills of kirana in kiranaNamesSet
for k in kiranaNamesSet:

    total,totalBarcodes,totalSpeechInventory=0,0,0
    lastUsedArray,timeStampArray,l,s=[],[],0,0
    
    for doc in UsersArray:
        
        barcode_inventory_collection=db.collection(u'users').document(doc[0]).collection(u'barcode_inventory').get()
        bills_collection=db.collection(u'users').document(doc[0]).collection(u'bills').get()
        speech_inventory_collection=db.collection(u'users').document(doc[0]).collection(u'speech_inventory').get()
        
        barcodes=lengthOfCollection(barcode_inventory_collection)
        bills=lengthOfCollection(bills_collection)
        speechItems=lengthOfCollection(speech_inventory_collection)
        
        if 'kiranaName' in doc[1]:#mistake is either one of them is missing so not showing
            #sab timestamp or lastUsed ko ek array mein append karo or latest time show karo
            
            if 'lastUsed' in doc[1]:
                lastUsedTime=doc[1]['lastUsed']
                if len(str(lastUsedTime))==13:
                    lastUsedTime/=1000
                    l=time.ctime(lastUsedTime)
                    lastUsedArray.append(l[-13:-5])

            if 'timestamp' in doc[1]:
                timeStamp=doc[1]['timestamp']
                if len(str(timeStamp))==13:
                    timeStamp/=1000
                    s=time.ctime(timeStamp)#Sat Sep 29 15:02:11 2018(Day Month Date Time Year)
                    timeStampArray.append(s[-len(s):-5])#to get rid of year Sat Sep 29 15:02:11

            current_owner=doc[1]['kiranaName']
        if k==current_owner:
            totalBarcodes+=barcodes
            total+=bills
            totalSpeechInventory+=speechItems
            
    print(k,total,totalBarcodes,totalSpeechInventory,sorted(lastUsedArray),sorted(timeStampArray))
    arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItemsAndlastUsedTimeAndtimeStamp.append([k,total,totalBarcodes,totalSpeechInventory,sorted(lastUsedArray)[-1],sorted(timeStampArray)[-1]])
    
print(arrayOfNamesAndBillsAndSpeechItemsAndBarcodeItemsAndlastUsedTimeAndtimeStamp)
'''



