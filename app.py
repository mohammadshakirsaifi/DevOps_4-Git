from flask import Flask, request, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)

# Serve HTML form
@app.route('/')
def form():
    return send_from_directory('.', 'todo_form.html')

# Backend API
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["todo_db"]
    collection = db["items"]

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return "Item Stored Successfully"

if __name__ == "__main__":
    app.run(debug=True)
