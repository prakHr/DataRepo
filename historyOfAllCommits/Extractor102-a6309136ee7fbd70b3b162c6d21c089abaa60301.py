import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import json

#Credentials of project1 and project2 is required
cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

#function takes the credentials(=>input) and gives reference address to database(=>db)
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)#instance of app is deleted to reuse again
    return db

db= extractDatabase(cred1)
db1=extractDatabase(cred2)
users_ref=db.collection(u'Kiranas')#takes the collection
docs=users_ref.get()
ArrayToBeKeepedIn=[]#Array takes the random name of documents
for doc in docs:
    db1.collection(u'Kiranas').document(doc.id).set(doc.to_dict())
    ArrayToBeKeepedIn.append(doc.id)
#print(ArrayToBeKeepedIn)
SecondArray,num=[],0
for i in ArrayToBeKeepedIn:#iterates through the array
    #if i =='Navkar_store':#Since Navkar_store has speechCollection
    num+=1
    SpeechCollections=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').get()#takes all the documents(Id and data) from SpeechItems collection
    
    for docu in SpeechCollections:
        #print(u'{} => {}'.format(docu.id, docu.to_dict()))
        db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).set(docu.to_dict())#reverse engineering to set all the data in SpeechItems according to document Id
        speechInventoryPriceCollections=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').get()#takes all the document of the collection SpeechInventoryPrice stored in corresponding documents
        for docu2 in speechInventoryPriceCollections:#repeating the same process again for collections in random Documents
            #print(u'{} => {}'.format(docu2.id, docu2.to_dict()))
            db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).set(docu2.to_dict())
            pricecollection=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'pricecollection').get()
            stockcollection=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'stockcollection').get()
            for priceDocuments in pricecollection:
                #print(u'{} => {}'.format(priceDocuments.id, priceDocuments.to_dict()))
                db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'pricecollection').document(priceDocuments.id).set(priceDocuments.to_dict())
            for stockDocuments in stockcollection:
                #print(u'{} => {}'.format(stockDocuments.id, stockDocuments.to_dict()))
                db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'stockcollection').document(stockDocuments.id).set(stockDocuments.to_dict())

 

            #collection Kirana=>document(Navkar)=>collection speechItems=>random documents=>collection speechInventoryPrice=>random documents=>pricecollection,stockcollection
           
            
num=0


            

    
