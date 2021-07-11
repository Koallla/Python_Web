from pymongo import MongoClient

client = MongoClient("mongodb+srv://mika:290922@cluster0.im3uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


# CONNECT TO DB
db = client.personal_assistant

# CONNECT TO COLLECTION
records_db = db.records