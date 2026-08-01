from pymongo.mongo_client import MongoClient

# Replace YOUR_PASSWORD with your actual password (and consider using environment variables)
uri = "mongodb+srv://asad_networksecurity:YOUR_PASSWORD@networksecuritycluster1.j28zwrd.mongodb.net/?appName=NetworkSecuritycluster1"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    # Indentation added here
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    # Indentation added here
    print(f"Connection failed: {e}")