# Write a program to make a copy of a text file “this.txt”

with open("this.txt") as f:     
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)

    '''saved the content of 'this.txt' in the variable (content),
    opened/created a copy file and copied what was stored in (content)'''