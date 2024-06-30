import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import json

#Issues:-set overwrites data
cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

def extractFromFirstProjectOfFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirstProjectOfFirebase(cred1)
users_ref=db.collection(u'Kiranas')
docs = users_ref.get()
ArrayToBeKeepedIn=[]
for doc in docs:
    ArrayToBeKeepedIn.append(doc.id)
    
#print(ArrayToBeKeepedIn)
SecondArray,num=[],0
for i in (ArrayToBeKeepedIn):
    num+=1
    #RandomName=str(str('u\'')+str(i+'\''))
    #print(RandomName)
    BarcodesCollections=db.collection(u'Kiranas').document(i).collection(u'Barcodes').get()
    for docu in BarcodesCollections:
        SecondArray.append([docu.id,docu.to_dict()])
    SecondArray.append(str('DocumentNumber')+str(' ')+str(num))
print('SecondArray=>',SecondArray)
print('Len of SecondArray=>',len(SecondArray))
           

num=0
def setDataCopiedFromExtractedAbove(ArrayToBeKeepedIn,SecondArray,cred):#some names are better not getting reverse-engineered such that control remains to us
    app=firebase_admin.initialize_app(cred,name='name2')
    firebase_admin.initialize_app(cred)
    db=firestore.client()
    i=0
    num=1
    for Second in SecondArray: 
        if i==len(ArrayToBeKeepedIn)-1:break
        print('Second=>',Second)
        
        print(len(Second))
            
        if len(Second)!=2 and Second==str('DocumentNumber')+str(' ')+str(num):
            num+=1
            i+=1
            continue#https://cloud.google.com/firestore/docs/manage-data/add-data
        if ArrayToBeKeepedIn[i] in ['Jain_Departmental_Store','Navkar_Store']:
            db.collection(u'Kiranas').document(ArrayToBeKeepedIn[i]).collection(u'Barcodes').document(Second[0]).set(Second[1])#set overwrites the data
           
    delete_app(app)
    
setDataCopiedFromExtractedAbove(ArrayToBeKeepedIn,SecondArray,cred2)




