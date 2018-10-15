#printMunshik3BarcodesDictionaryCollection
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

#function takes reference of mainCollections as argument and print the value corresponding to dictionary[keys] of all documents
def printDocumentsOfMainCollection(reference):
    main_collection=reference.get()
    for doc in main_collection:
        d=doc.to_dict()
        print(d,end='\n')

#function prints only the specific value corresponding to a specific key existing in all documents        
def printValueOfSpecificDictKeyOfMainCollection(reference,key):
    main_collection=reference.get()
    for doc in main_collection:
        d=doc.to_dict()
        if key in d:
            print(d[key])

cred1=credentials.Certificate('munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json')
db1=extractDatabase(cred1)
users_ref=db1.collection(u'users')
#printValueOfSpecificDictKeyOfMainCollection(users_ref,'units')
'''outputs is of the forms:-
['कि.ग्रा. / ग्राम', 'लीटर / मि.ली.', ' इकाई', 'अन्य'] comes from {'units': ['कि.ग्रा. / ग्राम', 'लीटर / मि.ली.', ' इकाई', 'अन्य']} 
'''
cred2=credentials.Certificate("project2-a9304-firebase-adminsdk-g278y-70502f4ece.json")
db2=extractDatabase(cred2)
Kiranas_ref=db2.collection(u'Kiranas')
#printDocumentsOfMainCollection(Kiranas_ref)
'''outputs is of the forms:-
{'address': 'banyan tree', 'transferTo': True}
{'address': 'fatehsagar'}
{'address': 'pichhola'}
'''
