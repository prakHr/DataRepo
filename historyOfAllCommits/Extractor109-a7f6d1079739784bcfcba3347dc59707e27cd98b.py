#printMunshik3BarcodesDictionaryCollection
import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

cred2=credentials.Certificate("project2-a9304-firebase-adminsdk-g278y-70502f4ece.json")

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db2=extractDatabase(cred2)

def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

DocumentsArray=Extractor(db2.collection(u'Kiranas'))
'''
def printFromBarcodesCollection(b_collection):
    #name_array,number_array,price_array,len_price_array=[],[],[],[]
    array=[]
    for random_doc in b_collection:
        ID,my_dict=random_doc.id,random_doc.to_dict()
        if 'name' not in my_dict:
            print('barcodeName not found in id of kiranas collection: '+str(ID))
            if 'barcode' not in my_dict:
                print('barcodeNumber not found in id of kiranas collection: '+str(ID))
                if 'price' not in my_dict:
                    print('barcodePrice not found in id of kiranas collection: '+str(ID))
            continue
        name,number,price=my_dict['name'],my_dict['barcode'],my_dict['price']
        array.append([name,number,price,len(price)])
        #name_array.append(name);number_array.append(number);price_array.append(price);len_price_array.append(len(price))
        #array.append(name,number,price,len(price))#array[0]=name,array[1]=number,array[2]=price,array[3]=len(price)
    #print(array)
    return array
arrayOfArrays=[]
for doc in DocumentsArray:
    #arrayOfArrays=[] doubt here
    ids,my_dict,array=doc[0],doc[1],[]
    BarcodesCollection=db2.collection(u'Kiranas').document(ids).collection(u'Barcodes').get()
    array=printFromBarcodesCollection(BarcodesCollection)
    arrayOfArrays.append(array)
print(arrayOfArrays)
'''
for doc in DocumentsArray:
    ids=doc[0]
    SpeechItemsCollectionRef=db2.collection(u'Kiranas').document(ids).collection(u'SpeechItems')
    speechArray=Extractor(SpeechItemsCollectionRef)
    for ids1,my_dict in speechArray:
        print(ids1)
    
