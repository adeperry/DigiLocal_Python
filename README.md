# DigiLocal Python

## Author @Ade-StapleHill

My DigiLocal Python exercises 

## Running

Top level directory contains file *requirements.txt* that lists Python modules to
pip3 install.
I use `python3 venv` to setup a virtual environment so that I know what modules need importing.

```
python3 -m venv env      # create subdir env to contain virtual env
source env/bin/activate  # start new enviroment
  pip3 install -r requirements.txt  # install Python modules
  ... do stuff
  deactivate            # exit from envioronment
```

Some of the Python files contain a companion `pytest` _test_ file, use `xvfb-run` if 
app uses an Xserver, e.g: `xvfb-run pytest`

## GitHub CI

To start GitHub testing, push to a branch and then select `New pull request`. If testing fails, simply push changes to the branch which triggers a retest. Once testing passed, select `Rebase and merge` to update master. For an example of a previous run, see details in [Snake game pull](https://github.com/adeperry/DigiLocal_Python/pull/2)

## Contents

* blue/PokeDex.py - simple check that use of Python pillow module is api compatible with
obsolete PIL. It appears to be compatible so Project Guide just needs import change.

* yellow/Snake_with_Classes.py - Check sanity `pytest` test file for `pygame`. Discovered needed to change Python version from 3.8 to 3.7 in GitHub action *.github/workflows/pythonapp.yml* 

