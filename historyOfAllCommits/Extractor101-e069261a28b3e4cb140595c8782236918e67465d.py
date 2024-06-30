import firebase_admin
#jo chiz sahi se nahi lekhi hai logon ne use database se hatao
#fields need to grow for document
#To stay under Cloud Firestore rate limits, limit operations to 500 writes/second for each collection.
from firebase_admin import *
from firebase_admin import firestore
import json

#Issues:-Extracts from realtime database
cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

def extractFromFirstProjectOfFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    #ref=db.reference('/dinosaurs/dino')
    #mydict=ref.get()
    delete_app(app)
    return db

#FileNotFoundError: [Errno 2] No such file or directory: 'python-78039-firebase-adminsdk-mthis-6f5f1c843.json'
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
           

#for a in SecondArray:print(a)
            
    #if doc.id==u'Jain_Departmental_Store':
      #  tempStorageDocs1=db.collection(u'Kiranas').document(u'Jain_Departmental_Store').collection(u'Barcodes').get()#contains data from collection
        #for c in tempStorage.get():print(c)#google.cloud.firestore_v1beta1.collection.CollectionReference
        #for docu in tempStorageDocs1:
          #  print(u'{}' . format(docu.id))
        #print(tempStorageDocs1)
        #tempStorage=doc.to_dict()
    #if doc.id==u'Navkar_Store':
      #  NtempStorage=doc.to_dict()#contains data from fields
    #print(u'{} => {}'.format(doc.id, doc.to_dict()))
num=0
def setDataCopiedFromExtractedAbove(ArrayToBeKeepedIn,SecondArray,cred):#some names are better not getting reverse-engineered such that control remains to us
    app=firebase_admin.initialize_app(cred,name='name2')
    firebase_admin.initialize_app(cred)
    db=firestore.client()
    i=0
    num=1
    for Second in SecondArray:
            #for values in Second:
              #  print(values)
        if i==len(ArrayToBeKeepedIn)-1:break
        print('Second=>',Second)
        
        print(len(Second))
            
        if len(Second)!=2 and Second==str('DocumentNumber')+str(' ')+str(num):
            num+=1
            i+=1
            continue#https://cloud.google.com/firestore/docs/manage-data/add-data
            
        db.collection(u'Kiranas').document(ArrayToBeKeepedIn[i]).collection(u'Barcodes').document(Second[0]).set(Second[1])#set overwrites the data
           
    delete_app(app)
    
setDataCopiedFromExtractedAbove(ArrayToBeKeepedIn,SecondArray,cred2)

#GOOGLE_APPLICATION_CREDENTIALS=
#from google.cloud import firestore
#db=firestore.Client("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
#print(db)

    

#def putIntoSecondProjectOfFirebase(cred2):
  #  firebase_admin.initialize_app(cred,{'databaseURL':'https://project2-a9304.firebaseio.com'})
    #ref=db.reference()
    
