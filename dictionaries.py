counties = {
    'MBS': 'Mombasa',
    'BGM': 'Bungoma',
    'UG': 'Uasin Gishu',
    'NBI': 'Nairobi',
    'TRN': 'Trans-Nzoia',
}


capitals = {
    'UG': 'Eldoret',
    'TRN': 'Kitale',
    'NBI': 'Nairobi',
}

counties['KSM'] = 'Kisumu'
capitals['KSM'] = None
capitals['MBS'] = 'Nyali'
capitals['BGM'] = 'Kimilili'


print('_' * 50)
print('The capital of ', counties['UG'], ' county is ', capitals['UG'])
print('_' * 50)


for abr, county in counties.items():
    print('%s is abreviated as %s' % (county, abr))


print('_' * 50)
for abr, capital in capitals.items():
    print('%s is the capital of %s' % (capital, abr))


print('_' * 50)
for abr, county in counties.items():
    print('The capital of %s(%s) is %s' % (county, abr, capitals[abr]))


print('_' * 50)
where = input('Which county abbreviation? : ')
here = counties.get(where)
print('That is %s county ' % here)
