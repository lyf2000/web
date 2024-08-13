### Prepare

Setup venv: `python -m venv venv`
Install dependencies: `pip install -r reqs.txt`


### Launch

Start up backend: `python -m uvicorn main:app --host 0.0.0.0 --port 80 --reload --reload-include \*.py`
