#!c:\python\python

# cd C:\Users\tmulher\Documents\_dev\Python\lp2e
# cd /C/Users/tmulher/Documents/_dev/Python/lp2e
# p4_ch12.py

y = 5

def intersect(seq1, seq2):
    result = [ ]
    for item in seq1:
         if item in seq2:
            if item not in result:
                result.append(item)
#    print(result) 
    return result

def display_intersect(a, b, result, disp_string):
    result.sort
    print(disp_string)
    print('-' * 40)
    print('The intersection of ', a, ' and', b, '==>\n', result, '\n\n')

def test_intersect():
    a = [1,2,3,4,5,6]
    b = [2,4,6,8,10]
    result = intersect(a, b)
    display_intersect(a, b, result, 'Testing intersect: 2 Lists')
    
    a = 'Ricky Ricardo'
    b = 'William Frawley'
    result = intersect(a, b)
    display_intersect(a, b, result, 'Testing intersect: 2 Strings')

    a = {'b': 2,'d': 4, 'f': 6}
    b = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    result = intersect(a, b)
    display_intersect(a, b, result, 'Testing intersect: 2 Dictionaries')

def scope(x):
    x = 153
    global y
    y += 5
    #y = 'fred' 
    print(y + 5, ' in scope')

    #print(y)
    print('x = ', x, ' in the def.')
def test_scope():
    print(y, ' in test_scope')
    x = (1, 2, 3)
    scope(x)
    print('x = ', x, ' in the caller')

if __name__ == '__main__':
    import os
    os.system('cls')
    #test_intersect()
    test_scope()