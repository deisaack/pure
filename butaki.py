people = {
    {
        'name'      : 'Justine',
        'gender'    : 'Male',
        'married'   : 'False',
        'divorced'  : 'False',
    },
    {
        'name': 'Paul',
        'gender': 'Male',
        'married': 'True',
        'divorced': 'False',
    },
    {
        'name': 'Sarah',
        'gender': 'Female',
        'married': 'False',
        'divorced': 'True',
    },
}


class Person(object):
    name = None
    gender = None
    married = None

    def __init__(self):
        self.gender

    def foo(self, married):
        print('You have been removed from marrried people')

