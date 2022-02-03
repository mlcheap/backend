import flask_restful
from ..view.auth import Signin, Signup, Logout, ResetPassword
from ..view.init import Init
from ..view.file import Image, Icon
from ..view.label import LabelTask, NewTask, GetProject
from ..view.ai import Ai
from ..view.classes import GetClass, GetAllClasses
from ..view.rank import RankDB, RankInfo


def initialize_routes(api: flask_restful.Api):
    api.add_resource(Signin, '/auth/signin')
    api.add_resource(Signup, '/auth/signup')
    api.add_resource(Logout, '/auth/logout')
    api.add_resource(ResetPassword, '/auth/reset-password')

    api.add_resource(Init, '/init')

    api.add_resource(Icon, '/file/icon')
    # api.add_resource(Image, '/image')
    #
    api.add_resource(LabelTask, '/label/label-task')
    api.add_resource(NewTask, '/label/new-item')
    api.add_resource(GetProject, '/label/project')
    api.add_resource(Ai, '/ai')
    api.add_resource(GetClass, '/class')
    api.add_resource(GetAllClasses, '/classes')

    #
    # api.add_resource(RankDB, '/ranking/db')
    # api.add_resource(RankInfo, '/ranking/info')
