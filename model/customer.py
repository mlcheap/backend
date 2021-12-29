from app import db


def find_customer_by_token(token):
    return db['customer'].find_one({'token': token})
