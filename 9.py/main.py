'''Write a program to find out whether a file is identical and
 matches the content of another'''

with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("YES! These files are identical.")
else:
    print("NO! These files are not identical.")