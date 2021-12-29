from ..Resources.BaseResource import BaseResource


def to_dic_task(task):
    return {
        "task-type": task["task-type"],
        # "callbacks": task["callbacks"],
        # "items": task["items"],
        "_id": str(task["_id"]),
        'labelers':task['labelers'],
        'total_labels':task['total_labels'],
        'created_at': task["created_at"],
        'updated_at': task["updated_at"],
        'status': task["status"]
    }


class GetTasksResource(BaseResource):

    def to_dict(self):
        return {
            "project_id": self.data["project_id"],
            "tasks": [to_dic_task(task) for task in self.data["tasks"]]}
