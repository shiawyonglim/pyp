login = str(111)

def input_record():
    std=input("Please enter the Student ID: ")
    course=input("Please enter the Course code: ")
    return std,course,login


def new_grade(std,course,login):
    n_grade=input("Please enter the new grade: ")
    return std,login,course,n_grade

def check():
    fhand = open('./my.txt')
    std,course,login = input_record() #3 var
    count=0 # 1 var
    for line in fhand:
        line = line.rstrip()
        if std in line and course in line and login in line:
            print(line, "the record is exist")
            count+=1
    if count == 0:
        print("There is no records")
    return std,login,course,count 


def update():
    print(".....Please enter the Student ID, Lecturer ID and Course Code wanted to be changed......")
    std,login,course,count = check()
    std,login,n_course,n_grade = new_grade(std,course,login)
    with open('../my.txt', 'r') as f:
        lines = f.readlines()
    with open('./my.txt', 'w') as f:
        for line in lines:
            if not (std in line and course in line and login in line):
                f.write(line)
    with open('./my.txt', 'a') as f:
        f.write(f"{login},{std},{n_course},{n_grade}\n")





