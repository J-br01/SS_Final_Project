from Server import app
import os
import json
import csv

userdata  = os.path.join(app.static_folder, 'json', 'userdata.json')
booksdata = os.path.join(app.static_folder, 'json', 'booksdata.json')

def createUser(name, surname, username, email, password):
    user = {"name": str(name),
            "surname": str(surname),
            "username": str(username),
            "email": str(email),
            "password": str(password)}

    return user

def readJSON(file):
    with open(file, 'r') as openfile:
        return json.load(openfile)

def appendJSON(new_data, section, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data[section].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def createNewUser(name, surname, username, email, password):
    user = createUser(name, surname, username, email, password)
    appendJSON(user, "userdata", userdata)

def compareField(file, section, attribute, value):
    file = readJSON(file)

    for x in file[section]:
        if x[attribute] == str(value):
            return True
    return False

def checkLogin(email, password):
    return compareField(userdata, "userdata", 'email', email) and compareField(userdata, 'userdata', 'password', password)
