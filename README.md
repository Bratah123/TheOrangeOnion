# CSUFTheOnion
CSUF Onion Article website for CPSC 254 specializing in satire news related to Califonia State University, Fullerton.

# Installation
Do note that these instructions apply to Windows Machine for Development Reasons.

1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python -m venv venv` to create a virtual env for this project.
4. Run command: `. venv/Scripts/activate` to activate the virtual environment.
5. Run command: `pip install -r requirements.txt`

# Installation on Linux
1. `git clone` the repository
2. Traverse to the project root directory
3. Run command: `python -m venv venv` to create a virtual env for this project.
4. Run command: `source venv/Scripts/activate` to activate the virtual environment.
5. Run command: `pip install -r requirements.txt`

# Run the Server
1. Run the command: `python src/wsgi.py` from the root directory.
2. go to [127.0.0.1:4040](http://127.0.0.1:4040) on any web browser.
   
# Setting PowerShell's Execution Policy
1. Right-click on the PowerShell icon and select "Run as Administrator."
2. run command: 'Get-ExecutionPolicy' to check the current execution policy 
3. if the policy is not 'RemoteSigned', run command: 'Set-ExecutionPolicy RemoteSigned' and confirm when prompted
5. repeat step 2 to check if policy has changed

# Setting Linux Execution Policy
1. Traverse to the project root directory
2. eun command 'ls -l venv/Scripts/activate' to check if project has execution permissions if not go to step 3
3. run command: 'chmod +x venv/Scripts/activate'




