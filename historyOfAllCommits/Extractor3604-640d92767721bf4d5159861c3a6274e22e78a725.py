#Type
#Bytes
#Date and time
#Geographical point
#Reference
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

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

def SizeAccordingToType(types,size=0):#right now accounts for int,str,bool,list,map,null
    if type(types)==None:
        size=1
    if type(types)==int or type(types)==float:
        size=8
    elif type(types)==str:
        size=utf8len(types)
    elif type(types) in [True,False]:
        size=1
    elif type(types)==dict:
        for key,value in types.items():
            size+=SizeAccordingToType(value)
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
        pathSize=utf8len(p)+utf8len(doc)+additionalBytes#16+10+21
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
19355=>barcode_inventory
22905=>barcode_repeats
22=>customers
40335=>speech_inventory
237=>tags
14384=>unlisted_barcode_inventory
'''
billsByteSize,billsId=0,[]
for doc in db1.collection(BillsCollection).get():
    billsByteSize+=SizeAccordingToType(doc.to_dict())
    billsId.append(doc.id)

billsPathSize=[]
billsSubCollection=['sold']
for randomId in billsId:#/bills/1536820091567/sold/1538557548588
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
print('billsByteSize=>'+str(billsByteSize))
'''
TotalBillsPathSize=>39
billsByteSize=>87
'''
