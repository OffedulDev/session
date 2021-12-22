# Object Manager
# [
# 
# 1 - Questo file contiene tutte le classi (oggetti) che il main.py utilizza.
# 2 - Questo file contiene tutte le funzione per l'object managing.
# 
# TO-DO:
# - 
# -
# -
# -
# -
#
# ]

import json
from typing import List, Tuple

current_json = []
current_item = []
current_objects = []

# / Objects \ 

class Session:
    def __init__(self, session_token, item_list, json_list):
        if session_token == "" or session_token == None: return

        self.secret_token = str(session_token).encode("utf_32")

        try:
            self.item_list = list(item_list)
            self.json_list = list(json_list)
        except:
            return

class IntegerObject:
    def __init__(self, name, value):

        try:
            self.name = name
            self.value = int(value)
            self.type = "Integer"
        except:
            return

    def change(self, field, new_value):
        if field == "name":
            self.name = new_value
        else:
            self.value = int(new_value)

class StringObject:
    def __init__(self, name, value):

        try:
            self.name = name
            self.value = str(value)
            self.type = "String"
        except:
            return

    def change(self, field, new_value):
        if field == "name":
            self.name = new_value
        else:
            self.value = str(new_value)

class TupleObject:
    def __init__(self, name, value):

        try:
            self.name = name
            self.value = tuple(value)
            self.type = "Tuple"
        except:
            return

    def change(self, field, new_value):
        if field == "name":
            self.name = new_value
        else:
            self.value = tuple(new_value)

class ListObject:
    def __init__(self, name, value):

        try:
            self.name = name
            self.value = list(value)
            self.type = "List"
        except:
            return

    def change(self, field, new_value):
        if field == "name":
            self.name = new_value
        else:
            self.value = list(new_value)

class UnknownObject:
    def __init__(self, name, value):

        try:
            self.name = name
            self.value = value
            self.type = "Unknown"
        except:
            return

    def change(self, field, new_value):
        if field == "name":
            self.name = new_value
        else:
            self.value = new_value
# / Functions \ 

def AddJsonToSession(_json):
    if _json == None or _json == "": return

    try:
        formattedObject = json.loads(_json)

        if formattedObject['type'] == "Integer":
            obj = IntegerObject(formattedObject['name'], formattedObject['value'])

            AddJson(obj)
        elif formattedObject['type'] == "String":
            obj = StringObject(formattedObject['name'], formattedObject['value'])

            AddJson(obj)
        elif formattedObject['type'] == "Tuple":
            obj = TupleObject(formattedObject['name'], formattedObject['value'])

            AddJson(obj)
        elif formattedObject['type'] == "List":
            obj = ListObject(formattedObject['name'], formattedObject['value'])

            AddJson(obj)
        else:
            obj = UnknownObject(formattedObject['name'], formattedObject['value'])

            AddJson(obj)
        
    except:
        return

def AddJson(object):
    # if not isinstance(object, IntegerObject) or not isinstance(object, StringObject) or not isinstance(object, Tuple) or not isinstance(object, ListObject): return

    formattedObject = {
        "name": object.name,
        "value": object.value,
        "type": object.type
    }

    jsonObject = json.dumps(formattedObject)
    current_json.append(jsonObject)
    current_item.append(formattedObject["name"])

def updateSession():
    for obj in current_objects:
        if isinstance(obj, Session):
            obj.json_list = current_json
            obj.item_list = current_item
        else:
            continue

def initializeSession(token):
    
    _count = IntegerObject("count", 0)

    for obj in current_objects:
        if isinstance(obj, Session):
            return
        else:
            continue
    
    startSession(token)

def startSession(token):
    current_objects.append(Session(token, current_item, current_json))

    
# / Init \

def init():
    initializeSession("VmYq3t6w9z$C&F)J@McQfTjWnZr4u7x!")

    # a = StringObject("a", "hey")
    # b = StringObject("b", "fsdhu")
    # c = StringObject("c", "543")
    # d = StringObject("d", "dsa")

    # AddJson(a)
    # AddJson(b)
    # AddJson(c)
    # AddJson(d)

    # AddJsonToSession(current_json[0])
    # AddJsonToSession(current_json[1])
    # AddJsonToSession(current_json[2])
    # AddJsonToSession(current_json[3])

    # current_json.pop(0)
    # current_json.pop(1)
    # current_json.pop(2)
    # current_json.pop(3)

    # print(current_json)

if __name__ == "__main__":
    init()
