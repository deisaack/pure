elements = []
data = ['good', 4, 'nothing', 'fellow']

for i in range(0, 6):
    elements.append(i)

print(elements)
print(elements.pop(1))

for d in data:
    elements.append(d)

print('\n===========================================================\n')


animals = ['cheetah', 'zebra', 'baboon', 'crocodile', 'kangaroo',
          'pig', 'beer', 'peacock']
zebra = animals[1]
print('Which animal?')
i = int(input())
print(animals[i])
print('\n===========================================================\n')

index = -1
for animal in animals:
    index += 4
    print('The animal at index %d is %s' % (index, animal))
