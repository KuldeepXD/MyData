
def add_book():
    d1 = {}
    call_no=int(input("Enter the Book Call number: "))
    book_name=str(input("Enter the Book Name: "))
    author_name= str(input("Enter the Author Name:"))
    publish_year=int(input("Enter the Book Publish Year: "))
    book_qantity=int(input("Enter the Book Quantity: "))

    d1["Call_no"]=call_no
    d1["Bookname"]=book_name
    d1["Author name"]=author_name
    d1["Publish year"]=publish_year
    d1["Book quantity"]=book_qantity

    print(f"The details of books your entered are as follows:\nBook call number:{call_no}\nBook Name:{book_name}\nAuthor Name:{author_name}\nBook Publish Year:{publish_year}\nBook Quantity:{book_qantity}")
    
def issue_book():
    d2 = {}

    call_no1=int(input("Enter the Book Call number: "))
    student_ID=int(input("Enter the Student's ID: "))
    student_name= str(input("Enter the Student Name:"))
    return_date=str(input("Enter the return date(dd/mm/yy): "))

    d2["Call no"]=call_no1
    d2["Student ID"]=student_ID
    d2["Student name"]=student_name
    d2["Return Date"]=return_date
    

    print("Book issued successfully!")




print("\nLIBRARY MANAGEMENT SOFTWARE MENU")
choice=int(input("Enter your choice:\n<1>: Add Book\n<2>: Update Book\n<3>Issue Book\n<4>: Quantity of Books\n"))


