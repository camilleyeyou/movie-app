import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
db_name = os.getenv('MONGO_DB_NAME', 'movie_app_db')

print(f"Attempting to connect with URI: {mongo_uri}")

try:
    client = pymongo.MongoClient(mongo_uri)
    
    client.admin.command('ping')
    
    print(f"Successfully connected to MongoDB!")
    
    db = client[db_name]
    print(f"Connected to database: {db_name}")
    
    print("Collections:")
    for collection in db.list_collection_names():
        print(f"- {collection}")
        
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")