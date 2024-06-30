import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

def utf8len(s):
    return 1+len(s.encode('utf-8'))#returns 1+utf-8 in accordance to https://firebase.google.com/docs/firestore/storage-size

additionalBytes=16
'''
Sizes=[]
for b in ['barcode_inventory','barcode_repeats','bills','customers'
          'speech_inventory','tags',
          'unlisted_barcode_inventory','users'
          ]:
    Sizes.append(utf8len(b))
#print(Sizes)#[17, 15, 5, 25, 4, 26, 5] in utf-8 encoding
'''
cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db1=extractDatabase(cred1)

def ExtractRandomDocIdFromCollectionAndPutIntoArray(reference,database):
    docs,array=reference.get(),[]
    for doc in docs:
        array.append(doc.id)
    return array

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



'''
SizesOfRandomDocs=[]
#pathsSizes=something
for p in ['barcode_inventory','barcode_repeats','bills','customers'
          'speech_inventory','tags',
          'unlisted_barcode_inventory','users'
          ]:
    Array=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(p),db1)
    a=[]
    for aDash in Array:
        a.append(utf8len(aDash))
    #print(Array)
    SizesOfRandomDocs.append(a)
'''
#print(SizesOfRandomDocs)
pathsOfRandomDocs=[]
'''
for p in ['barcode_inventory','barcode_repeats','bills','customers'
          'speech_inventory','tags',
          'unlisted_barcode_inventory'
          ]:
    Array=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(p),db1)
    for doc in Array:
        pathSize=utf8len(p)+utf8len(doc)
        pathsOfRandomDocs.append(('/'+p+'/'+doc,pathSize))
print(pathsOfRandomDocs)'''

#how to find the path
#for p in ['bills',#sold Collection
  #  'users']:#barcode_inventory,bills,customers,speech_inventory

MainCollectionUsersFieldDataSize,SubCollectionUsersFieldDataSize=0,0
for doc in db1.collection('users').get():
    usersDict=doc.to_dict()
    MainCollectionUsersFieldDataSize+=SizeAccordingToType(usersDict)

usersCollection=u'users'
usersArray=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(usersCollection),db1)
usersCollections=[u'barcode_inventory'
                  ,u'bills'
                  ,u'customers'
                  ,u'speech_inventory']

#barcodeInventoryPaths,billsPaths,customersPath,speechInventoryPath=[],[],[],[]
usersPaths=[]

for randomId in usersArray:
 
    for collection in usersCollections:
        Array=[]
        for doc in db1.collection(usersCollection).document(randomId).collection(collection).get():
            SubCollectionUsersFieldDataSize+=SizeAccordingToType(doc.to_dict())
            Array.append(doc.id)
        print(Array)
        for randomId2 in Array:
            pathSize=utf8len(usersCollection)+utf8len(randomId)+utf8len(collection)+utf8len(randomId2)+additionalBytes
            usersPaths.append(('/'+usersCollection+'/'+randomId+'/'+collection+'/'+randomId2,pathSize))
  
#print(usersPaths)

TotalUserPathSize=0
for (_,size) in usersPaths:
    TotalUserPathSize+=size
print(TotalUserPathSize+MainCollectionUsersFieldDataSize+SubCollectionUsersFieldDataSize)#724451+3844+850199
print(MainCollectionUsersFieldDataSize)#3844
print(SubCollectionUsersFieldDataSize)#850199
    
    
