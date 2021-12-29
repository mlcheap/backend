# codes
BAD_REQUEST_CODE = 400
OK_CODE = 200
UNAUTHORIZED_CODE = 401
SERVER_ERROR_CODE = 500

# messages
REQUEST_MUST_BE_JSON_MESSAGE = "missing JSON in request"
SUCCESS_MESSAGE = "successful"
FAILED_MESSAGE = "failed"
EXPIRATION_TOKEN_MESSAGE = "The token has expired"
MISSING_MESSAGE = "missing {} parameter"
WRONG_LOGIN_MESSAGE = "email or password is wrong"
EMAIL_EXIST_MESSAGE = "email address already exists"
EXIST_MESSAGE = "{} already exists"
USER_NOT_EXIST_MASSAGE = "labeler not exists"
NOT_ACTIVE_DATABASE = "DATABASE NOT ACTIVE"
UN_PERMITTED_MESSAGE = "you not have permission"

# data
THERE_IS_NO_MORE_DATA = "there is no more data"
NOT_VALID_LABELS = "not valid labels"
IMAGE_DATA = 'image'
TEXT_DATA = 'text'
IMAGE2_DATA = 'image2'
DATA = "data"
COMPARE_IMAGE_DATA = 'compare-image'

# label
LABEL = "label"
TEXT_LABEL = 'text'
STAR_LABEL = 'star'
ENUM_LABEL = 'enum_labels'
AGE_LABEL = 'age'
MULTI_CLASS_LABEL = 'multi_class'
RADIO_LABEL = 'radio-label'
COMPARE_LABEL = 'compare'
BOOLEAN_LABEL = 'boolean'
REAL_LABEL = 'real'

# langs
ENGLISH_LANG = 'en'
PERSIAN_LANG = 'fa'

# constrains
SPECIAL_LIST = 'special_list'

# DB_TYPE
STATIC_LABEL = "static-label"
DYNAMIC_LABEL = "dynamic-label"

# SEED TYPE
MONO_SEED = "mono"
SHARED_SEED = "shared"

# Quality Types
SELF_CONSISTENCY_COMPARE = "self-consistency-compare"
SELF_CONSISTENCY_RATE = "self-consistency-rate"

# Generating Model
RandomCompareGenerator = "random-compare-generator"
