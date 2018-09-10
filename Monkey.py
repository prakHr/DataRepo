#part 2
#how to start mongo,first mongo,sudo mongod --dbpath /var/lib/mongodb
#2011A3PS090P-Issan bhaiya
import pymongo
from pymongo import MongoClient
#cred = credentials.Certificate("python-78039-firebase-adminsdk-mthis-6f5f1c843f.json")
def putIntoMongoDB(db,collection,mydict):
    collection.insert(mydict)
#mydict=extractFromFirebase(cred)
myclient=MongoClient("mongodb://localhost:27017")    
mydb=myclient["users"]
mycollection=mydb["customers"]
#mydict={ 'dinosaurs': {'lambeosaurus': {'height': 2.1, 'length': 12.5, 'weight': 5000}, 'stegosaurus': {'height': 4, 'length': 1231, 'weight': 131}}, 'users': 213}
putIntoM#mongoDB(mydb,mycollection,mydict)
#my ip address 192.168.43.101:5000/meter
#counter=1
#for i in mycollection.find():
  #  print(i)
    #print(counter)
    #counter+=1
#mydict comes from part 1
#print(myclient.list_database_names())
#print(mydb.list_collection_names())
#collist=mydb.list_collection_names()
import json
#mycollection.insert(mydict)#or iterate and insert

#print(mycollection.find())
#what to write in terminal and hope it works
#mongo
#show dbs
#use clients
#db.clients.find()
#db.clients.drop()
#db.drop
#db.dropDatabase()
#show dbs
#exit
#show collections

#can be done from terminal like this mongoimport --db users --collection contacts --file contacts.json 
