# DFCU_API

#1. Creating the environment.
Create a python environment using virtualenv. This guide assumes you are working on a linux environment as the commands listed are linux commands.
To install virtualenv if not available on your system, use the following commands.

​​sudo apt-get install python3-pip

sudo pip3 install virtualenv

Create a directory/folder mkdir myProject and cd myProject

virtualenv venvMyProject  - to create an environment.

#2. Pulling project from github.
Do 
git pull https://github.com/shiram/dfcu_api.git   
to get project.

Activate our environment with this command, 
source venvMyProject/bin/activate

Run pip  install -r requirements.txt -- to install project requirements.
Run ./manage.py runserver -- to start running the development server.
