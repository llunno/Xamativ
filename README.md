![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?logo=sqlite&logoColor=white)

# Running dev server
To develop - run `uvicorn main:app --reload --host 127.0.0.1 --port 80` to get a development server with a reloader

# Running prod server
Run `uvicorn main:app --host 127.0.0.1 --port 80`. This will run the server in a production environment.

To upload to production, remember to change the `host` and `port` to the correct values, matching the production environment.
