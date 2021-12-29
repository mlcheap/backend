from ..Resources.BaseResource import BaseResource


class CreateClassResource(BaseResource):
    def to_dict(self):
        dic = {
            "project_id": self.data["project_id"],
            "name": self.data["name"],
            "metadata": self.data["metadata"],
            "_id": str(self.data["_id"]),

        }
        return dic
