# Write a program to mine a log file and find out whether it contains ‘pythonʼ.

word = 'python'

with open("log.txt") as f:
    content = f.read()

    if word in content:
        print("\"python\" is present in this log file.")
    else:
        print("\"python\" is not present in this log file.")
