from factorial.factorial import *
from exp_root.exponentiation import *
from exp_root.root import *
from logarithm.logarithm import *


def main():
    while True:
        n = input('''Choose what you want to find out
        (if you want to calculate the factorial - enter "f",
        if you want to calculate the exponentiation - enter "e",
        if you want to calculate the root - enter "r",
        if you want to calculate the logarithm - enter "l"):''')

        if n == 'f':
            m = input('Enter the number:')
            while type(m) != int:
                try:
                    m = int(m)
                    if m < 0:
                        raise ValueError
                except ValueError:
                    print('It has to be a positive integer number!')
                    m = input('Enter the number: ')
            print(fact(m))

        elif n == 'e':
            y = input('Choose: exponentiation to the square (enter "2") or cube (enter "3"):')

            m = input('Enter the number:')
            while type(m) != float:
                try:
                    m = float(m)
                except ValueError:
                    print('It has to be a number!')
                    m = input('Enter the number: ')

            if y == '2':
                print(exp2(m))
            elif y == '3':
                print(exp3(m))
            else:
                print('The entered value is incorrect!')

        elif n == 'r':
            y = input('Choose: root of the square (enter "2") or cube (enter "3"):')

            m = input('Enter the number:')
            while type(m) != float:
                try:
                    m = float(m)
                    if m < 0:
                        raise ValueError
                except ValueError:
                    print('It has to be a positive number!')
                    m = input('Enter the number: ')
            if y == '2':
                print(root2(m))
            elif y == '3':
                print(root3(m))
            else:
                print('The entered value is incorrect!')

        elif n == 'l':
            y = input('Choose which logarithm you want to calculate (enter "log", "ln" or "lg"):')

            b = input('Enter the number:')
            while type(b) != int:
                try:
                    b = int(b)
                    if b <= 0:
                        raise ValueError
                except ValueError:
                    print('It has to be a positive integer number!')
                    b = input('Enter the number: ')

            if y == 'log':
                a = input('Enter the base:')
                while type(a) != int:
                    try:
                        a = int(a)
                        if a <= 0 or a == 1:
                            raise ValueError
                    except ValueError:
                        print('It has to be a positive integer number (not 1)!')
                        a = input('Enter the base: ')
                print(log(a,b))
            elif y == 'ln':
                print(ln(b))
            elif y == 'lg':
                print(lg(b))
            else:
                print('The entered value is incorrect!')

        else:
            print('The entered value is incorrect!')

        str = input("If you want to continue, print 'yes' or print any other key to stop the program: ")
        if str != 'yes':
            break


if __name__ == '__main__':
    main()

