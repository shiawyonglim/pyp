student_file = 'student.txt'
enrollment_file = 'enrollments.txt'
outstanding_file = 'outstanding.txt'


def paid():
     student_id = input("Kindly enter student ID: ").upper()

     with open(outstanding_file, "r") as file:
         lines = file.readlines()
         student_in_outstanding = any(student_id == line.strip().split(',')[0] for line in lines)
         if not student_in_outstanding:
             print("Student is not inside.")
             return
     # Check if student exists in the name list
     with open(student_file, "r") as file:
         lines = file.readlines()
         student_exists = any(student_id == line.strip().split(',')[0] for line in lines)
     outstanding_fee = None
     if student_exists:
         with open("outstanding.txt",'r')as file:
             lines=file.readlines()
             for line in lines:
                 line=line.strip().split(",")
                 if line[0]==student_id:
                     outstanding_fee=line[-1]
                     break
     if outstanding_fee is None:  # Check if outstanding_fee is None
        outstanding_fee = 0


     if float(outstanding_fee)>0:
         while True:
             try:
                 print("-------------------------")
                 print(f"Oustading Fee = {outstanding_fee}")
                 tuition_fee = float(input("Enter tuition fee amount:"))
                 if tuition_fee > 0:
                    if tuition_fee <= float(outstanding_fee):
                        update_file(student_id, tuition_fee)
                        return
                    else:
                        print(f"Tuition fee cannot greater then the outstanding amount ({outstanding_fee})")
                        print("Please re-enter")

                 else:
                     print("Please enter a positive number.")
             except ValueError:
                 print("Please enter a valid number.")

     elif float(outstanding_fee)<=0:
                       print ("This student have fully paid their course fee ")

     else:
         print("Student does not exist")
         paid()


 #update / add to student_acc.txt file
def update_file(student_id,tuition_fee ):
     with open("student_acc.txt",'r')as file:
         lines=file.readlines()

     updated_lines=[]

     for line in lines:
         student_acc_list = line.strip().split(',')



         if  student_acc_list[0] == student_id:
               updated_line = line.strip()+f",{tuition_fee}\n"
               updated_lines.append(updated_line)
               print(f"tuition fee for {student_id} have updated")
         else:
             updated_lines.append(line)

     with open("student_acc.txt", 'w') as file:
         file.writelines(updated_lines)
     receipts(student_id,tuition_fee,0)




def receipts(student_id,tuition_fee,new_num):
     total = 0.0
     print("------RECEIPT--------")
     print(f"Student ID:{student_id}\nTotal Paid Amount:RM{tuition_fee}")
     with open("receipt.txt",'r')as file:
       lines=file.readlines()
       for line in lines:
         last_num=lines[-1].split(",")[0]
         new_num=int(last_num)+1

       with open ("receipt.txt",'a')as file:
           file.writelines(f"\n{new_num},{student_id},RM{tuition_fee}")
     print(f"Receipt Number:{new_num}")
     print("\nThank You")

     with open("student_acc.txt", 'r') as file:
         lines = file.readlines()
         updated_lines = []

         for line in lines:
             data = line.strip().split(",")
             student_name = data[0]

             student_total_paid = [float(x) for x in data[1:]]
             for amount in student_total_paid:
                 total += amount
             updated_line = f"{student_name},{total}\n"
             updated_lines.append(updated_line)

         with open("fin_sum.txt", 'w') as file:
             file.writelines(updated_lines)
     outstanding_fee()


def outstanding_fee():

     with open ("student.txt",'r')as namelist:
         lines=namelist.readlines()
         updated_lines = []
         for line in lines :
             line=line.strip().split(",")
             course_fee=line[-1]
             student_id=line[0]
             with open ("fin_sum.txt",'r')as file:
                 lines=file.readlines()
                 for line_fin in lines:
                     line_fin=line_fin.strip().split(",")
                     if line_fin[0] == student_id:
                         collected=line_fin[-1]
                         outstanding=float(course_fee)-float(collected)
                         updated_line=(f"{line_fin[0]},{outstanding}\n")
                         updated_lines.append(updated_line)
                         break
         with open("outstanding.txt",'w') as oustading:
             oustading.writelines(updated_lines)



def financial_total_receipt():#vs total receipt
   with open ("fin_sum.txt",'r')as file:
     lines=file.readlines()
     total_paid_list=[]
     total_receipt=0.0

     for line in lines :
       student_id,total_paid=line.strip().split(",")
       total_paid_list.append(float(total_paid))
     for amount in total_paid_list:
         total_receipt +=amount
         
     print(f"Total fees collected = RM{total_receipt}")
     return total_receipt





def financial_total_course_fee():#vs total course fee
   with open("student.txt",'r')as file :
     lines=file.readlines()
     total_fee_list=[]
     total_course_fee = 0.0

     for line in lines :
        data =line.strip().split(",")
        course_fee=data[-1]
        total_fee_list.append(float(course_fee))

     for fee in total_fee_list:
       total_course_fee += fee        
     print(f"Total course fess = RM{total_course_fee}")

   return total_course_fee


def compare_receipt_and_course_fee(total_fee, total_receipt):
     financial_sumary= float(total_fee) - float(total_receipt)
     print(f"----------------------------\nTotal outstanding = RM{financial_sumary}\n")



def accountant_menu ():
     while True:
        print("----------Accountance Menu-----------", "\n1.Record tuittion fees ", "\n2.View outstanding fees","\n3.Financial Sumary","\n4.Main Menu");
        task = input("Enter number of task : ")
        if task=="1":
          paid()
        elif task == "2":
            print("--------------------------------------\nList of student with outstanding Fees")
            with open("outstanding.txt", 'r') as file:
                print(file.read())
        elif task == "3":
           total_fee = financial_total_course_fee()
           total_receipt = financial_total_receipt()

           compare_receipt_and_course_fee(total_fee, total_receipt)
        elif task =="4":
           print("returning to the menu")
           return
        else:
           print("Invalid input.Please enter a number between 1-4 ")
           continue


