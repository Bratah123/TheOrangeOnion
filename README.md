# CSUFTheOnion
This repository houses the source code for the CSUF Onion Article website for CPSC 254, which publishes satirical news pertaining to California State University, Fullerton.

## Installation on Windows
*These instructions intended are for development on Windows machines only*

1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python -m venv venv` to create a virtual env for this project
4. Run command: `. venv/Scripts/activate` to activate the virtual environment
    - If you run into an error at this stage, refer to the next subsection on setting the execution policy
5. Run command: `pip install -r requirements.txt`

### Setting PowerShell's Execution Policy (Windows only)
1. Launch an administrative shell
    - Windows 11: Use the following key combinations: `Windows Key` + `X`, let go and then `A`
    - Windows 10: Search for `Windows PowerShell`, then right click and select `Run as administrator`
2. Run the command: `Get-ExecutionPolicy` to check the current execution policy 
3. If the policy is not set to `RemoteSigned`, run command: `Set-ExecutionPolicy RemoteSigned` and confirm when prompted
4. Repeat step 2 to check if policy has changed successfully

## Installation on Linux
1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python -m venv venv` to create a virtual env for this project
4. Run command: `source venv/Scripts/activate` to activate the virtual environment
    - If you run into an error at this stage, refer to the next subsection on setting the execution policy
5. Run command: `pip install -r requirements.txt`

### Setting Linux Execution Policy
1. Traverse to the project root directory
2. Run command `ls -l venv/Scripts/activate` to check if project has execution permissions if not go to step 3
3. Run command: `chmod +x venv/Scripts/activate`

## Run the Server
1. Run the command: `python src/wsgi.py` from the root directory
2. Go to the IP address listed in the console output on any web browser
    - At the time of writing, this should be [127.0.0.1:4040](http://127.0.0.1:4040)
    - Your mileage may vary as this is subject to change; always check the console output

## Acknowledgements
External Collaborators:
- [Amos Chua](https://github.com/KOOKIIEStudios)
    - Project Manager, Proofreader, DevOps
