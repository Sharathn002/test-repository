import sys

# Accept command line arguments
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print(f'Argument 1: {arg1}')
    print(type(arg1))
    print(f'Argument 2: {arg2}')
    print(type(arg2))
else:
    print('No arguments provided.')

# Get system-specific parameters and configuration
print(f'System platform: {sys.platform}')
print(f'Python version: {sys.version}')
print(f'Python executable path: {sys.executable}')
print(f'Search path for modules: {sys.path}')
