import os

file_content = ""
i = 0

def parse(user_input):
    global file_content
    with open(user_input) as f:
        file_content = f.read()

def count(user_input):
    global file_content, i
    words = file_content.split()
    i = 0
    for each in words:
        i += 1

def main():
    collected_input = os.path.expanduser(input("Define path to file:"))
    parse(collected_input)
    count(collected_input)
    print(file_content)
    print(i)
    
main()