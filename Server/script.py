from Server import app
import os
import json
import csv

userdata  = os.path.join(app.static_folder, 'json', 'userdata.json')
booksdata = os.path.join(app.static_folder, 'json', 'booksdata.json')
favourite = os.path.join(app.static_folder, 'json', 'favourites.json')

def createUser(name, surname, username, email, password):
    user = {"name": str(name),
            "surname": str(surname),
            "username": str(username),
            "email": str(email),
            "password": str(password)}

    return user

def createBook(name, author, content, price, img):
    book = {"name": str(name),
            "author": str(author),
            "content": str(content),
            "price": str(price),
            "img": str(img)}

    return book

def createFavourite(name, author):
    fav = {"name": str(name),
            "author": str(author)}

    return fav

def readJSON(file):
    path = '../static/json'
    f_path = os.path.join(path, file)
    if os.path.exists(f_path):
        with open(file, 'r') as openfile:
            return json.load(openfile)

def appendJSON(new_data, section, filename):
    path = '../static/json'
    f_path = os.path.join(path, filename)
    if os.path.exists(f_path):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data[section].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        return 'Invalid filename'

def modifyJSON(new_data, section, value, filename):
    path = '../static/json'
    f_path = os.path.join(path, filename)
    if os.path.exists(f_path):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data[section][value] = new_data
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        return 'Invalid filename'

def checkCoincidenceJSON(object_name, section, value, filename):
    data = readJSON(filename)
    for entry in data[section]:
        print(entry)
        print(entry[value])
        if entry[value] == str(object_name):
            return True
    return False

def removeObjJSON(object_name, section, value, filename):
    new_data = {section: []}
    data = readJSON(filename)

    for entry in data[section]:
        if entry[value] == str(object_name):
            continue
        new_data[section].append(entry)
    path = '../static/json'
    f_path = os.path.join(path, filename)
    if os.path.exists(f_path):
        with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)


def createNewUser(name, surname, username, email, password):
    user = createUser(name, surname, username, email, password)
    appendJSON(user, "userdata", userdata)

def editUser(name, surname, email, password):
    user = createUser(name, surname, email, email, password)
    if checkCoincidenceJSON(email, 'userdata', 'email', userdata):
        # remove old entity
        removeObjJSON(email, 'userdata', 'email', userdata)
        # add modified entity
        appendJSON(user, 'userdata', userdata)
        return "'User edited successfully!'"
    else:
        return "No user with such data."


def compareField(file, section, attribute, value):
    file = readJSON(file)

    for x in file[section]:
        if x[attribute] == str(value):
            return True
    return False

def checkLogin(email, password):
    return compareField(userdata, "userdata", 'email', email) and compareField(userdata, 'userdata', 'password', password)

def updateFavourite(value, bookname, author):
    if value:
        # Add book to Database
        addFavourite(bookname, author)
        return True
    else:
        # Remove book from Database
        removeFavourite(bookname)
        return False

def addFavourite(bookname, author):

    if not checkCoincidenceJSON(bookname, 'favourites', 'name', favourite):
        createFavourite(bookname, author)
        appendJSON(createFavourite(bookname, author), 'favourites', favourite)

        print("Book '" + bookname + "' added to favourites.")
        return True
    else:
        print("Book '" + bookname + "' is already in favourites.")
        return True


def removeFavourite(bookname):
    try:
        removeObjJSON(bookname, 'favourites', 'name', favourite)
    except:
        print("Book '" + bookname + "' was not found.")
        return False
    print("Book '" + bookname + "' deleted from favourites.")
    return True

