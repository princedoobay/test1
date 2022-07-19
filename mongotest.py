import pymongo
client = pymongo.MongoClient("mongodb+srv://Prince:Prince.54@cluster0.jlitp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
call = db1['test']
call.insert_one(d )