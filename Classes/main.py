#!c:\python\python

# 21.3 inheritance
import Classes

def start():
    
    x = Classes.FirstClass()
    y = Classes.FirstClass()

    x.setdata('King Arthur')
    y.setdata(3.14159)

    print(x.getdata())
    print(y.getdata())



    z = Classes.SecondClass()
    z.setdata('Fred')
    print(z.getdata())

    a = Classes.ThirdClass('abc')
    print(a.getdata())

    b = a + 'def'
    print(b.getdata())

    a *= 3
    print(a.getdata())

    c = Classes.NextClass()
    c.printer('Instance call')

if __name__ == '__main__':
    start()

