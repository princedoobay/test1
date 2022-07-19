

d = {
    "name" : "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
call = db1['test']
call.insert_one(d )