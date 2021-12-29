from ..Resources.BaseResource import BaseResource


def project_to_dic(project):
    return {
        "project_name": project["project_name"],
        "created_at": project["created_at"],
        "updated_at": project["updated_at"],
        "project_id": str(project["_id"]),
    }


class GetAllProjectsResource(BaseResource):

    def to_dict(self):
        return {
            'projects': [project_to_dic(project) for project in self.data["projects"]]
        }
