#!/bin/bash

PYTHON_PATH="/opt/python-2.7.9/bin/python"
APP_SELECTOR="/home/mya/outside_dir.txt"
DATE="outside_$(date +\%Y-\%m-\%d--\%H-\%M-\%S)"
TARGET_DIR="/home/mya/apps/$DATE"
GET_VERSION_CMD="git clone git@github.com:phelmig/outside.git ."

# Create Target Directory
if [ -d "$TARGET_DIR" ]; then
  rm -rf "$TARGET_DIR"
fi
mkdir -p $TARGET_DIR
cd $TARGET_DIR

# Get the latest Version
$GET_VERSION_CMD
cd mvp/
# Switch to productive settings
mv "$TARGET_DIR/mvp/outside/outside/settings_prod.py" "$TARGET_DIR/mvp/outside/outside/settings.py"

# install virtualenv
virtualenv --python=$PYTHON_PATH .
source bin/activate

#Install required Software
pip install -r requirements.txt

# Update Static assets
cd outside/
./manage.py collectstatic
#./manage.py compress
echo "$TARGET_DIR/mvp" > $APP_SELECTOR


