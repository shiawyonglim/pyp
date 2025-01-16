#all done checking waiting for change

from student import enroll_module, view_grades



student_file = "./student.txt"
course_file = "./course.txt"
enrollment_file = "./enrollments.txt"
grade_file = "./grades.txt"
oustanding_file = "./outstanding.txt"

def register_new_student(): #done checking
    print("Registering a new student...")
    student_id = input("Enter Student ID: ")
    with open(student_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if student_id == line[0]:
                print("The Student ID is already recorded.")
                return register_new_student()
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    contact_information = input("Enter your Contact Information: ")
    student_pass= (student_id+'@'+course)

    student = {
        "Student ID": student_id,
        "Student Name": student_name,
        "Course": course,
        "Contact Information": contact_information,
        "Student password": student_pass
    }

    with open(student_file, "a") as file:
        file.write(f"{student['Student ID']},{student['Student Name']},{student['Course']},{student['Contact Information']}\n")
        
    with open('Student_login.txt', "a") as file:
        file.write(f"{student['Student ID']},{student['Student password']}\n")
    
    with open(course_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if student['Course'] == line.split(",")[0]:
                outstanding_status = line.split(",")[2].strip()
                with open(oustanding_file, "a") as file:
                    file.write(f"{student['Student ID']},{outstanding_status}\n")
                break
    print("Register New Student Successfully.")


def remove_student(): #done checking
    print ("--- Remove student ---")
    print("-" * 100)
    print("Student data review - Student ID, Name, Phone Number, Register date, Course Code, Facaulty Code")
    print("-" * 100)
    try:
        with open(student_file, "r") as file:
            lines = file.readlines()
        if not lines:
            print("\nNo data found.\n")
        else:
            for line in lines:
                print (line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{student_file}' was not found.")
        
    student_id = input("Enter Student ID that needs to be removed: ")

    try:
        with open(student_file, "r") as file:
            lines = file.readlines()
            updated_lines = []
            for line in lines:
                if student_id not in line:
                    updated_lines.append(line)

        if len(updated_lines) < len(lines):
            with open(student_file, "w") as file:
                file.writelines(updated_lines)
            print(f"Student with ID {student_id} removed.")
        else:
            print(f"No student with ID {student_id} found.")

    except FileNotFoundError:
        print("Student file not found.")


def update_student_record(): #done checking but waitng for update
    student_id = input("Enter Student ID that needs to be changed: ").strip()
    found = False

    try:
        with open(student_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")  # Split line into fields
                if len(data) >= 2 and data[1].strip() == student_id:  # Exact match for student ID
                    found = True
                    print(f"Match found: {line.strip()}")
                    # Proceed with update logic
                    while True:
                        print("------------------------------------")
                        print("1. Update program")
                        print("2. Update Student's contact information")
                        print("3. Back to main menu")
                        choice = input("Please enter the selection you need to update: ")

                        if choice == "1":
                            new_program = input("Enter new program: ")
                            if not new_program.isalpha():
                                print("Invalid program. Please enter letters only.")
                                continue

                            updated_lines = []
                            updated_lines1 = []
                            for line in lines:
                                fields = line.strip().split(",")
                                if len(fields) >= 3 and fields[1] == student_id:
                                    # Replace the line with updated content
                                    fields[2] = new_program
                                    updated_line = ",".join(fields) + "\n"
                                    updated_lines.append(updated_line)
                                    updated_line1 = ",".join(fields) + "\n"
                                    updated_lines1.append(updated_line1)
                                    line_found = True
                                    print(f"Updated program for student ID {student_id}.")
                                else:
                                    # Keep other lines unchanged
                                    updated_lines.append(line)
                                    updated_lines1.append(line)

                            if line_found:
                                # Rewrite the file with updated content
                                with open(course_file, "w") as file:
                                    file.writelines(updated_lines)
                                with open(student_file,"w") as file1:
                                    file1.writelines(updated_lines1)
                            else:
                                print(f"No matching student ID {student_id} found.")

                        elif choice == "2":
                            contact_info = input(
                                "Enter Student's contact information: ")
                            if contact_info in [line.strip() for line in lines]:
                                print("The student's contact information is already recorded.")
                            else:
                                print("Contact information updated successfully.")
                            student = {"Contact info": contact_info}
                            with open(student_file, "a") as file:
                                file.write(f"{student['Contact info']}\n")
                        elif choice == "3":
                            return
                        else:
                            print("Invalid choice. Please try again.")
                            break
    except FileNotFoundError:
        print("Student file not found.")
        open(student_file, "x")
        return

    if not found:
        print("Student not found.")


def manage_enrolment():#done checking
    student_id = input("Enter Student ID that needed to be changed: ")
    found = False

    try:
        with open(student_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if student_id in line:
                    found = True
                    while True:
                        print("------------------------------------ ")
                        print("1. Student Module Registration")
                        print("2. Updating Module Information")
                        print("3. Back to main menu")
                        choice = input(
                            "Please enter the selection you need to manage: ")

                        if choice == "1":
                            enroll_module(student_id)
                            
                        elif choice == "2":
                            module_name = input(
                                "Enter the module name to update: ")
                            new_module_info = input(
                                "Enter the new module name: ")
                        
                            updated = False
                            with open(enrollment_file, "r") as file:
                                lines = file.readlines()

                            with open(enrollment_file, "w") as file:
                                for line in lines:
                                    if line.startswith(
                                            f"{student_id},{module_name}"):
                                        file.write(
                                            line.replace(
                                                module_name, new_module_info))
                                        updated = True
                                    else:
                                        file.write(line)

                            if updated:
                                print(
                                    f"Module '{module_name}' updated to '{new_module_info}' successfully."
                                )
                            else:
                                print(
                                    f"Module '{module_name}' not found for Student ID {student_id}."
                                )

                        elif choice == "3":
                            return

    except FileNotFoundError:
        print("Student file not found.")
        return

    if not found:
        print("Student not found.")


def issue_transcripts(): #dine checking
    student_id = input("Enter Student ID: ")
    view_grades(student_id)
    


def view_student_information():# done checking
    student_id = input("Enter Student ID that needed to check: ")
    found = False

    try:
        # Open files
        with open(student_file, "r") as file, open(grade_file, "r") as gradefile:
            lines = file.readlines()
            grades = gradefile.readlines()

            # Iterate through student records
            for line in lines:
                if student_id in line:
                    found = True
                    # Assuming data in lines is comma-separated: ID, Name, Contact
                    data = line.strip().split(",")
                    student_name = data[1] if len(data) > 1 else "Unknown"
                    program = data[2] if len(data) > 2 else "Unknown"

                    print("Student ID:", student_id)
                    print("Student Name:", student_name)
                    print("Program:", program)

                    # Find the student's grade
                    for grade in grades:
                        if student_id in grade:
                            print("Student's Grade:", grade.strip())
                            break
                    else:
                        print("Grade not found for the student.")

                    break  # Exit loop after finding the student

    except FileNotFoundError:
        print("Student file not found.")
        return

    if not found:
        print("Student not found.")


def registrar_menu():
    while True:
        #print_menu()
        print("-------------------------------")
        print("Registrar Menu")
        print("1. Register New Students")
        print("2. Update Student Records")
        print("3. Manage Enrolments")
        print("4. Issue Transcripts")
        print("5. View Student Information")
        print("6. Remove Student")
        print("7. Exit")
        print("-------------------------------")
        choose = input("Please Enter Your Choice: ")

        if choose == "1":
            register_new_student()
        elif choose == "2":
            update_student_record()
        elif choose == "3":
            manage_enrolment()
        elif choose == "4":
            issue_transcripts()
        elif choose == "5":
            view_student_information()
        elif choose == "6":
            remove_student()
        elif choose == "7":
            print("Exiting Registrar Menu.")
            break
