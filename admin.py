from registrar import register_new_student, remove_student

module_file = 'module.txt'
student_file = 'student.txt'
lecturer_file = 'lecturer.txt'
faculty_file = 'faculty.txt'

def add_new_module (): #done checking 
    print ("--- Add new module ---")
    while True:
        new_module = input("Type 'start' to enter module details or type 'quit' to quit: ")

        if new_module.lower() == 'start':
            existing_module = []
            try:
                with open(module_file, "r") as file:
                    existing_module = [line.strip().split(", ") for line in file.readlines()]
            except FileNotFoundError:
                print(f"{module_file} not found. A new file will be created upon saving.\n")

            while True:
                module_code = input ("Enter the module code: ").strip()
                if any (module_code == m[0] for m in existing_module):
                    print ("The module code exists. Enter new details.")
                    
                module_name = input("Enter the module name: ")
                if any (module_name == m[1] for m in existing_module):
                        print ("The module name already exists. Enter new details.")
                else:
                    break

            module_credit = input("Enter the module credit: ")
            
            faculty = input("Enter the faculty: ")
            existing_faculty = []
            try:
                with open(faculty_file, "r") as file:
                    existing_faculty = [line.strip().split(", ") for line in file.readlines()]
            except FileNotFoundError:
                print(f"{faculty_file} not found. A new file will be created upon saving.\n")
            if any (faculty == f[0] for f in existing_faculty):
                try:
                    with open(module_file, "a") as file:
                        file.write(f"{module_code}, {module_name}, {module_credit},{faculty}\n")
                        print("Module has been added successfully!")
                except FileNotFoundError:
                    print("file not found.")
                    return
            else:
                print ("The faculty does not exist.")

        elif new_module.lower() == 'quit':
            print("Exiting program. All data has been saved.\n")
            break

        else:
            print("Invalid input. Please type 'start' or 'quit'.\n")





def add_new_lecturer():
    print ("--- Add new lecturer ---")

    while True:
        new_lecturer = input("Type 'start' to enter lecturer details or type 'quit' to quit: ")

        if new_lecturer.lower() == 'start':
            existing_lecturer = []
            try:
                with open(lecturer_file, "r") as file:
                    existing_lecturer = [line.strip().split(", ") for line in file.readlines()]
            except FileNotFoundError:
                print(f"{lecturer_file} not found. A new file will be created upon saving.\n")

            while True:
                lecturer_ID = input("Enter the lecturer ID: ").strip()
                if any (lecturer_ID == l[0] for l in existing_lecturer):
                    print ("The lecturer ID already exists. Enter new details.")
                else:
                    break

            lecturer_name = input("Enter the lecturer name: ")
            functional_area = input("Enter the faculty code: ")
            with open(lecturer_file, "a") as file:
                file.write(f"{lecturer_ID}, {lecturer_name}, {functional_area}\n")
                print("Lecturer has been added successfully!")

        elif new_lecturer.lower() == 'quit':
            print("Exiting program. All data has been saved.\n")
            break

        else:
            print("Invalid input. Please type 'start' or 'quit'.\n")


def remove_lecturer():
    print ("--- Remove lecturer")
    while True:
        remove_lecturer_program = input("Type 'start' to remove lecturer details or type 'quit' to quit: ")

        if remove_lecturer_program.lower() == 'start':
            with open(lecturer_file, "r") as file:
                lines = file.readlines ()

            if not lines:
                print("\nNo lecturer details found.\n")
                break

            print ("Current existing lecturer details: \n")
            for line in lines:
                print (line.strip())

            lecturer_to_remove = input ("\nEnter the lecturer ID to remove: ")

            updated_lines = [line for line in lines if not line.startswith(lecturer_to_remove + ",")]

            if len (lines) == len (updated_lines):
                print (f"No student found with ID '{lecturer_to_remove}.")
            else:
                with open(lecturer_file,"w") as file:
                    file.writelines (updated_lines)
                print ("lecturer has been removed successfully!\n")
                print ("Updated lecturer details: ")
                for line in updated_lines:
                    print (line.strip())

        elif remove_lecturer_program.lower() == 'quit':
            print("Exiting program. All data has been saved.\n")
            break

        else:
            print("Invalid input. Please type 'start' or 'quit'.\n")


def update_lecturer():
    print  ("--- Update lecturer details ---")
    while True:
        update_lecturer_program = input("Type 'start' to update lecturer details or type 'quit' to quit: ")

        if update_lecturer_program.lower() == 'start':
            with open(lecturer_file, "r") as file:
                lines = file.readlines ()

            if not lines:
                print("\nNo lecturer details found.\n")
                break

            print ("Current existing lecturer details: ")
            for line in lines:
                print (line.strip())

            lecturer_to_update = input ("\nEnter the lecturer ID to update: ")

            updated_lines = []
            lecturer_found = False

            for line in lines:
                if line.startswith(lecturer_to_update + ","):
                    lecturer_found = True
                    print (f"Current lecturer details: {line.strip()} \n")

                    updated_name = input ("Enter the new lecturer name: ")
                    updated_functional_area = input ("Enter the new functional area: ")

                    updated_line = f"{lecturer_to_update}, {updated_name}, {updated_functional_area}\n"

                    updated_lines.append(updated_line)

                else:
                    updated_lines.append(line)

            if lecturer_found:
                with open(lecturer_file, "w") as file:
                    file.writelines(updated_lines)
                print("Lecturer has been updated successfully!")

            else:
                print(f"No lecturer found with ID '{lecturer_to_update}'.\n")

        elif update_lecturer_program.lower() == 'quit':
            print("Exiting program. All data has been saved.\n")
            break

        else:
            print("Invalid input. Please type 'start' or 'quit'.\n")


def total_students_report():
    print ("--- Total students report ---")
    try:
        with open('student_name_list.txt', "r") as file:
            lines = file.readlines()

        if not lines:
            print("\nNo data found.\n")
            return

        print("- - - Course Programme Report - - -\n")
        print(f"{'Course Programme':<50} {'Number of Students':<20}")
        print("-" * 70)

        course_count = {}
        for line in lines:
            try:
                _, _, _, _, _, course_programme = line.strip().split(",")
                course_programme = course_programme.strip().title()  # Normalize case
            except ValueError:
                print(f"(Invalid line: {line.strip()} automatically skipped)")
                continue

            if course_programme in course_count:
                course_count[course_programme] += 1
            else:
                course_count[course_programme] = 1

        for course, count in course_count.items():
            print(f"{course:<50} {count:<20}")

        students = sum(course_count.values())
        print(f"\ntotal students: {students:<20}")

    except FileNotFoundError:
        print(f"Error: The file '{student_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def active_courses_report():
    print ("--- Active courses report ---")
    try:
        with open (module_file, "r") as file:
            lines = file.readlines()

        if not lines:
            print("\nNo data found.\n")
            return

        print("- - - Active Courses Report - - -\n")
        print(f"{'Module Code':<20} {'Module Name':<20} {'Module Credit':<20} {'Area of Studies':<50}")
        print("-" * 110)

        for line in lines:
            try:
                module_code, module_name, module_credit, area_of_studies = line.strip().split(", ")
                module_credit = int (module_credit.strip())

                print(f"{module_code:<20} {module_name:<20} {module_credit:<20} {area_of_studies:<50}")

            except ValueError:
                print (f"(Invalid line {line.strip()}automatically skipped)")
                continue

    except FileNotFoundError:
        print(f"Error: The file '{module_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def faculty_report():
    print ("--- Faculty report ---")
    try:
        with open(faculty_file, "r") as file:
            lines = file.readlines()

        if not lines:
            print("\nNo data found.\n")
            return

        print("- - - Faculty Report - - -\n")
        print(f"{'Faculty ID':<20} {'Department name':<50}")
        print("-" * 70)

        for line in lines:
            try:
                faculty_ID, department_name = line.strip().split(",")
            except ValueError:
                print(f"(Invalid line {line.strip()}automatically skipped)")
                continue

            print(f"{faculty_ID:<20} {department_name:<50}")

    except FileNotFoundError:
        print(f"Error: The file '{faculty_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_all_data():# done checking
    print ("--- View all data ---")
    try:
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

        print("-" * 100)
        print("Module data review - Module code, Name, Credit, Area of studies")
        print("-" * 100)
        try:
            with open(module_file, "r") as file:
                lines = file.readlines()
            if not lines:
                print("\nNo data found.\n")
            else:
                for line in lines:
                    print (line.strip())
        except FileNotFoundError:
            print(f"Error: The file '{student_file}' was not found.")

        
        print("-" * 100)
        print("Course data review - Module code, Name, Credit")
        print("-" * 100)
        try:
            with open(module_file, "r") as file:
                lines = file.readlines()
            if not lines:
                print("\nNo data found.\n")
            else:
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: The file '{module_file}' was not found.")


        print("-" * 100)
        print("Lecturer data review - Lecturer ID, Name, Functional Area")
        print("-" * 100)
        try:
            with open(lecturer_file, "r") as file:
                lines = file.readlines()
            if not lines:
                print("\nNo data found.\n")
            else:
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: The file '{student_file}' was not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def admin():
    while True:
        print ("----- Administrator Menu -----")
        print ("1. Module")
        print ("2. Students")
        print ("3. Lecturers")
        print ("4. Generate reports")
        print ("5. View all data")
        print ("6. Exit\n")

        choice = input ("Type the number to select your choice: ")

        if choice== "1":
            add_new_module()
        elif choice == "2":
            print ("1. Add students")
            print ("2. Remove students")
            choice = input ("Select your choice: ")
            if choice == "1":
                register_new_student()
            if choice == "2":
                remove_student()

        elif choice == "3":
            print ("1. Add lecturers")
            print ("2. Remove lecturers")
            print ("3. Update lecturers")
            choice = input ("Select your choice: ")
            if choice == "1":
                add_new_lecturer()
            elif choice == "2":
                remove_lecturer()
            elif choice == "3":
                update_lecturer()

        elif choice == "4":
            print ("1. Total students report")
            print ("2. Active courses report")
            print ("3. Faculty report")
            choice = input("Select your choice: ")
            if choice == "1":
                total_students_report()
            elif choice == "2":
                active_courses_report()
            elif choice == "3":
                faculty_report()
            else:
                print ("Invalid input. Please try again.")
        elif choice == "5":
            view_all_data()
        elif choice == "6":
            print ("Exiting program...")
            break
        else:
            print ("Invalid input. Please try again.")