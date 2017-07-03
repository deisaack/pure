subj = ['COM', 'CHE', 'PHY', 'COM', 'GEO', 'STA', 'IRD', 'MAT', 'PSY']
print(subj)
print(len(subj))
print(subj.count('COM'))
print('GEO' in subj)
print('geo' in subj)
print(subj.index('PHY'))
del subj[3]
print(subj)
subj.remove('GEO')
print(subj)
subj.pop()
subj.pop(1)
print(subj)
