# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def occurances_of_a(file_name):
    try:
        f = open(file_name, 'r')
        doc = f.read()
        f.close()
        num_of_a = 0
        for character in doc:
            if character == 'a':
                num_of_a += 1
        return num_of_a
    except FileNotFoundError:
        return 0

print(occurances_of_a('test.txt'))
print(occurances_of_a('testfgdfs.txt'))
