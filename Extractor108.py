import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

import time,math,datetime,random,six
from datetime import timedelta

_AUTO_ID_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

def _auto_id():
    return ''.join(random.choice(_AUTO_ID_CHARS) for _ in six.moves.xrange(20))

#project-python(is filled with munshik3 data) and project2(is fiilled with projectMehboob)
cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project2-a9304-firebase-adminsdk-g278y-70502f4ece.json")

#function takes the credentials(=>input) and gives reference address to database(=>db)
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)#instance of app is deleted to reuse again
    return db

db1=extractDatabase(cred1) 
db2=extractDatabase(cred2)

#function saves Id And data-fields Into array From reference node and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

mainCollectionCreated=u'FailedTransfers'

#function takes BarcodesCollection from projectMehboob as input and stores output in the form arrayOfArrays[[barcodeName1,barcodeNumber1,barcodePriceArray1,len(barcodePriceArray1)],[barcodeName2,barcodeNumber2,barcodePriceArray2,len(barcodePriceArray2)]...]
def extractionFromBarcodesCollection(b_collection,path):
    array,reasons=[],[]
    for random_doc in b_collection:
        flag1,flag2,flag3,flag4=False,False,False,False
        
        ID,my_dict=random_doc.id,random_doc.to_dict()
        
        if 'name' not in my_dict:flag1=True
        if 'barcode' not in my_dict:flag2=True
        if 'price' not in my_dict:flag3=True
        if 'modified' not in my_dict:flag4=True
            
        pathDash=path+'/'+ID+'/'
        
        if flag1==True:#here we need to check all conditions using if-statements
            nowTime=time.time();nowTime=math.ceil(nowTime*1000)
            ts=str(nowTime)
            reasons.append(['Name',pathDash,ts])
        if flag2==True:nowTime=time.time();nowTime=math.ceil(nowTime*1000);ts=str(nowTime);reasons.append(['Number',pathDash,ts])
        if flag3==True:nowTime=time.time();nowTime=math.ceil(nowTime*1000);ts=str(nowTime);reasons.append(['Price',pathDash,ts])
        if flag4==True:nowTime=time.time();nowTime=math.ceil(nowTime*1000);ts=str(nowTime);reasons.append(['Modified',pathDash,ts])

            
        if flag1==True and flag2==True and flag3==True and flag4==True:#gonna be 2<<3 cases i.e. 16 cases
            name,number,price,modified='','',[0],''
        elif flag1==True and flag2==True and flag3==False and flag4==True:name,number,price,modified='','',my_dict['price'],''
        elif flag1==True and flag2==False and flag3==True and flag4==True:name,number,price,modified='',my_dict['barcode'],[0],''
        elif flag1==False and flag2==True and flag3==True and flag4==True:name,number,price,modified=my_dict['name'],'',[0],''
        elif flag1==True and flag2==False and flag3==False and flag4==True:name,number,price,modified='',my_dict['barcode'],my_dict['price'],''
        elif flag1==False and flag2==False and flag3==True and flag4==True:name,number,price,modified=my_dict['name'],my_dict['barcode'],[0],''
        elif flag1==False and flag2==False and flag3==False and flag4==True:name,number,price,modified=my_dict['name'],my_dict['barcode'],my_dict['price'],''
        elif flag1==False and flag2==True and flag3==False and flag4==True:name,number,price,modified=my_dict['name'],'',my_dict['price'],''
        elif flag1==True and flag2==True and flag3==True and flag4==False:#gonna check all cases if we use if-statements instead of elif
            name,number,price,modified='','',[0],my_dict['modified']
        elif flag1==True and flag2==True and flag3==False and flag4==False:name,number,price,modified='','',my_dict['price'],my_dict['modified']
        elif flag1==True and flag2==False and flag3==True and flag4==False:name,number,price,modified='',my_dict['barcode'],[0],my_dict['modified']
        elif flag1==False and flag2==True and flag3==True and flag4==False:name,number,price,modified=my_dict['name'],'',[0],my_dict['modified']
        elif flag1==True and flag2==False and flag3==False and flag4==False:name,number,price,modified='',my_dict['barcode'],my_dict['price'],my_dict['modified']
        elif flag1==False and flag2==False and flag3==True and flag4==False:name,number,price,modified=my_dict['name'],my_dict['barcode'],[0],my_dict['modified']
        elif flag1==False and flag2==False and flag3==False and flag4==False:name,number,price,modified=my_dict['name'],my_dict['barcode'],my_dict['price'],my_dict['modified']
        elif flag1==False and flag2==True and flag3==False and flag4==False:name,number,price,modified=my_dict['name'],'',my_dict['price'],my_dict['modified']
            
        array.append([modified,name,number,price,len(price)])#array[0]=modified,array[1]=name,array[2]=number,array[3]=price,array[4]=len(price)
    return array,reasons
    
DocumentsArray=Extractor(db2.collection(u'Kiranas'))

#function takes database,a array,a name of main collection,id to transfer at and inventory as input and set documents according to array in database
def editCollection(database,array,main_collection,idToTransferAt,inventory):
    for doc in array:
        ids,my_dict=doc[0],doc[1]
        database.collection(main_collection).document(idToTransferAt).collection(inventory).document(ids).set(my_dict)
    
for doc in DocumentsArray:
    ids,my_dict=doc[0],doc[1]
    if 'transferTo' in my_dict:
        
        idToTransferAtdb1=my_dict['transferTo']
        if idToTransferAtdb1[0:3]!='+91':#if transferTo doesn't contain +91,then
            idToTransferAtdb1='+91'+my_dict['transferTo']
        
        BarcodesCollection=db2.collection(u'Kiranas').document(ids).collection(u'Barcodes').get()    
        SpeechItemsCollection=db2.collection(u'Kiranas').document(ids).collection(u'SpeechItems').get()

        BarcodePath='/Kiranas/'+ids+'/Barcodes'
        
        everythingArray,reasonsArrayForMissingVariable=extractionFromBarcodesCollection(BarcodesCollection,BarcodePath)

        reason2=str('missing barcode')
        for reasons in reasonsArrayForMissingVariable:
            pathVariable=reasons[1]
            timestampGeneratedFromCode=reasons[2]
            reason21=reason2+reasons[0]

            db2.collection(mainCollectionCreated).document(_auto_id()).set({'path':pathVariable,'reason':reason21,'timestamp':timestampGeneratedFromCode,'transferRequestFor':str(ids)})
        
        for i in range(len(everythingArray)):
            modifiedValue=everythingArray[i][0]
            if modifiedValue==False:
                priceArrayLengthIndb2=everythingArray[i][4]
                if priceArrayLengthIndb2==1:db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][2]).set({'barcodeName':everythingArray[i][1],'barcodeNumber':everythingArray[i][2],'barcodePrice':everythingArray[i][3][0]})
                elif priceArrayLengthIndb2==2:db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][2]).set({'barcodeName':everythingArray[i][1],'barcodeNumber':everythingArray[i][2],'barcodePrice':everythingArray[i][3][0],'barcodePrice2':everythingArray[i][3][1]})
                elif priceArrayLengthIndb2==3:db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][2]).set({'barcodeName':everythingArray[i][1],'barcodeNumber':everythingArray[i][2],'barcodePrice':everythingArray[i][3][0],'barcodePrice2':everythingArray[i][3][1],'barcodePricePkt':everythingArray[i][3][2]})
            elif modifiedValue==True:
                priceArrayLengthIndb2=everythingArray[i][4]
                if priceArrayLengthIndb2==1:db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][2]).update({'barcodeName':everythingArray[i][1],'barcodeNumber':everythingArray[i][2],'barcodePrice':everythingArray[i][3][0]})
                elif priceArrayLengthIndb2==2:db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][2]).update({'barcodeName':everythingArray[i][1],'barcodeNumber':everythingArray[i][2],'barcodePrice':everythingArray[i][3][0],'barcodePrice2':everythingArray[i][3][1]})
                elif priceArrayLengthIndb2==3:db1.collection(u'users').document(idToTransferAtdb1).collection(u'barcode_inventory').document(everythingArray[i][2]).update({'barcodeName':everythingArray[i][1],'barcodeNumber':everythingArray[i][2],'barcodePrice':everythingArray[i][3][0],'barcodePrice2':everythingArray[i][3][1],'barcodePricePkt':everythingArray[i][3][2]})
            
        speechArray=Extractor(SpeechItemsCollection)
        for docs in speechArray:
            c,d=docs[0],docs[1]
            db1.collection(u'users').document(idToTransferAtdb1).collection(u'speech_inventory').document(c).set(d)
            
    elif 'transferTo' not in my_dict:
        nowTime=time.time();nowTime=math.ceil(nowTime*1000);ts=str(nowTime)
        reason1=str('transferTo field not found')
        pathVariable='/Kiranas/'+ids
        db2.collection(mainCollectionCreated).document(_auto_id()).set({'path':pathVariable,'reason':reason1,'timestamp':ts,'transferRequestFor':str(ids)})#autogenerateID(need to print path to find its type in python)




