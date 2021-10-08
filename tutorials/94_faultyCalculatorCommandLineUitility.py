# QUICK QUIZ := Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a command line utility calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# Your program should take operator and the two numbers as argument from the user
# and then return the result

import argparse
import sys


def faultyCalculator(args):
    if args.a == 45 and args.b == 3 and args.o == '*':
        return 555
    elif args.a == 56 and args.b == 9 and args.o == '+':
        return 77
    elif args.a == 56 and args.b == 6 and args.o == '/':
        return 4
    elif args.o == '+':
        return args.a + args.b
    elif args.o == '-':
        return args.a - args.b
    elif args.o == '*':
        return args.a * args.b
    elif args.o == '/':
        return args.a / args.b
    else:
        return "Something went wrong check arguments perfectly.\n"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--a', type=int, default=1.0,
                        help="Enter First Number. This is a utility for Calculation. Please Contact Manisha For More")

    parser.add_argument('--b', type=int, default=1.0,
                        help="Enter Second Number. This is a utility for Calculation. Please Contact Manisha For More")

    parser.add_argument('--o', type=str, default='+', help="Select Operations symbol:- +, -, *, /")

    args = parser.parse_args()
    sys.stdout.write(str(faultyCalculator(args)))
