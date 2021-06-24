#Importing mysql python library, establishing connection

import mysql.connector
mydbb=mysql.connector.connect(host="localhost",
                                user="root",
                                password="root",
                                database='student')
mycursor=mydbb.cursor()

class student:
    def __init__(self):
        print('''
----------------------------
welcome to school management
          system
----------------------------
1> Add new student Data
2> Show Student Data
3> Search Student Data
4> Delete Student Data
5> Update Student data
6> Exit''')
        print()

    #Add new student info into database
    
    def new_student(self):
        add_student = int(input("enter the number of students you want to add: "))
        for i in range(1, add_student + 1):
            name = input('enter the name of student: ')
            rollno = int(input("enter the rollno: "))
            address = input("enter the address: ")
            attendance = int(input("enter the attendance: "))
            mycursor.execute(f"insert into student_data values({rollno},'{name}','{address}',{attendance})")
            mydbb.commit()
            
    #Display Student data 
        
    def show_students_list(self):
        mycursor.execute(f"select * from student_data")
        for i in mycursor:
            l=i
            print(f"roll number: {l[0]}\n"
                  f"name: {l[1]}\n"
                  f"address: {l[2]}\n"
                  f"attendance: {l[3]}\n ")
    
    #Search student data from database
    
    def search(self):
        search_rollno=int(input("enter the rollno: "))
        mycursor.execute(f"select * from student_data where rollno={search_rollno}")
        for i in mycursor:
            l=i
        print(f"roll number: {l[0]}\n"
              f"name: {l[1]}\n"
              f"address: {l[2]}\n"
              f"attendance: {l[3]}\n ")
        
    #Delete Student Data from database
    
    def delete(self):
        delete_rollno=int(input('enter the rollno: '))
        mycursor.execute(f"delete from student_data where rollno={delete_rollno}")
        mydbb.commit()
        print("Student Data deleted successfully")
        
    #Update Student Information
    
    def update(self):
        update_attendance=int(input("enter new attendance of the student: "))
        rollno1=int(input("enter the rollno of the student: "))
        mycursor.execute(f"update student_data set attendance={update_attendance} where rollno={rollno1}")
        mydbb.commit()
        print("Student Data updated successfully")

    def exit(self):
        print("Thank you , Have a nice day")

obj=student()
while True:
    select_option=input("choose a number from the above: ")
    if select_option=='1':
        obj.new_student()
        student()
    elif select_option=='2':
        obj.show_students_list()
        student()
    elif select_option=='3':
        obj.search()
        student()
    elif select_option=='4':
        obj.delete()
        student()
    elif select_option=='5':
        obj.update()
        student()
    elif select_option=='6':
        obj.exit()
        break
    else:
        print("Sorry , please choose a valid option")