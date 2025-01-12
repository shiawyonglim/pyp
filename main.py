from datetime import datetime
from registrar import registrar_menu
from student import student_menu
from accountant import accountant_menu
from lecturer import update
from admin import add_new_lecturer, admin

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(',') for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_data(filename, data):
    # Open the file for writing
    with open(filename, "w") as file:
        # Write the data to the file
        for item in data:
            file.write(item + "\n")

# this function is to add the data into the file
def append_data(filename, data):
    with open(filename, 'a') as file:
        for item in data:
            file.write(",".join(str(x) for x in item) + "\n")

#login using the role the user choose 
def login(role):
    while True:
        id = input(f"please input your {role}id: ")
        password = input("Password: ")
        user = read_file(role + '_login.txt')

        for user in user:
            if user[0] == id and user[1] == password:
                return user[0]
        print("Invalid credentials. Try again.")


#main menu of the whole system
def main():
    print("Welcome to University Management System")
    while True:
        print('''
1. Admin
2. Lecturer
3. Student
4. Registrar
5. accountant
6. Exit
        ''')
        choice = input("Enter choice: ")

        #chossin role so to login
        if choice == '1':
            login('Admin')
            admin()
        elif choice == '2':
            login('Lecturer')
            lecturer_menu()
        elif choice == '3':
            student_id = login('Student')
            student_menu(student_id)
        elif choice == '4':
            login('Registrar')
            registrar_menu()
        elif choice == '5':
            login('Accountant')
            accountant_menu()
        elif choice == '6':
            print("Thank you for using University Management System")
            break
        else:
            print("Invalid choice")


main()
