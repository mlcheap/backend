from ..Resources.BaseResource import BaseResource


class CreateTaskResource(BaseResource):
    def label_serializer(self, label):
        # print(label)
        return {"labeler_id": label['labeler_id'],
                'task_id': label['task_id'],
                'labels': label['labels'],
                'label_time': label['label_time'],
                'inserted_at':label['inserted_at'],
                'lang': label['lang']}

    def to_dict(self):
        dic = {
            "project_id": self.data["project_id"],
            "task-type": self.data["task-type"],
            "callbacks": self.data["callbacks"],
            "items": self.data["items"],
            "_id": str(self.data["_id"]),
            'created_at': self.data["created_at"],
            'updated_at': self.data["updated_at"],
            'status': self.data["status"],
        }
        if 'labels' in self.data:
            dic['labels'] = [self.label_serializer(label) for label in self.data['labels']]
        return dic
