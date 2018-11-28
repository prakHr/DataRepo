#push on githbu
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
from datetime import timedelta 

start_time=time.time()

cred1=credentials.Certificate("????????????????.json")

def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)

#Function saves Id And data-fields Into array From reference node and return that array
def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append(doc.id)
    return array

#Function has same functionality as Extractor function
def iterator(collection):
    array=[]
    for document in collection:
        array.append(document.id)
    return array


ref6=db.collection(u'Calculations')

ref7=db.collection(u'users')
UsersList=Extractor(ref7)
#print(UsersList)

#for loop takes userID in users,then takes all the ids of sub-collection(for instance ,speech_inventory)  into array
#then length of corresponding array is taken and set into a document using corresponding userID by storing the items into dictionary

for users in UsersList:
    speech_inventory_reference=ref7.document(users).collection(u'speech_inventory')
    barcode_inventory_reference=ref7.document(users).collection(u'barcode_inventory')
    bills_reference=ref7.document(users).collection(u'bills')
    customers_reference=ref7.document(users).collection(u'customers')

    length_speech_inventory=len(Extractor(speech_inventory_reference))
    length_barcode_inventory=len(Extractor(barcode_inventory_reference))
    billsArray=Extractor(bills_reference)
    length_customers=Extractor(customers_reference)

    ref6.document(users).set({
        'length_speech_inventory':length_speech_inventory
        ,'length_barcode_inventory':length_barcode_inventory
        ,'length_bills':len(billsArray)
        ,'length_customers':len(length_customers)
        })
    #total bills and payment subcollection can also be set
    '''
    for bill in bills:
        soldC=Extractor(ref7.document(users).collection('bills').document(bill).collection('sold'))
        ref6.document(users).collection('bills').document(bill).set({'billSoldLength':len(soldC)})

    for customer in length_customers:
        paymentC=Extractor(ref7.document(users).collection('customers').document(customer).collection('payment'))
        ref6.document(users).collection('customers').document(customer).collection('payment').set(
            {
                'totalPayment':len(paymentC)
             })
     '''   

        
    
end_time=time.time()-start_time
print(end_time)
    

 


    
    
    
