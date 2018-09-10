#part 1

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("python-78039-firebase-adminsdk-mthis-6f5f1c843f.json")
#for gunicorn -b 0.0.0.0:5000 Avenger:app --reload
def  extractFromFirebase(cred):
    firebase_admin.initialize_app(cred,{'databaseURL':'https://python-78039.firebaseio.com'})
    ref=db.reference()
    mydict=ref.get()
    return mydict

print(extractFromFirebase(cred))

#root=db.reference()
#print(root.get())

#print(mydict)

#snapshot = ref.order_by_child('height').get()

#for key,val in snapshot.items():
#    print('{0} was {1} meters tall'.format(key,val))
#new_user=root.child('users')
#new_user.update({'since':1799})

#mary=db.reference('users/{0}'.format(new_user.key)).get()
#print(mary['name'])
#print(mary['since'])

#we can give queries of the form $gt ex,query={"population":{"$gt":250000}},db.cities.find(query)
#query={"Date":{"$gt":datetime(1837,1,1),{"$lte":datetime(1837,12,31)}}}

#db.cities.find({"name":{"$exists":0}}).count() to find the count of documents that don't have a name field in cities collection
#db.cities.remove({"name":{"$exists":0}}) now we can remove this documents(very similar to find)
#
