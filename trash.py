#!C:\python\python

def min1(*args):
    result = args[0]
    for arg in args[1:]:
        if arg > result:
            result = arg
    return result

def min2(first, *rest):
    for arg in rest:
        if arg > first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[-1]


print(min1(3,4,1,2))
print(min2("bb", "aa"))
print(min3([2,2], [1,1], [3,3]))


