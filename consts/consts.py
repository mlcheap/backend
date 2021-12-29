import os

# codes
BAD_REQUEST_CODE = 400
OK_CODE = 200
SERVER_ERROR_CODE = 500
# messages
REQUEST_MUST_BE_JSON_MESSAGE = "missing JSON in request"
SUCCESS_MESSAGE = "successful"
FAILED_MESSAGE = "failed"
MISSING_MESSAGE = "missing {} parameter"
NOT_EXISt_MESSAGE = "{} not exist"
DEFAULT_ICON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'applications', 'server_api', 'src',
                                 'resources', 'data', 'icon', 'default.png')
