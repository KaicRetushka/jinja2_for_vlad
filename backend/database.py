import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['jinja2_mongo_db']

colection_users = db['users']

def select_all_login():
    return colection_users.find({}, {'login': 1, '_id': 0})

def insert_user(login, password, name, surname):
    user = colection_users.find_one({'login': login})
    if user:
        return False
    colection_users.insert_one({'login': login, 'name': name, 'surname': surname, 'password': password})
    return True