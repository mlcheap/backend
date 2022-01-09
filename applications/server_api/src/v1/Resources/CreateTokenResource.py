from ..Resources.BaseResource import BaseResource


class CreateTokenResource(BaseResource):
    def to_dict(self):
        return {
            'token': self.data['token'],
        }
