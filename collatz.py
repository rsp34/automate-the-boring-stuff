import sys


def collatz(num):
    if num % 2 == 0:
        out = evenCollatz(num)
    else:
        out = oddCollatz(num)
    print(int(out))
    return out


def evenCollatz(num):
    return num/2


def oddCollatz(num):
    return 3*num+1


try:
    check = True
    while check:
        inputString = input('Choose an integer: ')
        try:
            num = int(inputString)
            check = False
        except ValueError:
            check = True
    while num != 1:
        num = collatz(num)
except KeyboardInterrupt:
    sys.exit()