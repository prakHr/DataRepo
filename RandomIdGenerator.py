import random
import six

_AUTO_ID_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
def _auto_id():
    return ''.join(random.choice(_AUTO_ID_CHARS) for _ in six.moves.xrange(20))

#print(_auto_id())

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

def storePathTest(database,path,main_collection):
    my_dict={'path':path}
    FailedTransfersCollectionDocuments=db2.collection(main_collection).get()
    for doc in FailedTransfersCollectionDocuments:
        db2.collection(main_collection).document(doc.id).set(my_dict)

example_path='/Winnie/foo'
storePathTest(db2,example_path,u'FailedTransfers')
