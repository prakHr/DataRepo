import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import json

cred1=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")
cred2=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db= extractDatabase(cred1)
db1=extractDatabase(cred2)
users_ref=db.collection(u'Kiranas')
docs=users_ref.get()
ArrayToBeKeepedIn=[]
for doc in docs:
    ArrayToBeKeepedIn.append(doc.id)
print(ArrayToBeKeepedIn)
SecondArray,num=[],0
for i in ArrayToBeKeepedIn:
    if i =='Navkar_store':
        num+=1
        SpeechCollections=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').get()

        for docu in SpeechCollections:
            print(u'{} => {}'.format(docu.id, docu.to_dict()))
            db1.collection(u'Kiranas').document(u'Navkar_store').collection(u'SpeechItems').document(docu.id).set(docu.to_dict())
            speechInventoryPriceCollections=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').get()
            for docu2 in speechInventoryPriceCollections:
                print(u'{} => {}'.format(docu2.id, docu2.to_dict()))
                db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).set(docu2.to_dict())
                pricecollection=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'pricecollection').get()
                stockcollection=db.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'stockcollection').get()
                for priceDocuments in pricecollection:
                    print(u'{} => {}'.format(priceDocuments.id, priceDocuments.to_dict()))
                    db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'pricecollection').document(priceDocuments.id).set(priceDocuments.to_dict())
                for stockDocuments in stockcollection:
                    print(u'{} => {}'.format(stockDocuments.id, stockDocuments.to_dict()))
                    db1.collection(u'Kiranas').document(i).collection(u'SpeechItems').document(docu.id).collection(u'speechInventoryPrice').document(docu2.id).collection(u'stockcollection').document(priceDocuments.id).set(stockDocuments.to_dict())

                
             
            #collection speechInventoryPrice=>documents=>pricecollection,stockcollection
            
            
num=0


            

    
