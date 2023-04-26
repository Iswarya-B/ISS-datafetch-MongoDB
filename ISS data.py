import pymongo
import requests
import time


client = pymongo.MongoClient("mongodb://iswarya:<password>@ac-jgnafnu-shard-00-00.btxtni3.mongodb.net:27017,ac-jgnafnu-shard-00-01.btxtni3.mongodb.net:27017,ac-jgnafnu-shard-00-02.btxtni3.mongodb.net:27017/?ssl=true&replicaSet=atlas-1op5j8-shard-0&authSource=admin&retryWrites=true&w=majority")
#Creating a new instance of the MongoClient class to connect to a MongoDB server

db = client["ISS"] #Creating database
col = db["position_data"] #Creating Collection
start_time = time.time()
end_time = start_time + (2*60*60)
while time.time() < end_time:
  url = requests.get("http://api.open-notify.org/iss-now.json") #Link to fetch the data
  data = url.json()
  col.insert_one(data)
  time.sleep(10)

