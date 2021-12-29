from app import db
from bson import ObjectId
import datetime
from model.utils import get_class_col


def create_class(customer_id, project_id, name, metadata, unique_id):
    created_at = updated_at = datetime.datetime.utcnow()

    class_db = get_class_col(project_id)

    data_dic = {"project_id": project_id,
                "customer_id": customer_id,
                'created_at': created_at,
                'updated_at': updated_at,
                'name': name,
                'metadata': metadata}
    if unique_id:
        unique_id = str(unique_id)
        if len(unique_id) == 24:
            unique_id = ObjectId(str(unique_id))
        item = class_db.find_one({"_id": unique_id})
        if item:
            return {**item}
        else:
            class_db.insert_one({
                **data_dic,
                "_id": str(unique_id)})
        inserted_id = unique_id

    else:
        inserted_id = class_db.insert_one(data_dic).inserted_id
    return {
        "_id": str(inserted_id),
        **data_dic,
    }


def find_class(project_id, class_id):
    class_db = get_class_col(project_id)
    class_id = str(class_id)
    if len(class_id) == 24:
        class_id = ObjectId(class_id)
    return class_db.find_one({"_id": class_id})


def cancel_class(project_id,
                 class_id):
    class_db = get_class_col(project_id)
    class_db.delete_one({"_id": ObjectId(class_id)})


def find_classes(project_id):
    class_db = get_class_col(project_id)
    return class_db.find({}, {"name": 1})


def count_classes(project_id):
    class_db = get_class_col(project_id)
    return class_db.find({}).count()
