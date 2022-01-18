from ..Resources.BaseResource import BaseResource


def class_to_dict(_class):
    return {
        "name": _class["name"],
        "alternates":_class['metadata']["alternates"],
        "_id": str(_class["_id"]),
    }


class GetClassesResource(BaseResource):

    def to_dict(self):
        dic = {"classes": [class_to_dict(_class) for _class in self.data["classes"]]}
        return dic
