
#import section
from datetime import datetime
from costum_functions import read_file, save_data , append_data
import random


#file part declaration
student_file = "./student.txt"
course_file = "./course.txt"
enrollment_file = "./enrollments.txt"
grade_file = "./grades.txt"
module_file = "./module.txt"
attendance_file = "./attendance.txt"
attendance_module_file = "./attendance_modules.txt"
outstanding_file = "./outstanding.txt"
student_login_file = "./Student_login.txt"
lect_module_file = "./lec_modules.txt"
student_module = "./std_module.txt"



#view modules section
def view_available_modules():    
    modules = read_file(module_file)
    print("\nAvailable Modules:")
    
    #loop through the module and print every module
    for module in modules:
        print(f"Code: {module[0]}, Name: {module[1]}, Credits: {module[2]}")




#enroll module part
def enroll_module(student_id):
    # Check if student has already enrolled in any module
    courses = read_file(module_file)
    enrollments = read_file(enrollment_file)
    enrolled_courses = [e[1] for e in enrollments if e[0] == student_id]

    # Display only modules that they are not enrooled in
    print("\nAvailable Modules:")
    for course in courses:
        if course[0] not in enrolled_courses:
            print(f"Code: {course[0]}, Name: {course[1]}, Credits: {course[2]}")

    course_code = input("Enter module code to enroll: ")

    # Check if course exists
    if not any(c[0] == course_code for c in courses):
        print("Course not found")
        return

    #finding lect to teach the module
    lecturers_module = read_file(lect_module_file)
    module_lecturers = [l for l in lecturers_module if l[1] == course_code]
    if module_lecturers:
        lecturer_id = random.choice(module_lecturers)[0]

        
        std_module = read_file(student_module)
        std_module.append([student_id, course_code, lecturer_id])
        append_data(student_module, std_module)
    else:
        print("No lecturer found for this module.")
        return
        
    # Check if already enrolled
    enrollments = read_file(enrollment_file)
    if any(e[0] == student_id and e[1] == course_code for e in enrollments):
        print("Already enrolled in this module")
        return

    # Add student enrollments
    enrollments.append(
        [student_id, course_code,datetime.now().strftime('%Y-%m-%d')])
    append_data(enrollment_file, enrollments)
    print("Successfully enrolled in course")      


#view grades part
def view_grades(student_id):
    grades = read_file(grade_file)
    cgpa = 0.0
    course_count = 0

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
    students = read_file(student_file)
    #check student
    if not any(s[0] == student_id for s in students):
        print("Student not found.")
        return

    # get grades for the student
    grades = read_file(grade_file)
    student_grades = [g for g in grades if g[0] == student_id]
    if not student_grades:
        print("No grades found for the student.")
        return

    #print out grades
    print(f"Grades for student {student_id}:")
    for grade in student_grades:
        course_name, grade_value = grade[2], grade[3]
        gpa = grade_to_gpa.get(grade_value, 0.0)
        course_count += 1
        cgpa += gpa
        print(f"  - {course_name}: {grade_value} (GPA: {gpa})")

    #calculation for grade
    if course_count > 0:
        average_gpa = cgpa / course_count
        print(f"Average GPA: {average_gpa:.2f}")
    else:
        print("No grades found for the student.")




#view attendance part
def view_attendance(student_id):
    attendance = read_file(attendance_file) 
    #check studetn
    student_attendance = [record for record in attendance if record[0] == student_id]

    if not student_attendance:
        print("No attendance records found")
        return
    
    for attendance_record in student_attendance:
        # get attendance details
        attendance_code = attendance_record[1] 
        attendance_status = attendance_record[2]  
        timestamp = attendance_record[3]  

        attendance_module = read_file(attendance_module_file)  
        module_record = next((m for m in attendance_module if m[0] == attendance_code), None)

        if module_record:
            lecturer_id = module_record[1]  
            module_code = module_record[2]  
            # Print attendance details with module information
            print(f"Module: {module_code}, Attendance: {attendance_status}, Time: {timestamp}, Lecturer ID: {lecturer_id}")
        else:
            print("no attendance record found")



#unenroll module part
def unenroll_module(student_id):
    # show currently enrolled modules
    view_enrolled_module(student_id)
    course_code = input("Enter course code to unenroll: ")
    enrollments = read_file(enrollment_file)
    
    # find the enrollment record of the student and
    updated_enrollments = [
        e for e in enrollments
        if not (e[0] == student_id and e[1] == course_code)
    ]

    # check if student is not enroll 
    if len(updated_enrollments) == len(enrollments):
        print("Not enrolled in this course")
        return

    save_data(enrollment_file, [",".join(e) for e in updated_enrollments])
    print("Successfully unenrolled from course")




#add student view fees 
def view_outstanding_fees(student_id):
    fees = read_file(outstanding_file)
    student_fees = [f for f in fees if f[0] == student_id]

    if not student_fees:
        print("No fees found")
        return

    for fee in student_fees:
        print(f"StudentID: {fee[0]}, Amount: {fee[1]}")

#view enrolled module part
def view_enrolled_module(student_id):
    enrollments = read_file(enrollment_file)
    enrolled_courses = [e for e in enrollments if e[0] == student_id]

    if not enrolled_courses:
        print("No enrolled courses found")
        return

    for course in enrolled_courses:
        print(f"Course Code: {course[1]}, Enrollment Date: {course[2]}")

#change passwrod part
def change_password(studentid):
    current_password = input("Enter your current password: ")
    students = read_file(student_login_file)
    
    for i, student in enumerate(students):
        #check student password and id first
        if student[0] == studentid and student[1] == current_password:
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")
            #check if new password and confirm password are same and then change password
            if new_password == confirm_password:
                students[i][1] = new_password
                save_data(student_login_file, [",".join(s) for s in students])
                print("Password changed successfully")
                return
            else:
                print("Passwords do not match")
                return
    print("Invalid current password")
    
#student menu part
def student_menu(student_id):
    while True:
        print("\nStudent Menu:")
        print("1. View Available Modules")
        print("2. Enroll in Module")
        print("3. View Grades")
        print("4. Access Attendance Record")
        print("5. Unenroll from Module")
        print("6. View outstanding fees")
        print("7. View enrroled module")
        print("8. Change password")
        print("9. Logout")
        choice = input("Enter choice: ")
        #choose that they want to do part
        if choice == '1':
            view_available_modules()
        elif choice == '2':
            enroll_module(student_id)
        elif choice == '3':
            view_grades(student_id)
        elif choice == '4':
            view_attendance(student_id)
        elif choice == '5':
            unenroll_module(student_id)
        elif choice == '6':
            view_outstanding_fees(student_id)   
        elif choice == '7':
            view_enrolled_module(student_id)
        elif choice == '8':
            change_password(student_id)
        elif choice == '9':
            break
        else:
            print("Invalid choice")