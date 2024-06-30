'''
fromId:[+918432520108,+919799498646]
toId:33456

start:1538073000000
end  :1538332200000

timestamp changed to 1514745000000'''
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time,sys
import random,six
cred1=credentials.Certificate("project1-4e7b7-firebase-adminsdk-7irgt-433da006ab.json")
# database extraction using the credential
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db1=extractDatabase(cred1)

def function1(db1,phonesSourcesArray,destinationPhone,start_timestamp,end_timestamp):
    _AUTO_ID_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    def _auto_id():
        return ''.join(random.choice(_AUTO_ID_CHARS) for _ in six.moves.xrange(20))
    
    collection1,collection2,collection8=u'barcode_inventory',u'barcode_repeats',u'users'
    usersCollection1=collection1
    barcodesNumAndDict={}
    barcodesCount=[]
    for phoneNumber in phonesSourcesArray:
        barcodeInventoryCollectionDocuments=db1.collection(collection8).document(phoneNumber).collection(usersCollection1).get()

        for doc in barcodeInventoryCollectionDocuments:
            my_dict=doc.to_dict()
            ts=my_dict['timestamp']
            if (start_timestamp<= ts <=end_timestamp):

                number=my_dict['barcodeNumber']

                barcode_inventory_reference=db1.collection(collection1)
                docs=barcode_inventory_reference.get()
                
                #barcodesNumAndDict=>dictionary that append multiple values for same keys in an array {key1:[value1,value2],...}
                #key=>barcodeNumber,value=>my_dict
                if number not in barcodesNumAndDict:#we can also use collections.defaultdict
                    barcodesNumAndDict[number]=[my_dict]
                else:
                    if my_dict not in barcodesNumAndDict[number]:
                        barcodesNumAndDict[number].append(my_dict)
                #if multiple collection set overwrites the data and takes the latest document
                db1.collection(collection8).document(destinationPhone).collection(collection1).document(doc.id).set(my_dict)
    print(barcodesNumAndDict)
    #after putting all documents in barcode_inventory we can iterate throught the collection and put documents in barcode_repeats according to dictionary 
    collection=db1.collection(collection8).document(destinationPhone).collection(collection1).get()
    
    for doc in collection:
        my_dict=doc.to_dict()
        id=doc.id
        multiple_values=barcodesNumAndDict[id]
        length=len(multiple_values)
        if length==1:continue
        for i in range(length):
            if multiple_values[i]!=my_dict:
                db1.collection(collection8).document(destinationPhone).collection(collection2).document(_auto_id()).set(multiple_values[i])
    

function1(db1,['+918432520108','+919799498646'],'33456',1514745000000,1538332200000)

