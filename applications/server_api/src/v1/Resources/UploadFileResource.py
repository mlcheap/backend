from ..Resources.BaseResource import BaseResource


class UploadFileResource(BaseResource):
    def to_dict(self):
        return {"created_at": self.data["created_at"],
                "updated_at": self.data["updated_at"],
                "mime_type": self.data["mime_type"],
                "file_id": self.data["file_id"],
                "file_name": self.data["file_name"]}
