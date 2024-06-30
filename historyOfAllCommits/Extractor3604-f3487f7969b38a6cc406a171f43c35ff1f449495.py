#Type(Not taken into account are)
#Bytes
#Geographical point
#Reference
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
from datetime import datetime
import datetime
import google.cloud

def MiBToBytes_Conversion(mib):
    One_mib_in_bytes=1049000.0
    converted_bytes=mib*One_mib_in_bytes
    return converted_bytes

def BytesToMiB_Conversion(mib_bytes):
    One_mib_in_bytes=1049000.0
    converted_mib=mib_bytes/One_mib_in_bytes
    return converted_mib

def utf8len(s):
    return 1+len(s.encode('utf-8'))
#remaining collection bills,

additionalBytes=16
BillsCollection='bills'

MainCList=['barcode_inventory','barcode_repeats',
          'customers',
          'speech_inventory','tags',
          'unlisted_barcode_inventory'
          ]
cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db1=extractDatabase(cred1)

def SizeAccordingToType(types,size=0):#right now accounts for int,str,bool,list,map,null,datetime,timestamp
    if type(types)==datetime.datetime:
        size=8
    elif type(types)==None:
        size=1
    if type(types)==int or type(types)==float:
        size=8
    elif type(types)==str:
        size=utf8len(types)
    elif type(types) in [True,False]:
        size=1
    elif type(types)==dict:
        for key,value in types.items():
            size+=(SizeAccordingToType(value)+SizeAccordingToType(key))
    elif type(types)==list:
        for t in types:
            size+=SizeAccordingToType(t)#recursive so need to set maximum recursive depth
    return size

def ExtractRandomDocIdFromCollectionAndPutIntoArray(reference,database):
    docs,array=reference.get(),[]
    for doc in docs:
        array.append(doc.id)
    return array

CollectionsPathSize,Collections_paths=[],[]
for p in MainCList:
    Array=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(p),db1)
    totalPathSize=0
    pathsOfRandomDocs=[]
    for doc in Array:
        pathSize=(utf8len(p)+utf8len(doc)+additionalBytes)
        pathsOfRandomDocs.append(('/'+p+'/'+doc,pathSize))
        totalPathSize+=pathSize
    CollectionsPathSize.append(totalPathSize)
    Collections_paths.append(pathsOfRandomDocs)

for (x,y) in zip(CollectionsPathSize,MainCList):
    print(str(x)+'=>'+str(y)) 
'''
16351=>barcode_inventory
22472=>barcode_repeats
47=>customers
16356=>speech_inventory
62=>tags
22272=>unlisted_barcode_inventory
'''
CollectionsFieldSize=[]
for p in MainCList:
    size=0
    for doc in db1.collection(p).get():
        size+=SizeAccordingToType(doc.to_dict())
    CollectionsFieldSize.append(size)
    
for (x,y) in zip(CollectionsFieldSize,MainCList):
    print(str(x)+'=>'+str(y))
'''
36400=>barcode_inventory
44375=>barcode_repeats
62=>customers
74612=>speech_inventory
304=>tags
29000=>unlisted_barcode_inventory
'''

billsByteSize,billsId=0,[]
for doc in db1.collection(BillsCollection).get():
    #print(SizeAccordingToType(doc.to_dict()))
    #print(doc.to_dict())
    billsByteSize+=SizeAccordingToType(doc.to_dict())
    billsId.append(doc.id)

billsPathSize=[]
billsSubCollection=['sold']
for randomId in billsId:
    for b in billsSubCollection:
        subCollection=db1.collection(BillsCollection).document(randomId).collection(b).get()
        for doc in subCollection:
            pathSize=utf8len(BillsCollection)+utf8len(randomId)+utf8len(b)+utf8len(doc.id)
            billsByteSize+=SizeAccordingToType(doc.to_dict())
        billsPathSize.append(('/'+BillsCollection+'/'+randomId+'/'+b+'/'+doc.id,pathSize))
        
TotalBillsPathSize=0
for (_,b) in billsPathSize:
    TotalBillsPathSize+=b
    
print('TotalBillsPathSize=>'+str(TotalBillsPathSize))
print('BytesToMiB_Conversion =>'+str(BytesToMiB_Conversion(TotalBillsPathSize)))

print('billsByteSize=>'+str(billsByteSize))
print('BytesToMiB_Conversion =>'+str(BytesToMiB_Conversion(billsByteSize)))

'''
TotalBillsPathSize=>39
BytesToMiB_Conversion =>3.717826501429933e-05
billsByteSize=>273
BytesToMiB_Conversion =>0.00026024785510009535
'''
