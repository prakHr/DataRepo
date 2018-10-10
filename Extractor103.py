#Q. A particular barcodeNumber exists in how many users ?(ListOfList) Done from UnlistedBarcodeInventory,users
#Q.Active/Inactive?(Done) from users
#Q.Total Number of bills sold(Done)
#Q.Barcode Price for a particular Kirana(Done)
#In a Time Range
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
from datetime import timedelta

start_time=time.time()
cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

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
        array.append([doc.id,doc.to_dict()])
    return array

#Function has same functionality as Extractor function
def iterator(collection):
    array=[]
    for document in collection:
        array.append([document.id,document.to_dict()])
    return array

ref1,ref2,ref3,ref4,ref5=db.collection(u'barcode_inventory'),db.collection(u'barcode_repeats'),db.collection(u'speech_inventory'),db.collection(u'tags'),db.collection(u'unlisted_barcode_inventory')
BarcodesList,BarcodeRepeatsList,SpeechInventoryList,tagsList,unlistedBarcodesList=Extractor(ref1),Extractor(ref2),Extractor(ref3),Extractor(ref4),Extractor(ref5)
#print('len(BarcodesList),BarcodesList =>',len(BarcodesList),BarcodesList)
#print('len(BarcodeRepeatsList),BarcodesList=>',len(BarcodeRepeatsList),BarcodeRepeatsList)
#print('len(SpeechInventoryList),SpeechInventoryList=>',len(SpeechInventoryList),SpeechInventoryList)
#print('len(tagsList),tagsList=>',len(tagsList),tagsList)
#print('len(UnlistedBarcodesList),UnlistedBarcodesList=>'len(UnlistedBarcodesList),unlistedBarcodesList)

print('len(BarcodesList) =>',len(BarcodesList))
print('len(BarcodeRepeatsList)=>',len(BarcodeRepeatsList))
print('len(SpeechInventoryList)=>',len(SpeechInventoryList))
print('len(tagsList)=>',len(tagsList))
print('len(unlistedBarcodesList)=>',len(unlistedBarcodesList))

BarcodesPrices={}
BarcodePriceSum=0
BarcodeNumberSet=set()
for Barcodes in BarcodesList:
    barcodes,dic=Barcodes[0],Barcodes[1]
    if 'timeStamp' in dic:
        timestamp=dic['timeStamp']
    if 'barcodePrice' in dic:
        if dic['barcodePrice']>5000:dic['barcodePrice']=0#outliers exists so making values greater than 5000=>null
        BarcodesPrices[barcodes]=dic['barcodePrice']
        BarcodePriceSum+=dic['barcodePrice']
    BarcodeNumberSet.add(barcodes)

print('BarcodePriceSum=>',BarcodePriceSum)
usersPhoneNoSet=set()
for users in unlistedBarcodesList:
    dic=users[1]
    if 'user' in dic:
        usersPhoneNoSet.add(dic['user'])
print('usersPhoneNoSet=>',usersPhoneNoSet)
print('len(usersPhoneNoSet)=>',len(usersPhoneNoSet))
ans=[]
for PhoneNo in usersPhoneNoSet:
    for documents in unlistedBarcodesList:
        TotalBarcodesList,barcodeNumber,userNo=[],documents[1]['barcodeNumber'],documents[1]['user']
        if PhoneNo==userNo:#1 unique user uses how many barcodes from unlistedBarcodeInventory
            TotalBarcodesList.append(barcodeNumber)
    ans.append([len(TotalBarcodesList),TotalBarcodesList,PhoneNo])

#print('TotalBarcodesListOfList common in used by unlistedBarcodeInventory used by users',ans)

category0,category1,category2,category3=0,0,0,0
for SpeechInventory in SpeechInventoryList:
    dic=SpeechInventory[1]
    if 'category' in dic:
        if dic['category']=="0":category0+=1
        elif dic['category']=="1":category1+=1
        elif dic['category']=="2":category2+=1
        elif dic['category']=="3":category3+=1
print('Total items categorywise in category 0/1/2/3 =>',category0,category1,category2,category3)

ref6=db.collection(u'users')#documents=>collections(barcode_inventory,bills,customers_speech_inventory)
UserLists=Extractor(ref6)
lastUsedTime,timestamp,docsOfRef6=0,0,ref6.get()
ans,PhoneNumbers,barcodeName,barcodeSet,billsItem=[],set(),set(),set(),set()
for doc in docsOfRef6:
    dic=doc.to_dict()
    PhoneNumbers.add(doc.id)
    if 'lastUsed' in dic:lastUsedTime=dic['lastUsed']
    if 'timeStamp' in dic:timestamp=dic['timeStamp']
    if 'kiranaName' in dic:user=dic['kiranaName']
    if len(str(lastUsedTime))==13:
        lastUsedTime=lastUsedTime//1000

    print('User {} is last active on {} '.format(user,time.ctime(lastUsedTime)))

    a_collection,b_collection,c_collection,d_collection=db.collection(u'users').document(doc.id).collection(u'barcode_inventory').get(),db.collection(u'users').document(doc.id).collection(u'bills').get(),db.collection(u'users').document(doc.id).collection(u'customers').get(),db.collection(u'users').document(doc.id).collection(u'speech_inventory').get()
    arrayA,arrayB,arrayC,arrayD=iterator(a_collection),iterator(b_collection),iterator(c_collection),iterator(d_collection)
    print("User {} uses {} bills".format(user,len(arrayB)))
    for a in arrayA:
        barcode,dic=a[0],a[1]
        if 'barcodeName' in dic:
            barcodeName.add(dic['barcodeName'])
        barcodeSet.add(barcode)
    print('User {} uses {} barcodes'.format(user,len(barcodeSet)))
    price=0
    for b in barcodeSet:
        if b in BarcodesPrices:
            price+=BarcodesPrices[b]
    print('Total amount of barcode Price of User {} till {} is {}'.format(user,time.ctime(lastUsedTime),price))
    ans.append([user,barcodeSet,barcodeName])
    barcodeSet=set()
    #print(arrayA,arrayB,arrayC,arrayD)
    documentIds=[]
    for b in arrayB:
        documentIds.append(b[0])
    ID1=doc.id
    for ID in documentIds:
        soldCollection=db.collection(u'users').document(ID1).collection(u'bills').document(ID).collection(u'sold').get()
        arrayAA=iterator(soldCollection)
        for [a,b] in arrayAA:
            if 'billTableItemName' in b:
                billsItem.add(b['billTableItemName'])
    print('User {} uses billItems set {}'.format(user,billsItem))
    print('Total length of billItemSet => ',len(billsItem))

    billsItem=set()

print('ListOfList=>',ans)
elapsed_time_secs=time.time()-start_time
message="Execution took: %s secs" % timedelta(seconds=round(elapsed_time_secs))
print(message)        
