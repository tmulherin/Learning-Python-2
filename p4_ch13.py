#!c:\python\python
#p4_ch13.py

def intersect(*args):
    result = []
    arg1, arg2 = args[0], args[1]
    for item in arg1:
        if item in arg2:
            if item not in result:
                result.append(item)
    args = args[2:]
    for arg in args:
        tmpres = result
        result = []
        for item in tmpres:
            if item in arg:
                if item not in result:
                    result.append(item)
    return result

def union(*args):
    result = []
    for arg in args:
        for item in arg:
            if item not in result:
                result.append(item)
    return result
if __name__ == '__main__':
    result = intersect('spam', 'ham', 'lamb', 'Sam')
    result.sort()
    print(result)
    result = union('spam', 'ham', 'lamb', 'Sam')
    result.sort()
    print(result)