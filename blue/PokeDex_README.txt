sudo apt install python3-pip
python3 -m pip install --user --upgrade pip
sudo apt-get install python3-venv
sudo apt-get install python3-tk
python3 -m venv env
source env/bin/activate
  pip3 install requests
  pip3 install pillow
  pip3 freeze > requirements.txt
  deactivate
python3 -m venv env2
source env2/bin/activate
  pip3 install -r requirements.txt
  deactivate
