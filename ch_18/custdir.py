#!c:\python\python

# A module that lists the contents of other modules

def listing(module):
    aline = '-' * 80
    print(aline)
    print('Name:', module.__name__, '\nFile:', module.__file__)
    print(aline)

    count = 0
    for attr in module.__dict__.keys( ):
        count += 1
        output = ('%2d) %s' % (count, attr) + ' ')
        if attr[0:2] == "__":
            output += '<built-in name>'
        else:
            output += str(getattr(module, attr))
        print(output)
   
    print(aline)
    print(module.__name__, ' has %d names' % (count))
    print(aline)

if __name__ == '__main__':
    import custdir
    listing(custdir)


        