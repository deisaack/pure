from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the file to open:")
file_x = input("> ")

txt_again = open(file_x)

# file = str(txt_again.read())
# file= file.split(' ')
# print(file)

print(txt_again.read())
