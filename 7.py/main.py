''' Write a program to find out the line number where python is 
present from ques 6'''


word = 'python'

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if word in line:
        print(f"\"python\" is present in line: {lineno}")
        break

    else: 
        lineno += 1

else:
    print('not found')
    