import os

file_content = ""

def parse(user_input):
    global file_content
    with open(user_input) as f:
        file_content = f.read()

def main():
    collected_input = input("Define path to file:")
    collected_input = os.path.expanduser(collected_input)
    parse(collected_input)
    print("hello word")
    print("collected input:", collected_input)
    print("file_contnet:", file_content)
    



main()