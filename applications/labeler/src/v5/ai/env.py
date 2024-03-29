import os

MODEL_BASE_URL = os.getenv('MODEL_URL') or "https://skillai.mlcheap.com"
# MODEL_BASE_URL = "https://skillai.mlcheap.com"
# LABELER_BASE_URL = "http://localhost:6221"
HTTP_TOTAL_RETRIES = 4  # Number of total retries
HTTP_RETRY_BACKOFF_FACTOR = 1  # Wait 1, 2, 4 seconds between retries
HTTP_STATUS_FORCE_LIST = [408, 429] + list(range(500, 531))
# HTTP_STATUS_FORCE_LIST = list(range(200, 531))
HTTP_RETRY_ALLOWED_METHODS = frozenset({"GET", "POST", "DELETE"})
