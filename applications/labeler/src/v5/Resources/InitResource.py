from ..Resources.BaseResource import BaseResource
from ..Resources.RankResource import RankResource


class InitResource(BaseResource):

    @staticmethod
    def project_to_dict(project):
        return {
            "project_name": project["project_name"],
            "project_id": str(project["_id"]),
            'icon': project['icon'],
            'total_labeled': project['total_labeled'],
            'total_remain': project['total_remain']
        }

    def to_dict(self):
        return {
            'projects': [self.project_to_dict(project) for project in self.data['projects']],
            'rank': RankResource(self.data['rank']).to_dict(),
        }
