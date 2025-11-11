number = (int)(input("Enter the size of the pattern: "))
i = 0
while i < number: # loops through the rows
    for j in range(number): # loops through the columns on each row
        print("*", end="") # print each element of all columns in the current row
    print() # newline for the next row
    i += 1