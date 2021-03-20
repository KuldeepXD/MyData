#2D array project

row1 = int(input("Input number of rows: "))
col1 = int(input("Input number of columns: "))
list1 = [[0 for col in range(col1)] for row in range(row1)]

for row in range(row1):
    for col in range(col1):
        list1[row][col]= row*col

print(list1)