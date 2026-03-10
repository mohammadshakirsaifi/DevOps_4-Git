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
