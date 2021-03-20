#### 10/03/2021 ###
''' File Handling and Directory handling'''

#File handling such as .txt .csv(comma separated values) .excel
#Directory handling

# import os #import operating system module

# print(os.getcwd()) #Show the current location of directory cwd-current working directory,pwd- path of working directoru (used in linux)

# print(__file__)

# # os.mkdir("Directory_1")   # making directory/folder(in windows terms)> ye command ek naya folder bnadeti hai.
# # os.chdir("F:") # change directory
# os.rmdir("Directory_1") #remove driectory

# if os.path.isdir("Directory_1"):
#     print("Directory already created")
# else:
#     os.mkdir("Directory_1")

import os #import operating system module
import csv # import csv module for creating a excel file
os.chdir("F://")
file = open("recordd1.csv", "w") #make a csv file in the upper mention directory

# w here is used for file making( if file not exist the makes new and if exist then writes)
# Similarly a> append, 
# x> file making and writing(if file exist then error)
# r> for reading a file

file.write("ID, Name, City\n")
file.write("1, KD, Ynr\n")
file.write("2, VR, Pnt\n")

#using loop 
n=int(input("How many rows you want entered: "))
for n in range(1,n):
    vid = input("ID:")
    name = input("Name:")
    city = input("City:")
    file.write(f"{vid},{name},{city}\n")
file.close()

# file = open("record1.csv", "r") # "r" read krne ke liye sirf 
# print(f.read())
# f.close()
# # WE can also use csv read
# csv_read = csv.reader(open "recordd1.csv")), delimiter="," 
#delimiter ka maltb files comma lg ke separate hongi

###
# print(csv_read)
# l = list(csv_read) # Using list for show rows
# print(l)
##