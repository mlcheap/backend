from ..Resources.BaseResource import BaseResource


class AddLabelerResource(BaseResource):
    def to_dict(self):
        return {
            'token': self.data['token'],
            'project_id': self.data['project_id'],
            "active_labelers": self.data["active_labelers"],
            "deactivated_labelers": self.data["deactivated_labelers"]
        }
