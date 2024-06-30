#part 2
#function takes mydict from firebase and puts it into the db and print items onto shell
#db=>users,collection =>customers
import pymongo
from pymongo import MongoClient

def putIntoMongoDB(db,collection,mydict):
    collection.insert(mydict)
    for i in collection.find():
        print(i)
        print(counter)
        counter+=1
    
myclient=MongoClient("mongodb://localhost:27017")    
mydb=myclient["users"]
mycollection=mydb["customers"]

putIntoMongoDB(mydb,mycollection,mydict)

counter=1


