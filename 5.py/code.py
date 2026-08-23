# Repeat program 4 for a list of such words to be censored.



words = ['donkey', 'monkey', 'bad', 'dirty']               # created a list of word we want to censor

with open("file.txt") as f:                                #opened the file in read mode and saved it in the variable named 'content'.
    content = f.read()

for word in words:
    if word in content:                                    # if the any of the given words is present in the file then replace it with hash. Update the variable 'content' by saving this replace process in it.
        content = content.replace(word, "#" * len(word))   #this adds hashes equal to the length/# of characters of the found word.

with open("file.txt", "w") as f:                           # open the file in write mode. Write the value of 'content' in it; which actually is to replace the word donkey with ###
    f.write(content)