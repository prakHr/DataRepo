import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
'''
PhoneNos,Name,Bills,Barcodes,SpeechItems,Date last used and kirana timestamp

+917742466334 chouhan kirana 24 4 1778 Wed Oct 10 17:19:53 Tue Oct  9 08:02:09 2018
+919166025226 Vinodji 1 1024 589 Thu Oct 11 06:23:25 Fri Aug 17 05:37:57 2018
+918290023496 RadheShyam 5 4298 589 Thu Sep 13 06:29:17 Thu Sep 13 06:27:25 2018
+919610789692 Kamlesh Kirana 14 118 600 Fri Oct  5 08:17:04 Mon Sep  3 09:45:55 2018
+919777688002 Kanha Store 15 1149 742 Tue Oct  9 09:19:26 Fri Aug 31 07:06:54 2018
+916378824851 SB Enterprises 15 659 543 Thu Sep 13 07:42:51 Mon Sep  3 09:49:40 2018
+916378867751 sagar provision store 106 1294 2099 Thu Sep 13 07:42:51 Sat Sep 15 05:59:03 2018
+919782216504 Shubham Kira 36 1201 1830 Mon Oct  8 13:40:54 Mon Sep 24 10:43:14 2018
+91901175999 Chawla Store 9 434 1319 Fri Oct  5 08:18:41 Thu Aug 16 07:05:15 2018
+918249403101 Sample Bills 1 1 442  Thu Sep 13 06:29:17 Thu Sep 13 06:27:25 2018
+916378731893 Mahesh Kirana 7 279 595 Sat Sep 29 09:32:11
+919167287597 Variety Grain 43 4 1917 Thu Oct 11 06:23:25 Mon Sep  3 09:45:55 2018
+919664087863 vardhman 47 365 1803 Tue Oct  9 09:19:26 Fri Oct  5 09:23:27 2018
+919777688001 Kumawat Store 16 610 718 Tue Oct  9 09:19:26 Tue Aug 28 06:40:08 2018
+919982204792 Nishant Store 2 1 0 Wed Oct 10 16:12:59 Sat Aug 25 11:42:05 2018
+919809258989 Apni Kirana 24 4429 589 Sat Oct  6 08:19:51 Mon Sep 24 10:43:14 2018
+919777688003 Saral Store 13 576 597 Tue Oct  9 09:19:26 Fri Aug 31 07:06:54 2018
+919011752453 Jain Departmental(has 2 phones) 23 1628 581(need to work here) Thu Aug 16 07:05:15 2018
(+919829931177 for jain departmental store ) Wed Oct 10 11:32:10 2018
+919777688639 awesome 169 8 124 Thu Oct 11 06:34:30 Mon Sep 17 09:21:48 2018
'''
cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

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


ts,current_owner,l,s=0,0,0,0
for doc in UsersArray:
    if 'kiranaName' in doc[1]:

        if 'timestamp' in doc[1]:
            ts=doc[1]['timestamp']
            if len(str(ts))==13:
                ts/=1000
                s=time.ctime(ts)#Sat Sep 29 15:02:11 2018(Day Month Date Time Year)
                    #timeStampArray.append(s[-len(s):-5])#to get rid of year Sat Sep 29 15:02:11

        current_owner=doc[1]['kiranaName']

        print('=>',current_owner,s)
        #arrayOflastUsedTimeAndtimeStamp.append([k,lastUsed,timeStamp])

#print(arrayOflastUsedTimeAndtimeStamp)




