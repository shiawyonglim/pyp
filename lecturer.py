#import section
from datetime import datetime
from costum_functions import read_file, save_data, append_data


#file path declaration
student_file='./student.txt'
lect_module_file = './lec_modules.txt'
enrollments_file = './enrollments.txt'
grades_file = './grades.txt'
attendance_module_file = './attendance_modules.txt'
module_file = './module.txt'
attendance_file = './attendance.txt'



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

#check if grade is valid or not
def check_grade(grade):
    if grade.upper() in grade_to_gpa:
        return True
    else:
        print('please enter a valid grade')


#Check if student exists or not
def student_check(student_id):
    student = read_file(student_file)
    for s in student:
        if s[0] == student_id:
            print("Student ID is found")
            return student_id
            
    print("student not found")
           


#Check if module exists or correct
def module_check(module_code):
    module = read_file(module_file)
    for m in module:
        if m[0] == module_code:
            print("Module is found.You can proceed")
            return module_code
    print('Module not found')


#This function is to check if the module assigned to the lecturer
def assigned_module_check(lecturer_id,module_code):
    module_assigned = read_file(lect_module_file)
    for a in module_assigned:
        if a[0] == lecturer_id and a[1] == module_code:
            print("You are assigned to this module.")
            return lecturer_id, module_code
    print("You are not assigned to this module.")


#this function is to automatically make a attendance code
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
    student_list = read_file(enrollments_file)
    #check if module code there is a module code provided 
    if module_code == 0:
        view_assigned_modules(lecturer_id)
        module_code = module_check(input("Enter Module Code: "))
        assigned_module_check(lecturer_id, module_code)
    else:
        pass

    print(f'list of student who enrolled in {module_code}')
    #check if the student is enrolled by cjecking module code
    student_id_list = []
    for line in student_list:
        if line[1] == module_code:
            student_id_list.append(line[0])
    student_id_list.sort()
    student = read_file(student_file)
    j = 0
    #loop to print the student list
    for i in range(len(student_id_list)):
        for name in student:
            if name[0] == student_id_list[i]:
                print(f"{j+1}.{name[0]},{name[1]}")
                j += 1
    if student_id_list == []:
        print("No student is enrolled in this module")
        


#this function is to view the assigned modules
def view_assigned_modules(lecturer_id): # done check
    module = read_file(lect_module_file)
    module_name = read_file(module_file)
    module_code_list=[]
    #loop to get the module code
    for m in module:
        if m[0] == lecturer_id:
            module_code_list.append(m[1])

    #loop to print the assigned modules
    for i in range(len(module_code_list)):
        for m in module_name:
            if m[0] == module_code_list[i]:
                print(f"{i+1}. {m[0]}, {m[1]}")


#this function is to view the student grades
def view_grades(lecturer_id,module_code): # done
    grades=read_file(grades_file)
    #check is module code is already assinged
    lec_check = True
    if module_code == 0:
        view_assigned_modules(lecturer_id)
        module_code = module_check(input("Enter Module Code: "))
        lec_check = assigned_module_check(lecturer_id,module_code)
        print(lec_check)
    else: 
        pass
    if lec_check:
        print(f'list of student grade in {module_code}')
        student_grades = []
        #check lecturer and module code 
        for g in grades:
            if g[2] ==module_code and g[1] == lecturer_id:
                student_grades.append(g)
        i=0
        if student_grades == []:
            print("No grades found")
        else:
            #loop to print the grades
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
    print("grade added sucessfully")
    
#this function is to update the student grades
def update_grades(lecturer_id): #done
    grades = read_file(grades_file)
    module_code = module_check(input("Enter Module Code: "))
    assigned_module_check(lecturer_id,module_code)
    student_id = student_check(input("Enter Student ID: "))

    
    # Check if student is enrolled in this module
    for g in grades:
        if g[0] == student_id and g[1] == lecturer_id and g[2] == module_code:          
           print(g) 
           current_grade = g[3]
           break

    new_grade = input("Enter new grade: ")

    check_grade(new_grade)
    # Update grades.txt
    for i in range(len(grades)):
        if grades[i][0] == student_id and grades[i][1] == lecturer_id and grades[i][2] == module_code:
            grades[i][3] = new_grade
            break

    save_data(grades_file, grades)

    print("Grade updated successfully.")


#this function is to delete the student grades
def delete_grades(lecturer_id): #done    
    module_code = module_check(input("Enter Module Code: "))
    assigned_module_check(lecturer_id,module_code)
    student_id = input("Enter Student ID: ")

    with open(grades_file, "r") as file:
        lines = file.readlines()
        updated_lines = []
        #loop to remove the grade
        for line in lines:
            if student_id not in line:
                updated_lines.append(line)

    #doubble ocnfirm
    if len(updated_lines) < len(lines):
        with open(grades_file, "w") as file:
            file.writelines(updated_lines)
        print(f"Student with ID {student_id} removed.")
    else:
        print(f"No student with ID {student_id} found.")


    print("Grade deleted successfully.")



#this function is to mark attendance
def mark_attendance(lecturer_id):
    module = read_file(lect_module_file)
    attendance = read_file(attendance_file)
    attendance_module = read_file(attendance_module_file)
    enrollments = read_file(enrollments_file)

    module_code = module_check(input("Enter Module Code: "))
    assigned_module_check(lecturer_id, module_code)
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

    # find enrolled student
    student_id_list = [enrollment[0] for enrollment in enrollments if enrollment[1] == module_code]

    if not student_id_list:
        print("No students are enrolled in this module.")
        return

    print("Enrolled Students:")
    for i, student_id in enumerate(student_id_list, start=1):
        student_name = next((s[1] for s in enrollments if s[0] == student_id), "Unknown")
        print(f"{i}. {student_id} - {student_name}")

    view_student_list(lecturer_id, module_code)  
    
    #cannot add select student just now (fixed)
    #problem with attendance time(fixed)
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
        append_data(attendance_file, attendance)
    attendance_module=[]
    attendance_module.append([attendance_code, lecturer_id, module_code, class_start_time, class_end_time, class_type])
    append_data(attendance_module_file,attendance_code )

    print("Attendance marked successfully!")



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
        print('8. delete attendance')
        print("9. Logout")
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
        elif choice =='8':
            break
        else:
            print("Invalid choice")