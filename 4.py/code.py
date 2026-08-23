'''A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file.'''



word = 'donkey'               # defined the word we'llbe working on

with open("file.txt") as f:   #opened the file in read mode and saved it in the variable named 'content'.
    content = f.read()

if word in content:           # if the wrod 'donkey' is present in the file then replace it with hash. Update the variable 'content' by saving this replace process in it.
    content = content.replace(word, "######")

with open("file.txt", "w") as f:   # oepn the file in write mode. Write the value of 'content' in it; which actually is to replace the word donkey with ###
    f.write(content)