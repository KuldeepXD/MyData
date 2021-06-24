#Importing mysql python library

import mysql.connector
def main():
    print("""------------------------------
    ------------------------------
    Library Management Software
            Main Menu
    ------------------------------
    ------------------------------
    <1> Add Book
    <2> Available books
    <3> update Book
    <4> remove Book""")

    global select_option
    select_option = input('Please select an option from the above:')
main()

#Establishing connection to SQL Database

def sqlconnector():
    global mydbb
    mydbb = mysql.connector.connect( host="localhost",
    user="root",
    password="root",
    database="library")
sqlconnector()

#Creating table

def createtable():
    sqlconnector()
    global mycursor
    mycursor = mydbb.cursor()
    # b=input("enter table name:")
    # mycursor.execute(f"create table {b}(ISBN_number int,Book_name varchar(255),Author_name varchar(255),
    # Quantity int,Price int)")
createtable()

#Adding new book

if select_option=='1':
    def add_book():
        createtable()
        n = int(input('how many books you have to add :'))
        for i in range(1, n + 1):
            ISBN_number = int(input("enter ISBN number:"))
            Book_name = input("enter Book name:")
            Author_name = input("enter Author name:")
            Quantity = int(input("enter quantity:"))
            Price = int(input("enter price:"))
            mycursor.execute(f"insert into book values({ISBN_number},'{Book_name}','{Author_name}',{Quantity},{Price})")
            mydbb.commit()
    add_book()
    main()
    
#Listing Available books

if select_option=='2':
    def list_available_books():
        createtable()
        # mycursor.execute("show tables values")
        mycursor.execute("select * from book")
        for i in mycursor:
            print(i)
    list_available_books()
    main()
    
#Updating books

if select_option=='3':
    def update_book():
        update=input("do you want to update a book:y/n")
        if update=='y':
            book_edition=input("enter book edition:")
            previous_value=input("enter the previous value:")
            mycursor.execute(f"update book set Book_name='{book_edition}' where Book_name='{previous_value}'")
            mydbb.commit()
        if update=='n':
            pass
    update_book()
    main()
    
# Removing book from account

if select_option=='4':
    def remove_book():
        remove=input("do you want to remove book:y/n ")
        if remove=="y":
            book_name=input("enter book name which you have to remove: ")
            mycursor.execute(f"delete from book where Book_name='{book_name}'")
            mydbb.commit()
        if remove=="n":
            pass
    remove_book()
    main()

#Adding student info in database

if select_option=='5':
    def user_info():
        createtable()
        m=int(input("how many students are in college: "))
        for i in range(1,m+1):
            name=input("enter student name: ")
            roll_no=int(input("enter roll number: "))
            mycursor.execute(f"insert into students values('{name}',{roll_no})")
            mydbb.commit()
    user_info()

#Issue new book from per student limit

if select_option=='6':
    def issue_book():
        createtable()
        mycursor.execute("select * from students")
        result=mycursor.fetchall()
        list1=list(result)
        b=[]
        for i in list1:
            a=i[0]
            b.append(a)
        print(b)
        user = input("enter student name: ")
        if user in b:
            print('Name exist, you can issue the book')
            mycursor.execute("select * from book")
            result_books=mycursor.fetchall()
            books_list=[]
            for i in result_books:
                a=i[1]
                books_list.append(a)
            print('books are: ',books_list)
            books_quant=[]
            for i in result_books:
                a = i[3]
                books_quant.append(a)
            print('quantity of books are:',books_quant)
            book_issue = input("enter book name which you have to issue: ")
            mycursor.execute(f"select Quantity from book where Book_name='{book_issue}' ")
            for i in mycursor:
                global k
                k=i
            t=list(k)
            print(f'number of books of {book_issue} are {t} ')
            number_of_books = int(input("how many books you want to issue:"))
            if book_issue in books_list:
                mycursor.execute(f"update book set Quantity={t[0]-number_of_books} where Book_name='{book_issue}'")
                mydbb.commit()
                print("book issued successfully")

        else:
            print("no name")

    issue_book()

