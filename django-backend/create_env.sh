#!/bin/bash

pip install virtualenv
#Create a virtualenv
virtualenv venv
# shellcheck disable=SC2164
source venv/bin/activate

pip install -r requirements.txt
