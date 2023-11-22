# CSUFTheOnion
This repository houses the source code for the CSUF Onion Article website for CPSC 254, which publishes satirical news pertaining to California State University, Fullerton.

## Tech Stack
The Orange Onion is a Flask application styled using Bootstrap (served via CDN), and uses a SQLite embedded database.  
This project targets Python 3.10+, and assumes that you already have that added to PATH.

It uses Flask's built-in developmental WSGI server (powered by Werkzeug), as details pertaining to deployment in a production environment is beyond the scope of this project. Anyone who wishes to host a production version should consider a production-ready WSGI server like Waitress instead.

While development is mainly done using x86_64 machines running Windows, the proof-of-concept demo website is hosted on an x86_64 machine running Ubuntu Server 22.04, so the instructions in the following sections will focus mainly on these 2 environments.

## Installation on Windows
*These instructions intended are for development on Windows machines only*

1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python -m venv venv` to create a virtual env for this project
4. Run command: `. venv/Scripts/activate` to activate the virtual environment
    - If you run into an error at this stage, refer to the next subsection on setting the execution policy
5. Run command: `pip install -r requirements.txt`
    - You may use the command `deactivate` to exit from the virtual environment after this
6. Run command: `venv/Scripts/python src/db/init_db.py` to initialize the database

### Setting PowerShell's Execution Policy
1. Launch an administrative shell
    - Windows 11: Use the following key combinations: `Windows Key` + `X`, let go and then `A`
    - Windows 10: Search for `Windows PowerShell`, then right click and select `Run as administrator`
2. Run the command: `Get-ExecutionPolicy` to check the current execution policy 
3. If the policy is not set to `RemoteSigned`, run command: `Set-ExecutionPolicy RemoteSigned` and confirm when prompted
4. Repeat step 2 to check if policy has changed successfully

## Installation on Linux
1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python3 -m venv venv` to create a virtual env for this project
4. Run command: `source venv/bin/activate` to activate and enter the virtual environment
5. Run command: `venv/bin/pip3 install -r requirements.txt`
    - You may use the command `deactivate` to exit from the virtual environment after this
6. Run command: `venv/bin/python3 src/db/init_db.py` to initialize the database

## Run the Server
1. Run the following command from the project root directory:
    - Windows: `venv/Scripts/python src/wsgi.py`
    - Linux: `venv/bin/python3 src/wsgi.py`

2. Go to the IP address listed in the console output on any web browser
    - At the time of writing, this should be [127.0.0.1:4040](http://127.0.0.1:4040)
    - Your mileage may vary as this is subject to change; always check the console output

## Acknowledgements
External Collaborators:
- [Amos Chua](https://github.com/KOOKIIEStudios)
    - Project Manager, Proofreader
