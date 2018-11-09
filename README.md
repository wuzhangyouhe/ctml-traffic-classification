# Pre-requisite:

## Installation for python 2.7 and django in ubuntu 16
```
$ sudo apt-get update
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```
## MacOS user can use brew instead of apt-get
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python
```
## Installation for pip tool for python library
```
$ sudo apt-get install curl
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ sudo python get-pip.py
$ sudo apt-get install python-tk
$ sudo pip install django==1.10
$ sudo pip install numpy
$ sudo pip install pandas
$ sudo pip install SciPy
$ sudo pip install scikit-learn
$ sudo pip install matplotlib
$ sudo pip install djangorestframework
$ sudo apt-get install git
```
## After installation you will see 
```
liutao@ubuntu:~$ python -m django --version
1.11.6
```
Get the Django framwork :
```
git clone https://gitlab.com/wuzhangyouhe/CTML.git
cd CTML
```
Enable WebUI from Django:
```
$ python manage.py runserver
$ python manage.py migrate
```
Then access WebUI via http://127.0.0.1:8000/