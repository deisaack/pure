a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)
print(a_dict['server'])
# print(a_dict['mysql']) KeyError
a_dict['database'] = 'Postgres'
print(a_dict)
a_dict['user'] = 'Isaac'
print(a_dict)

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

print(len(SUFFIXES))
print(1000 in SUFFIXES)
print(SUFFIXES[1000])
print(SUFFIXES[1000][3])
print(SUFFIXES[1024][:])
SUFFIXES[1000][2] = 'YYY'
print(SUFFIXES[1000][:])
