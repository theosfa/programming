from login import get_login_name
import json

global file_name
file_name = "login_password.json"

def inputLogin():
    first = input('Podaj imię: ')
    last = input('Podaj nazwisko: ')
    idnumber = input('Podaj numer albumu: ')
    print('Twoja nazwa użytkownika to:')
    login = get_login_name(first, last, idnumber)
    return login

def create_login():
    login = inputLogin()
    while check_if_login_exists(login):
        login = inputLogin()
    print(login)
    password = input('Podaj hasło: ')
    write_login(login, password)

def log_in():
    login = input("Podaj login: ")
    if check_if_login_exists(login):
        password = input('Podaj hasło: ')
        check_pass = read_password(login)
        if password == check_pass:
            print("Log in succesfully")
        else:
            print("Password is incorrect")
    else:
        print("Such user doesn't exist")

def write_login(login, password):
    file = open(file_name, "r")
    login_matrix = json.loads(file.read())
    file.close()
    login_matrix[login] = password
    file = open(file_name, "w")
    file.write(json.dumps(login_matrix))
    file.close()

def read_password(login):
    file = open(file_name, "r")
    login_matrix = json.loads(file.read())
    file.close()
    return login_matrix[login]

def check_if_login_exists(login):
    file = open(file_name, "r")
    login_matrix = json.loads(file.read())
    file.close()
    if login in login_matrix:
        return True
    else:
        return False

def main():
    try:
        file = open(file_name, "r")
        file.close()
    except Exception as e:
        login_matrix = {}
        file = open(file_name, "w")
        file.write(json.dumps(login_matrix))
        file.close()
    exit = False
    while not exit:
        print("1. Login")
        print("2. Create login")
        print("3. Exit")
        answer = int(input("Input your choice: "))
        if answer == 1:
            log_in()
        elif answer == 2:
            create_login()
        else:
            exit = True


if __name__ == '__main__':
    main()
