import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)
#function takes reference of users collection as input and returns tuple(kiranaOwnerName,phoneNo)
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

#function saves id and data-fields into array from reference node of the tree in firestore and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

ref=db.collection(u'users')

UsersArray=Extractor(ref)
kiranaNamesSet=ExtractorOfKiranaNames(ref)
#print(kiranaNamesSet)

arrayOflastUsedTimeAndtimeStamp=[]


ts,current_owner,l,s=0,0,0,0
for doc in UsersArray:
    if 'kiranaName' in doc[1]:

        if 'timestamp' in doc[1]:
            ts=doc[1]['timestamp']
            if len(str(ts))==13:
                ts/=1000
                s=time.ctime(ts)#Sat Sep 29 15:02:11 2018(Day Month Date Time Year)
                    #timeStampArray.append(s[-len(s):-5])#to get rid of year Sat Sep 29 15:02:11

        current_owner=doc[1]['kiranaName']

        print('=>',current_owner,s)
        #arrayOflastUsedTimeAndtimeStamp.append([k,lastUsed,timeStamp])

#print(arrayOflastUsedTimeAndtimeStamp)




