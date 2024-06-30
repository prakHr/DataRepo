import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

import time,math,datetime,random,six

_AUTO_ID_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

def _auto_id():
    return ''.join(random.choice(_AUTO_ID_CHARS) for _ in six.moves.xrange(20))

#project-python(is filled with munshik3 data) and project2(is fiilled with projectMehboob) is empty right now
cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project2-a9304-firebase-adminsdk-g278y-70502f4ece.json")


def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db1=extractDatabase(cred1)#need to add here
db2=extractDatabase(cred2)

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

#function takes transferTo variable and outputs into array
def IdAndPhoneNoOfBarcodesModifiedAndTimestampFromBD(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        d=doc.to_dict()
        phones=str(d['transferTo'])
        array.append(phones)
    return array

def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

def extractionFromBarcodesCollection(b_collection):
    array=[]
    for random_doc in b_collection:
        ID,my_dict=random_doc.id,random_doc.to_dict()
        if 'name' not in my_dict:
            print('barcodeName not found in id of kiranas collection: '+str(ID))
            if 'barcode' not in my_dict:
                print('barcodeNumber not found in id of kiranas collection: '+str(ID))
                if 'price' not in my_dict:
                    print('barcodePrice not found in id of kiranas collection: '+str(ID))
            continue
        name,number,price=my_dict['name'],my_dict['barcode'],my_dict['price']
        array.append([name,number,price,len(price)])#array[0]=name,array[1]=number,array[2]=price,array[3]=len(price)
        #print(array)
    return array
    
DocumentsArray=Extractor(db2.collection(u'Kiranas'))

for doc in DocumentsArray:
    ids,my_dict=doc[0],doc[1]
    if 'transferTo' in my_dict:
        idToTransferAtdb1=my_dict['transferTo']
        BarcodesCollectionRef=db2.collection(u'Kiranas').document(ids).collection(u'Barcodes')
        SpeechItemsCollectionRef=db2.collection(u'Kiranas').document(ids).collection(u'SpeechItems')
        
        BarcodesCollection=BarcodesCollectionRef.get()    
        SpeechItemsCollection=SpeechItemsCollectionRef.get()
        '''
        everythingArray=extractionFromBarcodesCollection(BarcodesCollection)#[[['bshs', '25461845', [88], 1], ['qwerty', '123', [133, 24, 212], 3]], [], []]
        speechArray=Extractor(SpeechItemsCollectionRef) 
        for i in range(len(everythingArray)):
            priceArrayLengthIndb2=everythingArray[i][3]
            if priceArrayLengthIndb2==1:
                db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][1]).set({'barcodeName':everythingArray[i][0],'barcodeNumber':everythingArray[i][1],'barcodePrice':everythingArray[i][2]})
            elif priceArrayLengthIndb2==2:
                db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][1]).set({'barcodeName':everythingArray[i][0],'barcodeNumber':everythingArray[i][1],'barcodePrice':everythingArray[i][2][0],'barcodePrice2':everythingArray[i][2][1]})
            elif priceArrayLengthIndb2==3:
                db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][1]).set({'barcodeName':everythingArray[i][0],'barcodeNumber':everythingArray[i][1],'barcodePrice':everythingArray[i][2][0],'barcodePrice2':everythingArray[i][2][1],'barcodePricePkt':everythingArray[i][2][2]})
        '''
        barcodeArray=iterator(BarcodesCollection)
        for a,b in barcodeArray:
            db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(a).set(b)
        speechArray=iterator(SpeechItemsCollection)
        for c,d in speechArray:
            db1.collection(u'users').document(idToTransferAtdb1).collection(u'speech_inventory').document(c).set(d)
            
    elif 'transferTo' not in my_dict:
        #path='\\Kiranas\\jain' OR '\\Kiranas'+'jain'
        #now=time.ctime() OR t=datetime.datetime.strptime(time.ctime(),"%a %b %d %H:%M:%S %Y");ts=str(t.timestamp()) OR t=math.floor(time.time())=>10 length timestamp after rounding off(to convert into 13 length timestamp time.time()=1539596964.1039205)
        nowTime=time.time();nowTime=math.ceil(nowTime*1000)
        ts=str(nowTime)
        reason=str('transferTo field not found')
        pathVariable='/Kiranas/'+ids
        db1.collection(u'FailedTransfers').document(_auto_id()).set({'path':pathVariable,'reason':reason,'timestamp':ts,'transferRequestFor':str(ids)})#autogenerateID(need to print path to find its type in python)
        #need to convert timestamp to 13 length string,
    #elif: there is gonna be a big fatty error due to either incomplete Transfer 

'''
#mainCollectionsInDatabase1=[u'barcode_inventory',u'barcode_repeats',u'bills',u'customers',u'speech_inventory',u'tags',u'unlisted_barcode_inventory',u'users']
#billsCollectionInDatabase1=u'sold'
#usersCollectionsInDatabase1=[u'barcode_inventory',u'bills',u'customers',u'speech_inventory']
#customersCollectionInDatabase1=[u'payment',u'paid',u'udhaar']

#mainCollectionsInDatabase2=[u'BD',u'GlobalData',u'Kiranas',u'Mehboobs']
#globalDataCollectionInDatabase2=[u'Barcodes',u'SpeechItems']
#kiranasDataCollectionInDatabase2=[u'Barcodes',u'SpeechItems']
'''


'''
DocumentsArray=Extractor(db2.collection(u'Kiranas'))

for doc in DocumentsArray:
    ids,my_dict=doc[0],doc[1]
    value=0
    if 'transferTo' in my_dict:
        value=my_dict['transferTo']
        if value==True:#In projectMehboob barcode=>barcodeNumber,name=>barcodeName
            BarcodesCollectionREF=db2.collection(u'Kiranas').document(ids).collection(u'Barcodes')
            SpeechItemsCollectionREF=db2.collection(u'Kiranas').document(ids).collection(u'SpeechItems')
            SpeechItemsCollection=SpeechItemsCollectionREF.get()
            ModifiedAndPhones=IdAndPhoneNoOfBarcodesModifiedAndTimestampFromBD(BarcodesCollectionREF)
            for b,m,phones,price,ts in ModifiedAndPhones:
                
                if m==False:#set
                    p=len(price)
                    if p==1:db1.collection(u'users').document(phones).collection(u'barcode_inventory').document(b).set({'barcodeNumber':b,'barcodePrice':price[0],'timestamp':ts})
                    elif p==2:db1.collection(u'users').document(phones).collection(u'barcode_inventory').document(b).set({'barcodeNumber':b,'barcodePrice':price[0],'barcodePrice2':price[1],'timestamp':ts})
                    elif p==3:db1.collection(u'users').document(phones).collection(u'barcode_inventory').document(b).set({'barcodeNumber':b,'barcodePrice':price[0],'barcodePrice2':price[1],'barcodePricePkt':price[2],'timestamp':ts})
                elif m==True:#update
                    p=len(price)
                    if p==1:db1.collection(u'users').document(phones).collection(u'barcode_inventory').document(b).update({'barcodeNumber':b,'barcodePrice':price[0],'timestamp':ts})
                    elif p==2:db1.collection(u'users').document(phones).collection(u'barcode_inventory').document(b).update({'barcodeNumber':b,'barcodePrice':price[0],'barcodePrice2':price[1],'timestamp':ts})
                    elif p==3:db1.collection(u'users').document(phones).collection(u'barcode_inventory').document(b).update({'barcodeNumber':b,'barcodePrice':price[0],'barcodePrice2':price[1],'barcodePricePkt':price[2],'timestamp':ts})
                #TransferSpeechItems as it is from this point(i.e. assumption that structure is gonna be same in project-munshik3) that is speech_inventory =>has random documents(doc.id,doc.to_dict())
                for doc in SpeechItemsCollection:
                    db1.collection(u'users').document(phones).collection(u'speech_inventory').document(doc.id).set(doc.to_dict())
'''
