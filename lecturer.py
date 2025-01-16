from datetime import datetime
from costum_functions import read_file, save_data, append_data

student_file='./student.txt'
lect_module_file = './lecturer_module.txt'
enrollments_file = './enrollments.txt'
grades_file = './grades.txt'


grade_to_gpa = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'E': 0.0,
    'F': 0.0
}

def check_grade(grade):
    if grade.upper() in grade_to_gpa:
        return True
    else:
        print('please enter a valid grade')
        return False

#Check if student exists or correct
def student_check(student_id):
    student = read_file('student.txt')
    for s in student:
        if s[0] == student_id:
            print("Student ID is found")
            return student_id
            
    print("student not found")
    return
           


#Check if module exists or correct
def module_check(module_code):
    module = read_file('module.txt')
    for m in module:
        if m[0] == module_code:
            print("Module is found.You can proceed")
            return module_code
    print('Module not found')
#This function is to check if the module assigned to the lecturer

def assigned_module_check(lecturer_id,module_code):
    module_assigned = read_file('lec_modules.txt')
    for a in module_assigned:
        if a[0] == lecturer_id and a[1] == module_code:
            print("You are assigned to this module.")
            return lecturer_id, module_code
    print("You are not assigned to this module.")

def auto_attendance(last_attendance_code,student_number):
    first_alphabet = last_attendance_code[0]
    number= int(last_attendance_code[1:])
    attendance_list=[]
    for i in range(student_number):
        number +=1 
        attendance_code = first_alphabet + str(number)
        attendance_list.append([])





#this function is to view the student list
def view_student_list(lecturer_id, module_code): # done checking
    student_list = read_file('enrollments.txt')
    if module_code == 0:
        view_assigned_modules(lecturer_id)
        # Check if module exists or correct
        module_code = module_check(input("Enter Module Code: "))
        #Check if module is assigned to lecturer
        assigned_module_check(lecturer_id, module_code)
    else:
        pass
    print(f'list of student who enrolled in {module_code}')
    student_id_list = []
    for line in student_list:
        if line[1] == module_code:
            student_id_list.append(line[0])
    student_id_list.sort()
    student = read_file('student.txt')
    j = 0
    for i in range(len(student_id_list)):
        for name in student:
            if name[0] == student_id_list[i]:
                print(f"{j+1}.{name[0]},{name[1]}")
                j += 1
    if student_id_list == []:
        print("No student is enrolled in this module")

#this function is to view the assigned modules
def view_assigned_modules(lecturer_id): # done no problem
    module = read_file('lec_modules.txt')
    module_name = read_file("module.txt")
    module_code_list=[]
    for m in module:
        if m[0] == lecturer_id:
            module_code_list.append(m[1])

    for i in range(len(module_code_list)):
        for m in module_name:
            # if function cant run
            if m[0] == module_code_list[i]:
                print(f"{i+1}. {m[0]}={m[1]}")


#this function is to view the student grades
def view_grades(lecturer_id,module_code): # done
    grades=read_file(grades_file)
    if module_code == 0:
        view_assigned_modules(lecturer_id)
        # Get module code
        module_code = module_check(input("Enter Module Code: "))
        # Check if module assigned to the lecturer(PROBLEM)
        assigned_module_check(lecturer_id,module_code)
    else: 
        pass
    print(f'list of student grade in {module_code}')
    student_grades = []
    for g in grades:
        if g[2] ==module_code and g[1] == lecturer_id:
            student_grades.append(g)
    i=0
    if student_grades == []:
        print("No grades found")
    else:
        for grade in student_grades:
            print(f"{i+1 }.StudentID= {grade[0]}, Grade= {grade[3]}")
            i += 1
    
#this function is to add the student grades
def add_grades(lecturer_id): # done
    view_assigned_modules(lecturer_id)
    module_code = module_check(input("Enter Module Code: "))
    assigned_module_check(lecturer_id, module_code)
    print('')
    view_student_list(lecturer_id,module_code)
    view_grades(lecturer_id,module_code)
    student_id = student_check(input("Enter Student ID: "))
    
    # Check if student is enrolled in this module
    enrollments = read_file(enrollments_file)
    found = False
    for e in enrollments:
        if e[0] == student_id and e[1] == module_code:
            found = True
            break
    if not found:
        print(f"Student with ID {student_id} is not enrolled in module {module_code}")
        return

    # Check if student already has a grade for the module
    grades =read_file(grades_file)
    for g in grades:
        if g[0] == student_id and g[1] == lecturer_id and g[2] == module_code:
            print(f"Student with ID {student_id} already has a grade for this module. Do you want to update the grade?")
            update_choice = input("Enter 'y' to update, 'n' to cancel: ")
            if update_choice == 'y':
                update_grades(lecturer_id)
                return
            elif update_choice == 'n':
                return
            else:
                return
    grade = input("Enter grade: ") 
    check_grade(grade)
    # Add grade to file 
    grades= []

    grades.append([student_id, lecturer_id, module_code, grade])
    append_data(grades_file, grades)
#this function is to update the student grades

    
def update_grades(lecturer_id): #done
    grades = read_file(grades_file)

    module_code = module_check(input("Enter Module Code: "))

    assigned_module_check(lecturer_id,module_code)

    student_id = student_check(input("Enter Student ID: "))

    for g in grades:
        if g[0] == student_id and g[1] == lecturer_id and g[2] == module_code:          
           print(g) 
           current_grade = g[3]
           break

    new_grade = input("Enter new grade: ")

    # Update grades.txt
    for i in range(len(grades)):
        if grades[i][0] == student_id and grades[i][1] == lecturer_id and grades[i][2] == module_code:
            grades[i][3] = new_grade
            break

    save_data('grades.txt', grades)

    print("Grade updated successfully.")


#this function is to delete the student grades
def delete_grades(lecturer_id): #done    
    module_code = module_check(input("Enter Module Code: "))

    assigned_module_check(lecturer_id,module_code)

    student_id = input("Enter Student ID: ")

    with open('grades.txt', "r") as file:
        lines = file.readlines()
        updated_lines = []
        for line in lines:
            if student_id not in line:
                updated_lines.append(line)

    if len(updated_lines) < len(lines):
        with open('grades.txt', "w") as file:
            file.writelines(updated_lines)
        print(f"Student with ID {student_id} removed.")
    else:
        print(f"No student with ID {student_id} found.")


    print("Grade deleted successfully.")



#this function is to mark attendance




def mark_attendance(lecturer_id):
    module = read_file('lec_modules.txt')
    attendance = read_file('attendance.txt')
    attendance_module = read_file("attendance_module.txt")
    enrollments = read_file('enrollments.txt')

    # Check module code validity
    module_code = module_check(input("Enter Module Code: "))
    assigned_module_check(lecturer_id, module_code)

    # Class time inputs
    class_start_time = input("Enter class start time in HH:MM: ")
    class_end_time = input("Enter class end time in HH:MM: ")

    # Choose class type
    while True:
        choice = input("1. Tutorial... Enter {T}\n2. Lecture... Enter {L}\n")
        if choice.upper() == "T":
            class_type = "Tutorial"
            break
        elif choice.upper() == "L":
            class_type = "Lecture"
            break
        else:
            print("Invalid choice. Please enter 'T' or 'L'.")

    # Get students enrolled in the module
    student_id_list = [enrollment[0] for enrollment in enrollments if enrollment[1] == module_code]

    if not student_id_list:
        print("No students are enrolled in this module.")
        return

    # Display student list
    print("Enrolled Students:")
    for i, student_id in enumerate(student_id_list, start=1):
        student_name = next((s[1] for s in enrollments if s[0] == student_id), "Unknown")
        print(f"{i}. {student_id} - {student_name}")

    view_student_list(lecturer_id, module_code)  # Additional functionality, assuming it's defined

    # Mark attendance for selected students
    mark_student_indices = input("Choose the numbers of the students to mark attendance for (e.g., 1 2 3): ").split()
    try:
        selected_students = [student_id_list[int(i) - 1] for i in mark_student_indices]
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid student numbers.")
        return
    
    # Generate new attendance code
    if attendance_module:
        last_attendance_code = attendance_module[-1][0]
        first_alphabet = last_attendance_code[0]
        number = int(last_attendance_code[1:]) + 1
        attendance_code = first_alphabet + str(number)
    else:
        attendance_code = "A1" 

    attendance_date = datetime.now().strftime("%Y-%m-%d")
    attendance_time = datetime.now().strftime("%H:%M:%S")

    # Save attendance
    for student_id in selected_students:
        attendance.append([student_id, attendance_code, attendance_date, attendance_time])
        append_data("attendance.txt", attendance)
    attendance_module=[]
    attendance_module.append([attendance_code, lecturer_id, module_code, class_start_time, class_end_time, class_type])
    append_data("attendance_module.txt",attendance_code )

    print("Attendance marked successfully!")





def delete_attendance(lecturer_id): #done
    attendance_code = input('enter attendance code: ')
    student_id = input("Enter Student ID: ")

    with open('attendance.txt', "r") as file:
        lines = file.readlines()
        updated_lines = []
        for line in lines:
            if student_id not in line and attendance_code not in line:
                updated_lines.append(line)

    if len(updated_lines) < len(lines):
        with open('attendance.txt', "w") as file:
            file.writelines(updated_lines)
        print(f"Student with ID {student_id} removed.")
    else:
        print(f"No student with ID {student_id} found.")

def update_attendance(lecturer_id):

    view_student_list(lecturer_id,0)
    attendance = read_file('attendance.txt')


    attendance_code = input('enter attendance code: ')
    student_id = input("Enter module ID: ")

    mark_student = input("Choose the number of the student you want to mark attendance for: ").split()

    attendance_date = datetime.now().strftime("%x")
    attendance_time = datetime.now().strftime("%X")

    for i in mark_student:
        student_id = student_id_list[int(i)-1]
        attendance_time_taken = (attendance_date , attendance_time)
        append_data("attendance.txt", [[student_id,attendance_code,attendance_time_taken]])



#lecturer menu part
def lecturer_menu(lecturer_id):
    while True:
        print("\nLecturer Menu:")
        print("1. View Student List")
        print("2. View Assigned Modules")
        print("3. View Student Grade")
        print("4. Add Student Grade")
        print("5. Update Student Grade")
        print("6. Delete Student Gradee")
        print("7. Mark Attendancee")
        print("8. Update Attendance")
        print('9. delete attendance')
        print("10. Logout")

        choice = input("Enter choice: ")

        #choose that they want to do part
        if choice == '1':
            view_student_list(lecturer_id,0)
        elif choice == '2':
            view_assigned_modules(lecturer_id)
        elif choice == '3':
            view_grades(lecturer_id,0)
        elif choice == '4':
            add_grades(lecturer_id)
        elif choice == '5':
            update_grades(lecturer_id)
        elif choice == '6':
            delete_grades(lecturer_id)
        elif choice == '7':
            mark_attendance(lecturer_id)
        elif choice == '8':
            update_attendance(lecturer_id)
        elif choice == '9':
            delete_attendance(lecturer_id)
        elif choice=='10':
            break
        else:
            print("Invalid choice")