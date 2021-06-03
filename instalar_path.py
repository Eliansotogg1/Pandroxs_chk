import os
path = f'{os.path.dirname(os.path.realpath(__file__))}'
os.environ['PATH'] += os.pathsep + path
print(os.environ['PATH'])