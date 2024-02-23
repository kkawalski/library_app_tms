# library_app_tms

1. Create file **.env** with parameters from **.env.template**
2. Create database, role and password
3. Fill *DATABASE_URI* variable in **.env** file with the above credentials
4. Create and activate virtual environment
    > python -m venv env
    
    Or
    
    > python3 -m venv env

    Windows Powershell: 
    
    > .\env\Scripts\activate.ps1
    
    Windows Git Bash: 

    > source ./env/Scripts/activate
    
    Linux Bash: 
    
    > source ./env/bin/activate
5. Install required packages
    > pip install -r requirements.txt
6. Run application
    > flask run