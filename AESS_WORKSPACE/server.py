from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"  # Update with your MongoDB URI
DATABASE_NAME = "aidata"
COLLECTION_NAME = "ai_dete"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@app.route('/add_detection', methods=['POST'])
def add_detection():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        result = collection.insert_one(data)
        
        return jsonify({"message": "Data inserted successfully", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_detections', methods=['GET'])
def get_detections():
    try:
        # Fetch all data from the collection
        detections = list(collection.find({}, {"_id": 0}).sort("timestamp", -1))[:4]  # Exclude the MongoDB `_id` field from the results
        
        return jsonify({"detections": detections}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
