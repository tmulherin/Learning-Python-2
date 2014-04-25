#!c:\python\python

import Classes

def start():
    
    x = Classes.FirstClass()
    y = Classes.FirstClass()

    x.setdata('King Arthur')
    y.setdata(3.14159)

    print(x.getdata())
    print(y.getdata())

if __name__ == '__main__':
    start()

