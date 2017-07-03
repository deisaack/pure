from sys import argv

script = argv
input_file = input('Which file to read ?\t:')


def print_all(f):
    print(f.read())


def rewind(f):
    print(f.seek(1))


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)


input("First let's print the whole file:\n")
print_all(current_file)


print('\n\nOr maybe you wanted a different line please specify => ')
line = int(input())


print_a_line(line, current_file)


input("Now let's rewind, kind of like a tape.")
rewind(current_file)


input("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)


current_line += 1
print_a_line(current_line, current_file)


current_line += 1
print_a_line(current_line, current_file)
