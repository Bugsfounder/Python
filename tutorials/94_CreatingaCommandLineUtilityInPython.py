import argparse
import sys


def calc(args):
    if args.o == "add":
        return args.x + args.y

    elif args.o == "mul":
        return args.x * args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "div":
        return args.x / args.y

    elif args.o == "rem":
        return args.x % args.y
    else:
        return "Something went wrong:\n Check arguments Correctly: \n1. add +\n2. sub -\n3. mul x\n4. div %\n5. rem for remainder"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter First Number. This is a utility for calculation. Please Contact Manisha for more")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter Second Number. This is a utility for calculation. Please Contact Manisha for more")

    parser.add_argument('--o', type=str, default="add",
                        help="Enter Second Number. This is a utility for calculation. Please Contact Manisha for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
