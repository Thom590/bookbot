import os

file_content = ""

def parse(user_input):
    global file_content
    with open(user_input) as f:
        file_content = f.read()

def main():
    collected_input = os.path.expanduser(input("Define path to file:"))
    parse(collected_input)
    print(file_content)
    
main()