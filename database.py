# Base de datos en memoria
db = []

def create_string(string):
    if string in db:
        return {"error": "String already exists"}, 400
    db.append(string)
    return {"message": "String added"}, 201

def read_strings():
    return {"data": db}, 200

def update_string(old_string, new_string):
    if old_string not in db:
        return {"error": "String not found"}, 404
    if new_string in db:
        return {"error": "New string already exists"}, 400
    index = db.index(old_string)
    db[index] = new_string
    return {"message": "String updated"}, 200

def delete_string(string):
    if string not in db:
        return {"error": "String not found"}, 404
    db.remove(string)
    return {"message": "String deleted"}, 200
