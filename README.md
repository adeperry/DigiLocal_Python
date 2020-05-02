# DigiLocal Python

## Author @Ade-StapleHill

My DigiLocal Python exercises 

## Running

Top level directory contains file *requirements.txt* that lists Python modules to
pip3 install.
I use `python3 venv` to setup a virtual environment so that I know what modules need importing.

```
python3 -m venv env  # create subdir env to contain virtual env
source env/bin/activate  # start new enviroment
  pip3 install -r requirements.txt  # install Python modules
  ... do stuff
  deactivate    # exit from envioronment
```

Some of the Python files contain a pytest test file companion, use xvfb-run if 
app uses an Xserver, e.g: `xvfb-run pytest`

## Contents

* blue/PokeDex.py - simple check that use of Python pillow module is api compatible with
obsolete PIL. It appears to be compatible so Project Guide just needs import change.


