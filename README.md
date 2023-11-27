# The Orange Onion
This repository houses the source code for the The Orange Onion Article website for CPSC 254, which publishes satirical news pertaining to California State University, Fullerton.
The name is a combination of one of the school's (CSUF) official colors and The Onion, a satirical news network.

## Tech Stack
The Orange Onion is a Flask application styled using Bootstrap (served via CDN), and uses an SQLite embedded database.  
This project targets Python 3.10+, and assumes that you already have that added to PATH.

It uses Flask's built-in developmental WSGI server (powered by Werkzeug), as details pertaining to deployment in a production environment is beyond the scope of this project. Anyone who wishes to host a production version should consider a production-ready WSGI server like Waitress instead.

While development is mainly done using x86_64 machines running Windows, the proof-of-concept demo website is hosted on an x86_64 machine running Ubuntu Server 22.04, so the instructions in the following sections will focus mainly on these 2 environments.

## Installation on Windows
*These instructions intended are for development on Windows machines only*

1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python -m venv venv` to create a virtual env for this project
4. Run command: `venv/Scripts/pip install -r requirements.txt`
5. Run command: `venv/Scripts/python src/db/init_db.py` to initialize the database
6. Run command: `venv/Scripts/python src/db/init_db_data.py` to initialize some starter data to database

### Setting PowerShell's Execution Policy
If you run into errors regarding PowerShell execution policy, try the following:

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
5. Run command: `venv/bin/pip3 install -r requirements.txt`
6. Run command: `venv/bin/python3 src/db/init_db.py` to initialize the database
7. Run command: `venv/bin/python3 src/db/init_db_data.py` to initialize some starter data to database

## Gallery

![image](https://github.com/Bratah123/TheOrangeOnion/assets/58405975/90f697bd-1355-4375-b108-e8192d6ffca1)
![image](https://github.com/Bratah123/TheOrangeOnion/assets/58405975/c99ae6c4-d92d-42b7-9e5d-f0e256dd4657)
![image](https://github.com/Bratah123/TheOrangeOnion/assets/58405975/fb141fc8-08fc-4031-9b82-c602b2c558aa)
![image](https://github.com/Bratah123/TheOrangeOnion/assets/58405975/90095d83-a00f-4950-b3dc-b2029276ccd1)

## Run the Server (localhost - for development)
1. Run the following command from the project root directory:
    - Windows: `venv/Scripts/python src/wsgi.py`
    - Linux: `venv/bin/python3 src/wsgi.py`

2. Go to the IP address listed in the console output on any web browser
    - At the time of writing, this should be [127.0.0.1:4040](http://127.0.0.1:4040)
    - Your mileage may vary as this is subject to change; always check the console output

## Authors
- Back-end: [Brandon Nguyen](https://github.com/Bratah123)
- Front-end: [Garret Feng](https://github.com/thebluehomosapien)
- Documentation: [Tung Nguyen](https://github.com/Ragnaorok)
