import flask_restful
from ..view.projects import CreateProject, GetAllProjects, GetProject, EditProject
from ..view.file import UploadFile, ImportFile, DownloadFile
from ..view.tasks import CreateTask, GetTask, GetTasks, GetTasksCount, CancelTask
from ..view.labeler import AddLabeler, CancelLabeler, AllLabelers
from ..view.classes import GetClasses, GetClass, CreateClass, CreateClasses


def initialize_routes(api: flask_restful.Api):
    api.add_resource(CreateProject, '/create-project')
    api.add_resource(GetAllProjects, '/all-projects')
    api.add_resource(EditProject, '/edit-project')
    api.add_resource(GetProject, '/project')
    api.add_resource(UploadFile, '/file/upload-file')
    api.add_resource(ImportFile, '/file/import-file')
    api.add_resource(DownloadFile, '/file/download-file')
    api.add_resource(CreateTask, '/create-task')
    api.add_resource(CreateClass, '/create-class')
    api.add_resource(CreateClasses, '/create-classes')
    api.add_resource(GetTask, '/task')
    api.add_resource(GetClass, '/class')
    api.add_resource(GetTasks, '/tasks')
    api.add_resource(GetClasses, '/classes')
    api.add_resource(CancelTask, '/cancel-task')
    api.add_resource(GetTasksCount, '/tasks-count')
    api.add_resource(AddLabeler, '/add-labelers')
    api.add_resource(CancelLabeler, '/cancel-labeler')
    api.add_resource(AllLabelers, '/all-labelers')
