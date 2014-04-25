#!C:\python\python
import sys
import os

os.system('cls')

print(sys.path, '\n\n')

for path in sys.path:
    print(path)

keys = []
for key in sys.modules.keys():
    keys.append(key)

keys.sort()
print('\n\n')

for key in keys:
    print(key)

