from sys import argv
from os.path import exists

script = argv
from_file = input('Copy from==>')
to_file = input('Copy to==>')
in_file = open(from_file)
in_data = in_file.read()

# print("The input file is %d bytes long" % len(in_data))
if exists(to_file):
    print('You are about to overwrite %s with contents of %s which is %d bytes long. Press ENTER to continue' % (to_file, from_file, len(in_data)))
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")

out_file.close()
in_file.close()
