# FastAPI Blog


## How to set up:
- This project requires Python 3.6+ (I am currently running on 3.9.6)
- I recommend setting up a virtual environment before installing the requirements packages.
- To install requirements run:
```
pip install -r ./requirements.txt
```

## Code Tree
```
FastAPI
├─ blog
│  ├─ database.py
│  ├─ hashing.py
│  ├─ main.py
│  ├─ models.py
│  ├─ oauth2.py
│  ├─ repository
│  │  ├─ blogDriver.py
│  │  └─ userDriver.py
│  ├─ routers
│  │  ├─ authentication.py
│  │  ├─ blog.py
│  │  ├─ user.py
│  ├─ schemas.py
│  ├─ token.py
├─ blog.db
├─ README.md
└─ requirements.txt
```

## About the project
This project makes use of FastAPI to create an API for a basic blog web application. The focus is on setting up a backend for the blog app with future plan to add a web interface. Using FastAPI's IP/docs link all functionality has been tested and followed up with using Postman. Postman is optional and was primary used to track JWT authentication. 

### File Breakdown
- main.py -> Primary script that has been cleaned to contain the bare minimum through the use of routers. 
- blog.py -> Routes all blog url traffic to needed actions. Functionality stored in blogDriver.py
- user.py -> Routes all user url traffic to needed actions. Functionality stored in userDriver.py
- authentication.py -> Routes all login url traffic to needed actions.
- database.py -> Used to initailize the database.
- hashing.py -> Used for password encryption and password verfication. 
- models.py -> Used to set up tables for the blog and user elements.
- oauth2.py -> JWT token setup. 
- schemas.py -> Sets up response classes for user, blog, login, and token

