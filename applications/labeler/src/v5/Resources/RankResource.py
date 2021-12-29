from Resource.BaseResource import BaseResource


class RankResource(BaseResource):
    def to_dict(self):
        return {
            'rank': str(self.data['rank']),
            'score': self.data['score'],
        }
