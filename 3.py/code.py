'''Write a program to generate multiplication tables from 2 to 20 and write it to the different
files. Place these files in a folder for a 13-year-old.'''

# first of all, we'll define a function that generates the multiplication table

def generateTable(n):     
    table = ""                                     # 
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"            # writes the lines of a table and '\n' creates a new line after every iteration of the loop
    with open(f"Tables/table_of_{n}", "w") as f :  # automatically created a file name 'table' inside the folder named 'Tables'
        f.write(table)                             # writes the value of 'table' inside the opened folder and file


for i in range(2, 21):                             # called this function for the numbers 2 to 20; just as we were asked!
    generateTable(i)