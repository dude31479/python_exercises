
def writeToFile(file_name, text):
    with open(file_name, 'w') as file_obj:
        file_obj.write(text)

def appendToFile(file_name, text):
    with open(file_name, 'a') as file_obj:
        file_obj.write(text)

def readFromFile(file_name):
    with open(file_name, 'r') as file_obj:
        return file_obj.read()

def delFromFile(file_name, text):
    """Can't del something on a file directly. You have to read it, change it
    and then write it back onto the file."""
    pass

writeToFile('./greet.txt', ' ')
print(readFromFile('./greet.txt'))