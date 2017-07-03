x = int(input('Enter a values =>'))
o = int(input('Select an action'
              ' \n\t 1. ADD\n\t 2.SUBTRACT'
              '\n\t 3.MULTIPLY \n\t 4. DIVIDE\n\n==>'))


def add(a, b):
    print("Adding %d and %d" % (a, b))
    return a + b


def subtract(a, b):
    print('Subtracting %d - %d' % (a, b))
    return a-b


def multiply(a, b):
    print('Multiplying %d * %d' % (a, b))
    return a*b


def divide(a, b):
    print('Dividing %d / %d' % (a, b))
    return a/b

if o == 1 or o == 2 or o == 3 or o == 4:
    y = int(input('Enter the other value =>'))

    if o == 1:
        ans = add(x, y)
        print('The answer is %d ' % ans)
    elif o == 2:
        ans = subtract(x, y)
        print('The answer is %d ' % ans)
    elif o == 3:
        ans = multiply(x, y)
        print('The answer is %d ' % ans)
    elif o == 4:
        ans = divide(x, y)
        print('The answer is %d ' % ans)
    else:
        print('Invalid input')
else:
    print('Invalid input')
