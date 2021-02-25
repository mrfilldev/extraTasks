x = int(input('x = '))
ans = str('')
if 1 <= x <= 100:
    if x == 100:
        print('C')
    else:
        if x / 10 == 1:
            print('X')
        elif x / 10 == 2:
            print('XX')
        elif x / 10 == 3:
            print('XXX')
        elif x / 10 == 4:
            print('XL')
        elif x / 10 == 5:
            print('L')
        elif x / 10 == 6:
            print('LX')
        elif x / 10 == 7:
            print('LXX')
        elif x / 10 == 8:
            print('LXXX')
        elif x / 10 == 9:
            print('XC')

        if x % 10 == 1:
            print('I')
        elif x % 10 == 2:
            print('II')
        elif x % 10 == 3:
            print('III')
        elif x % 10 == 4:
            print('IV')
        elif x % 10 == 5:
            print('V')
        elif x % 10 == 6:
            print('VI')
        elif x % 10 == 7:
            print('VII')
        elif x % 10 == 8:
            print('VIII')
        elif x % 10 == 9:
            print('IX')
else:
    print('error')
