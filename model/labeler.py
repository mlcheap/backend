from app import db
from bson import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash
from .project import find_project_by_id, update_project

projects_db = db['projects_db']
labelers_db = db['labelers_db']
seeds_db = db['seeds_db']


def add_labeler_to_project(customer_id, project_id, emails):
    project = find_project_by_id(project_id)
    ACTIVATED_LABELERS = 'active_labelers'
    DE_ACTIVATED_LABELERS = 'deactivated_labelers'
    if project and project["customer_id"] == customer_id:
        if ACTIVATED_LABELERS not in project:
            active_labelers = emails
        else:
            active_labelers = project[ACTIVATED_LABELERS]
            for email in emails:
                if email not in active_labelers:
                    active_labelers.append(email)

        if DE_ACTIVATED_LABELERS in project:
            deactivated_labelers = project[DE_ACTIVATED_LABELERS]
            for email in emails:
                if email in deactivated_labelers:
                    deactivated_labelers.remove(email)
        else:
            deactivated_labelers = []
        update_project(project, {ACTIVATED_LABELERS: active_labelers,
                                 DE_ACTIVATED_LABELERS: deactivated_labelers})
        return active_labelers, deactivated_labelers


def serialize_labeler_by_email(email):
    labeler = find_labeler_by_email(email)
    _id = ""
    if labeler:
        _id = str(labeler["_id"])
    return {"email": email, "_id": _id}


def all_labelers_in_project(customer_id, project_id):
    project = find_project_by_id(project_id)
    active_labelers = []
    deactivated_labelers = []
    if project and project["customer_id"] == customer_id:
        if "active_labelers" in project:
            active_labelers = [serialize_labeler_by_email(email) for email in project['active_labelers']]
        if "deactivated_labelers" in project:
            deactivated_labelers = [serialize_labeler_by_email(email) for email in project['deactivated_labelers']]
    return active_labelers, deactivated_labelers


def cancel_labeler_from_project(customer_id, project_id, email):
    project = find_project_by_id(project_id)
    if project and project["customer_id"] == customer_id:
        active_labelers = project["active_labelers"]
        deactivated_labelers = project["deactivated_labelers"]
        if email in active_labelers:
            active_labelers.remove(email)
            deactivated_labelers.append(email)
        update_project(project, {"active_labelers": active_labelers,
                                 "deactivated_labelers": deactivated_labelers})
        return active_labelers, deactivated_labelers


def get_project_labelers(customer_id, project_name):
    project = projects_db.find_one({"customer_id": customer_id, "project_name": project_name})
    if "active_labelers" in project:
        return project["active_labelers"]
    return []


def find_labeler_by_email(email):
    return labelers_db.find_one({'email': email})


def create_labeler(email, name, password, gender):
    user = {'email': email,
            'name': name,
            'created_at': datetime.now(),
            'gender': gender,
            'password': generate_password_hash(password, method='sha256')}
    labelers_db.insert_one(user)


def reset_password(email, new_password):
    labelers_db.update_one({'email': email},
                           {'$set': {'password': generate_password_hash(new_password, method='sha256')}})


def find_labeler_id_by_email(email):
    labeler = labelers_db.find_one({'email': email})
    if labeler:
        return str(labeler["_id"])
    else:
        return None


def find_labeler_by_id(labeler_id):
    return labelers_db.find_one({'_id': ObjectId(labeler_id)})


def get_labeler_seed_from_db(project_absname, labeler_id):
    item = seeds_db.find_one({'project_absname': project_absname})
    if item and item['seeds']:
        for seed in item['seeds']:
            if labeler_id in item['seeds'][seed]:
                return seed


def get_labelers_seed_from_db(project_absname):
    item = seeds_db.find_one({'project_absname': project_absname})
    if item and item['seeds']:
        return item['seeds']


def set_labeler_seed_to_db(project_absname, labeler_id, seed):
    seed = str(seed)
    item = seeds_db.find_one({'project_absname': project_absname})
    if item:
        seeds = item['seeds']
        if seeds:
            if seed in seeds:
                seeds[seed].append(labeler_id)
            else:
                seeds[seed] = [labeler_id]
        else:
            seeds = {seed: [labeler_id]}

        seeds_db.update_one({'_id': item['_id']}, {'$set': seeds})
    else:
        seeds_db.insert_one({'project_absname': project_absname, 'seeds': {seed: [labeler_id]}})


def delete_labeler_seed_from_db(project_absname, labeler_id, seed):
    seed = str(seed)
    item = seeds_db.find_one({'project_absname': project_absname})
    if item:
        seeds = item['seeds']
        if seeds:
            if seed in seeds:
                seeds[seed].remove(labeler_id)
            seeds_db.update_one({'_id': ObjectId(item['_id'])}, {'$set': {'seeds': seeds}})


def get_total_rank(labeler_id):
    return 1


def get_total_score(labeler_id):
    return 1
