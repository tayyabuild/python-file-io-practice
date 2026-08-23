'''Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
contains the word ‘twinkleʼ.'''

with open("poem.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("The word 'twinkle is present in the file.")
    else:
        print("The word 'twinkle is not present in the file.")