import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time

start_time=time.time()
    
cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-9bb70771f8.json")
def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)
Calculations_ref=db.collection(u'Calculations')

#function takes reference of users collection as input and returns tuple(kiranaOwnerName,phoneNo)
def ExtractorOfKiranaNamesAndCorrespondingPhones(reference):
    docs=reference.get()
    Set,Set2=set(),set()
    for doc in docs:
        mydict=doc.to_dict()
        if 'kiranaName' in mydict:
            if mydict['kiranaName']=='' or mydict['kiranaName']==' ':
                continue
            Set.add((mydict['kiranaName'],doc.id))
            Set2.add(mydict['kiranaName'])
    return Set,Set2

#function saves id and data-fields into array from reference node of the tree in firestore and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

ref=db.collection(u'users')
usersArray=Extractor(ref)

arrayOflastUsedTimeAndtimeStamp=[]

kiranaNamesSet2,kiranaNamesSet=ExtractorOfKiranaNamesAndCorrespondingPhones(ref)
for (a,b) in kiranaNamesSet2:
    Calculations_ref.document(a+'phone '+'Number').set(
        {
            'kiranaName':a,
            'phoneNo':b
        })#needs to set a and b

def timeConversion(timestamp):
    if len(str(timestamp))==13:
        timestamp/=1000
        s=time.ctime(timestamp)
        return s
    elif len(str(timestamp))==10:
        s=time.ctime(timestamp)
        return s
    return 'length of function need to be added'

ts,tss,current_owner,l,s=0,0,0,0,0
for doc in usersArray:
    if 'kiranaName' in doc[1]:
        if doc[1]['kiranaName']=='' or doc[1]['kiranaName']==' ':
            continue
        if 'timestamp' in doc[1]:
            ts=doc[1]['timestamp']
            s=timeConversion(ts)
        if 'lastUsed' in doc[1]:
            tss=doc[1]['lastUsed']
            l=timeConversion(tss)
        current_owner=doc[1]['kiranaName']
        Calculations_ref.document(current_owner+'timestamp').set({
            'lastUsed':l,
            'timestamp':s
            })
        
end_time=time.time()-start_time
print(end_time)

