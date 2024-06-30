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
    return 1+len(s.encode('utf-8'))#returns 1+utf-8 in accordance to https://firebase.google.com/docs/firestore/storage-size

additionalBytes=16
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

def EmptyArray(array):
    if array==[]:
        return 1
    else:return 0
    
#/users/+919777688639/speech_inventory/DQqctA2wSMslh6v0g0ZK/speechInventoryPrice/1538996042795/records/stock
usersCollectionRandomDocArray=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(u'users'),db1)
Counter,constantPathSize=0,123
usersPathTotal=[]
for id1 in usersCollectionRandomDocArray:
    usersCollectionRandomDocArray2=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(u'users').document(id1).collection(u'speech_inventory'),db1)
    if EmptyArray(usersCollectionRandomDocArray2):continue
    for id2 in usersCollectionRandomDocArray2:
        usersCollectionRandomDocArray3=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(u'users').document(id1).collection(u'speech_inventory').document(id2).collection(u'speechInventoryPrice'),db1)
        if EmptyArray(usersCollectionRandomDocArray3):continue
        for id3 in usersCollectionRandomDocArray3:
            usersCollectionRandomDocArray4=ExtractRandomDocIdFromCollectionAndPutIntoArray(db1.collection(u'users').document(id1).collection(u'speech_inventory').document(id2).collection(u'speechInventoryPrice').document(id3).collection(u'records'),db1)
            if EmptyArray(usersCollectionRandomDocArray4):continue
            for id4 in usersCollectionRandomDocArray4:
                #pathSize=utf8len(u'users')+utf8len(id1)+utf8len('speech_inventory')+utf8len(id2)+utf8len('speechInventoryPrice')+utf8len(id3)+utf8len(u'records')+utf8len(id4)+additionalBytes
                pathURL='/'+'users'+'/'+str(id1)+'/'+'speech_inventory'+'/'+str(id2)+'/'+'speechInventoryPrice'+'/'+str(id3)+'/'+'records'+'/'+str(id4)
                usersPathTotal.append(pathURL)
                Counter+=1
                #print((pathURL))
                
print(len(usersPathTotal))
print(Counter*constantPathSize)


