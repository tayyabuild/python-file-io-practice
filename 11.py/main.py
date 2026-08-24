# Write a python program to rename a file to “renamed_by_python.txt”.

import os

os.rename("file.txt", "renamed_by_python.txt")


# we simply used 'os library' to get this task done!

# --------------------------------------------------------

# another way to do this(using file i/o operations):

'''
with open("file.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

running this block of code will simply copy the content from the existing
file and then create a new file with the new name and paste the 
content there.

But the problem is that the old file remains in the folder.
In order to delete that, we still need to use the 'os library'.




'''