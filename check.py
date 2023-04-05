import argparse

def function1(arg1, arg2):
    print('Function 1 called with arguments:', arg1, arg2)

def function2(arg1):
    print('Function 2 called with argument:', arg1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('function', help='Name of function to call')
    parser.add_argument('--arg1', help='First argument', default='')
    parser.add_argument('--arg2', help='Second argument', default='')
    args = parser.parse_args()

    if args.function == 'create':
        function1(args.arg1, args.arg2)
    elif args.function == 'delete':
        function2(args.arg1)
    else:
        print('Invalid function name')
