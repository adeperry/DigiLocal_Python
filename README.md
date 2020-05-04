# DigiLocal Python

## Author @Ade-StapleHill

My DigiLocal Python exercises. Check Python dependencies to be able to provide
pupils a requirements file that can be used with `pip` to install modules 
e.g. `pip3 install -r requirements.txt`

## Running

Top level directory contains file *requirements.txt* that lists Python modules to
pip3 install.
I use `python3 venv` to setup a virtual environment so that I know what modules need importing.

```
$ python3 -m venv env      # create subdir env to contain virtual env
$ source env/bin/activate  # start new enviroment
(env) pip3 install -r requirements.txt  # install Python modules
  ... do stuff
(env) deactivate            # exit from envioronment
```

Some of the Python files contain a companion `pytest` _test_ file, use `xvfb-run` if
 app uses an Xserver, e.g: `xvfb-run pytest`

## GitHub CI

To start GitHub testing, push to a branch and then select `New pull request`. If testing fails, simply push changes to the branch which triggers a retest. Once testing passed, select `Rebase and merge` to update master. For an example of a previous run, see details in [Snake game pull](https://github.com/adeperry/DigiLocal_Python/pull/2)

## Contents

* blue/PokeDex.py - simple check that use of Python *pillow* module is api compatible with
obsolete PIL which was installed on the club laptops. 
  * It appears to be compatible so no change is needed to the exercise instructions

* yellow/Snake_with_Classes.py - Check sanity `pytest` test file for `pygame`. 
  * *PAIN* if Python 3.8 is used, which is default in ubuntu 20.04 focal.
    * `pip3 install pygame` attempts to install *pygame==1.9.6* but fails in 3.8
    * `pip3 install pygame=2.0.0.dev6` installs ok however pygame `clock.tick()` framerate
    is much to quick even when changed to very small value e.g. 0.1
  * Change Python version from 3.8 to 3.7 in GitHub action *.github/workflows/pythonapp.yml*
  * To install Python 3.7 see [Installing Python 3.7 on Ubuntu with Apt](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)

```
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.7 python3.7-pip python3.7-venv python3.7-tk
$ python3.7 -m venv env_3.7
$ source env_3.7/bin/activate
(env_3.7) pip3.7 install -r requirements.txt
... do stuff
(env_3.7) deactivate
```