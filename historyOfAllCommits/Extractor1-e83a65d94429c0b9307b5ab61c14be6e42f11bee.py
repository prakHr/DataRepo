#part 1
#function takes ssl credentials =>filename.json
#using  firebase_admin module => converts between json and native data types in this case python dictionary 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("python-78039-firebase-adminsdk-mthis-6f5f1c843f.json")

def  extractFromFirebase(cred):
    firebase_admin.initialize_app(cred,{'databaseURL':'https://python-78039.firebaseio.com'})
    ref=db.reference()
    mydict=ref.get()
    return mydict

print(extractFromFirebase(cred))

