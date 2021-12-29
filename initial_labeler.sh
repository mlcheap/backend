#!/bin/bash
LABELER_PATH="./applications/labeler"
ENV_PATH="${LABELER_PATH}/venv"
APP_PATH="${LABELER_PATH}/app.py"
python3 -m venv "${ENV_PATH}"
source "${ENV_PATH}/bin/activate"
pip3 install -r "requirements.txt"
python3 -m run $APP_PATH
