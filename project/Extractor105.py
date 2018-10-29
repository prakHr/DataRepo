import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
#import time
from waitress import serve
#from paste.translogger import TransLogger
import json
from bson import Binary,Code
from bson.json_util import dumps
import flask_cors
from flask import Flask,render_template,request,jsonify,redirect,session,abort,make_response,url_for
from flask_cors import CORS, cross_origin
import random
from pymongo import MongoClient
from time import gmtime,strftime
import sqlite3


cred=credentials.Certificate("python-78039-firebase-adminsdk-mthis-66f13748f8.json")

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db
db=extractDatabase(cred)

def Extractor(reference):
    docs=reference.get()
    array=[]
    for doc in docs:
        array.append([doc.id,doc.to_dict()])
    return array
#(if possible put into mongodb) First after extracting or in this case printing
collection1,collection2=u'Kiranas',u'Mehboobs'

ref1,ref2=db.collection(collection1),db.collection(collection2)
kiranasList,mehboobsList=Extractor(ref1),Extractor(ref2)
#print(kiranasList)

# connection to MongoDB Database
connection = MongoClient("mongodb://localhost:27017/")

def create_mongodatabase(klist):
    try:
        dbnames=connection.database_names()
        if 'cloud_native' not in dbnames:
            db=connection.cloud_native.users
            for mineIsYours in klist:
                db.insert(mineIsYours[1])
        else:#at this step in the future we will empty the database or make a new collection and then put everything there
            print("Database already Initialized!")
    except:
        print("Database creation failed!!")

array=kiranasList


# Object creation
app=Flask(__name__,template_folder='templates')
app.config.from_object(__name__)
app.secret_key='<secret>'
CORS(app)

#List users
def list_users():
    api_list=[]
    db=connection.cloud_native.users
    for row in db.find():
        api_list.append(str(row))
    return jsonify({'user_list':api_list})

#List specific users
def list_user(user_id):
    api_list=[]
    db=connection.cloud_native.users
    for i in db.find({'id':user_id}):
        api_list.append(str(i))
    if api_list==[]:
        abort(404)
    return jsonify({'user_list':api_list})

# API Routes
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/clear')
def clearsession():
    session.clear()
    return redirect(url_for('main'))

@app.route('/api/v1/users',methods=['GET'])
def get_users():
    return list_users()

@app.route('/api/v1/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    return list_user(user_id)

#Error Handling
@app.errorhandler(404)
def resource_not_found(error):
    return make_response(jsonify({'error':'Resource not found!'}),404)

@app.errorhandler(409)
def user_found(error):
    return make_response(jsonify({'error': 'Conflict! Record exist'}), 409)

@app.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

if __name__=='__main__':
    create_mongodatabase(kiranasList)
    app.run(host='0.0.0.0',port=5000,debug=True)

