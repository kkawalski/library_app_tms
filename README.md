# library_app_tms

1. Создайте файла **.env** с параметрами из файла **.env.template**
2. Создайте базу данных, пользователя и пароль
3. Заполните переменную *DATABASE_URI* в файле **.env** с вышеуказанными данными
4. Создайте и активируйте вирутальное окружение
    > python -m venv env
    
    В случае если не сработает команда выше, используйте python**3**
    
    > python3 -m venv env

    Windows Powershell: 
    
    > .\env\Scripts\activate.ps1
    
    Windows Git Bash: 

    > source ./env/Scripts/activate
    
    Linux Bash: 
    
    > source ./env/bin/activate
5. Установите необходимые зависимости
    > pip install -r requirements.txt
6. Запускайте приложение
    > flask run