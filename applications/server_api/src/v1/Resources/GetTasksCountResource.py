from ..Resources.BaseResource import BaseResource


class GetTasksCountResource(BaseResource):

    def to_dict(self):
        return {"count": self.data}
