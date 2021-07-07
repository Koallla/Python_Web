from helpers import show_table
from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://mika:290922@cluster0.im3uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


# CONNECT TO DB
db = client.personal_assistant

# CONNECT TO COLLECTION
records_db = db.records


# rec = {
#     "name": "Filya",
#     "surname": "Cat",
#     "adress": "Cat house",
#     "note": ["Toilet", "Sleep"],
#     "tag": ["Wool", "Cute"],
#     "birthday": datetime.datetime.utcnow()
# }

# ADD
# test_collection.insert_one(rec).inserted_id

# UPDATE
# test_collection.update_one({'_id': ObjectId('60e3490c0b95927afe125621')},
# { "$set": {"age": 4} })

# DEL
# test_collection.delete_one({'name': 'Liza'})


# result = test_collection.find()



# for el in result:
#     print(el)






class WorkWithDataInDb():

    def show_records_for_query(self, query):
        pass


    def show_all_records(self, size=None):
        pass

    def update_record(self, query, name, field, new_data):
        pass


    def delete_record(self, query, name):
        pass
