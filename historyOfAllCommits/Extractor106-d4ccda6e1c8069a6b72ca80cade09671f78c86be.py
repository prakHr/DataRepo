import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

def extractFromFirebase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db=extractFromFirebase(cred1)

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

def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array

def lengthOfCollection(collection):
    length=0
    for docs in collection:
        length+=1
    return length

ref=db.collection(u'users')

UsersArray=Extractor(ref)
kiranaNamesSet=ExtractorOfKiranaNames(ref)
#print(kiranaNamesSet)
#{ 'vardhman', 'Saral Store', 'Mahesh Kirana', 'Variety Grain', 'Kumawat Store', 'Nishant Store', 'Jain Departmental', 'Sample Bills', 'Kanha Store', 'Kamlesh Kirana', 'RadheShyam', 'Shubham Kira', 'sagar provision store', 'Apni Kirana', 'Chawla Store', 'chouhan kirana', 'SB Enterprises', 'Vinodji', 'awesome'}

arrayTupleOfNamesAndBills=[]
#Total No of bills of kirana in kiranaNamesSet
for k in kiranaNamesSet:
    total=0
    for doc in UsersArray:
        bills_collection=db.collection(u'users').document(doc[0]).collection(u'bills').get()
        bills=lengthOfCollection(bills_collection)
        if 'kiranaName' in doc[1]:
            current_owner=doc[1]['kiranaName']
        if k==current_owner:
            total+=bills
    print(k,total)
    arrayTupleOfNamesAndBills.append([k,total])
    #find the length of bills collection for users
print(arrayTupleOfNamesAndBills)
'''
Mahesh Kirana 7
vardhman 47
Saral Store 13
RadheShyam 5
awesome 169
Chawla Store 9
Variety Grain 43
Kanha Store 15
Jain Departmental 23
Shubham Kira 36
sagar provision store 106
Kanha Store 15
Nishant Store 2
Vinodji 1
Sample Bills 1
Kumawat Store 16
Apni Kirana 24
SB Enterprises 15
chouhan kirana 23
Kamlesh Kirana 14
[['Mahesh Kirana', 7], ['vardhman', 47], ['Saral Store', 13], ['RadheShyam', 5], ['awesome', 169], ['Chawla Store', 9], ['Variety Grain', 43], 
['Kanha Store', 15], ['Jain Departmental', 23], ['Shubham Kira', 36], ['sagar provision store', 106], ['Nishant Store', 2], ['Vinodji', 1], ['S
ample Bills', 1], ['Kumawat Store', 16], ['Apni Kirana', 24], ['SB Enterprises', 15], ['chouhan kirana', 23], ['Kamlesh Kirana', 14]]
'''
    

