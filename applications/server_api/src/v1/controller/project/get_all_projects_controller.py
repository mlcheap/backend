from model.project import find_all_projects


def get_all_projects_process(customer_token):
    projects = find_all_projects(customer_token)
    print("projects", projects)
    return projects
