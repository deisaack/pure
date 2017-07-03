ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")
stuff = ten_things.split(' ')
more_stuff = [ "Day", "Night", "Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print('Adding: ', next_one)
    stuff.append(next_one)
    print('There\'s %d items now.' % len(stuff))

more_stuff[1] = 'isaac'
print('There we go', stuff)
print('==================================================')
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[:7:2]))
print(len(more_stuff))
print(stuff)
print(more_stuff)
