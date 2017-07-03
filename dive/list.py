ppo = ['isaac', 'jackton']
ppo += ['Andrew', 'James']
print(ppo)
ppo.append('Betty')
print(ppo)
others = ['Cherop', 'Helen', 'Lina']
ppo.append(others)
print(ppo)
ppo.extend(others)
print(ppo)
ppo.insert(0, 'George')
print(ppo)
print(ppo[2])
ppo.pop(2)
ppo[5] = 'Salome'  # replaces existing vallue
print(ppo)
print(', '.join(ppo))
print('#'.join(ppo[::2]))
for i in range(1, len(ppo)+1):
    ppo.append(i)
ppo.insert(12, 'Holliwood')
print(ppo)
print(len(ppo))
