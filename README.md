# Flask Seed Project

Flask - Python web development framework Seed Project
This project doesn't include example of DB connection (mySQL or Mongo)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

All dependency listed [here](https://github.com/AndyTsangChun/py_seed_project/blob/master/requirements.txt)

```
pip install -r requirements.txt
```
Key dependency version:
Flask >= 0.12.2

### Usages
Example:
```
python app.py
```

The following will be shown if run sucessfully
```
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 325-691-956
```
Run the followings in a browser for three basic demo:
**Case 1**
Normal route for html templates
```
http://127.0.0.1:8000/
```
**Case 2**
Error Code handling
```
http://127.0.0.1:8000/abc
```
**Case 3**
Route with interaction with our python module
```
http://127.0.0.1:8000/requestCore
```

## Built With

* [Flask](http://flask.pocoo.org/) - A micro web framework written in Python.

## Change Log
Please check from [here](https://github.com/AndyTsangChun/py_seed_project/blob/master/CHANGELOG.md)

## Authors

* **Andy Tsang** - *Initial work* - [Personal Web](https://andytsangchun.github.io/)
