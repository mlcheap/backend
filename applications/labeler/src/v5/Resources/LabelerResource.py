from Resource.BaseResource import BaseResource


class LabelerResource(BaseResource):
    def to_dict(self):
        return {
            'user': {
                'id': str(self.data['_id']),
                'name': self.data['name'],
                'email': self.data['email'],
                'gender': self.data['gender'],
                'created_at': self.data['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            }
        }
