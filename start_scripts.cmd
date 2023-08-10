@echo off


pip install virtualenv
virtualenv env
cd env/Scripts/
activate.bat
cd ../..
pip install -r requirements.txt