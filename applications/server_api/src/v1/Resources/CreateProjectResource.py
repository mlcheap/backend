from ..Resources.BaseResource import BaseResource


class CreateProjectResource(BaseResource):
    def to_dict(self):
        dic = {
            'project_name': self.data['project_name'],
            'project_id': self.data['project_id'],
            "labels_per_task": self.data["labels_per_task"],
            "icon_id": self.data["icon_id"],
        }
        for attr in ["model_id", "metadata", "lang"]:
            if attr in self.data:
                dic.update({attr: self.data[attr]})
        return dic
