from ..Resources.BaseResource import BaseResource


class GetProjectResource(BaseResource):
    def to_dict(self):
        dic = {
            "created_at": self.data["created_at"],
            "updated_at": self.data["updated_at"],
            "project_name": self.data["project_name"],
            "project_id": str(self.data["_id"]),
            "metadata": self.data['metadata'],
            "labels_per_task": self.data["labels_per_task"],
            "icon_id": self.data["icon_id"],
            "stat": self.data["stat"]
        }
        if "model_id" in self.data:
            dic.update({"model_id": self.data['model_id']})
        return dic
