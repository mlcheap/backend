from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash
from bson import ObjectId


def find_customer_by_id(customer_id):
    return db['customer'].find_one({'_id': ObjectId(customer_id)})


def find_customer_by_username(username):
    return db['customer'].find_one({'username': username})


def find_customer_by_token(token):
    return db['customer'].find_one({'token': token})


def add_customer(username, password):
    user = {'username': username,
            'created_at': datetime.now(),
            'password': password}
    db["customer"].insert_one(user)


def save_token(customer_id, token):
    db['customer'].update_one({"_id": ObjectId(customer_id)}, {"$set": {"token": token}})


def has_token(customer_id):
    customer = find_customer_by_id(customer_id)
    if customer and "token" in customer:
        return True
    return False


def load_token(customer_id):
    customer = find_customer_by_id(customer_id)
    if customer and "token" in customer:
        return customer["token"]
    return -1
