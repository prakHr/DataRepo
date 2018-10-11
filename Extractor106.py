import firebase_admin
from firebase_admin import *
from firebase_admin import firestore

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")
#timestamp and lastUsed apparently is calculated wrong or needed to fix(no idea right now)

'''
PhoneNos,Name,Bills,Barcodes,SpeechItems,Date last used and kirana timestamp

+917742466334 chouhan kirana 24 4 1778 Wed Oct 10 17:19:53
+919166025226 Vinodji 1 1024 589 Thu Oct 11 06:23:25
+918290023496 RadheShyam 5 4298 589 Thu Sep 13 06:29:17
+919610789692 Kamlesh Kirana 14 118 600 Fri Oct  5 08:17:04
+919777688002 Kanha Store 15 1149 742 Tue Oct  9 09:19:26
+916378824851 SB Enterprises 15 659 543 Thu Sep 13 07:42:51
+916378867751 sagar provision store 106 1294 2099 Thu Sep 13 07:42:51
+919782216504 Shubham Kira 36 1201 1830 Mon Oct  8 13:40:54
+91901175999 Chawla Store 9 434 1319 Fri Oct  5 08:18:41
+918249403101 Sample Bills 1 1 442  Thu Sep 13 06:29:17
+916378731893 Mahesh Kirana 7 279 595 Sat Sep 29 09:32:11
+919167287597 Variety Grain 43 4 1917 Thu Oct 11 06:23:25
+919664087863 vardhman 47 365 1803 Tue Oct  9 09:19:26
+919777688001 Kumawat Store 16 610 718 Tue Oct  9 09:19:26
+919982204792 Nishant Store 2 1 0 Wed Oct 10 16:12:59
+919809258989 Apni Kirana 24 4429 589 Sat Oct  6 08:19:51
+919777688003 Saral Store 13 576 597 Tue Oct  9 09:19:26
+919011752453 Jain Departmental(has 2 phones) 23 1628 581(need to work here)
(+919829931177)
+919777688639 awesome 169 8 124 Thu Oct 11 06:34:30
'''
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

for k in kiranaNamesSet:
    lastUsed,timeStamp,l,s=0,0,0,0
    for doc in UsersArray:
        if 'kiranaName' in doc[1]:
            if 'lastUsed' in doc[1]:
                lastUsedTime=doc[1]['lastUsed']
                if len(str(lastUsedTime))==13:
                    lastUsedTime/=1000
                    l=time.ctime(lastUsedTime)
                    
            if 'timestamp' in doc[1]:
                timeStamp=doc[1]['timestamp']
                if len(str(timeStamp))==13:
                    timeStamp/=1000
                    s=time.ctime(timeStamp)#Sat Sep 29 15:02:11 2018(Day Month Date Time Year)
                    #timeStampArray.append(s[-len(s):-5])#to get rid of year Sat Sep 29 15:02:11

            current_owner=doc[1]['kiranaName']
        if k==current_owner:
            lastUsed=str(l)[-13:-5]
            timeStamp=str(s)[-13:-5]      
    print('kiranaOwner , lastUsed variable here=>',k,lastUsed)
    #arrayOflastUsedTimeAndtimeStamp.append([k,lastUsed,timeStamp])
    
print(arrayOflastUsedTimeAndtimeStamp)




