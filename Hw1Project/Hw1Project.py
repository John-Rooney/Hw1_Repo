#John Rooney 1/14/20 Homework 1 I have not given or received any unauthorized assistance on this assignment

#Deleted this comment
def grade():
    """Predicts and prints predicted grade in DSC 430."""
    first = input('First name: ')
    last = input('Last name: ')
    iq = eval(input('IQ: '))
    if iq > 130:
        print('You are a Liar')
    elif 110 < iq <= 130:
        print('{} {} will probably get a B'.format(first, last))
    elif 90 <= iq <= 110:
        print('{} {} will probably get a C'.format(first, last))
    else:
        print('{} {} will probably fail'.format(first, last))
    return

def func(lst):
    """Returns True if list contains exactly 3 ints."""
    if len(lst) != 3:
        return False
    for i in lst:
        if type(i) == int:
            continue
        else:
            return False
    return True

def func2(lst):
    """Returns True if list is a valid square."""
    if func(lst) == True:
        if lst[2] <= 0:
            return False
        else:
            return True
    else:
        return False

def func3(lst):
    """Returns perimeter of square."""
    if func2(lst) == True:
        return lst[2]*4
    else:
        return -1

def func4(lst):
    """Returns area of square."""
    if func2(lst) == True:
        return lst[2]**2
    else:
        return -1

def func5(lst1, lst2):
    """Returns overlap area of 2 squares."""
    if func2(lst1) == False or func2(lst2) == False:
        return -1
    if lst1 == lst2:
        return func4(lst1)
    sq1 = [lst1[0], lst1[0]+lst1[2], lst1[1], lst1[1]+lst1[2]]
    sq2 = [lst2[0], lst2[0]+lst2[2], lst2[1], lst2[1]+lst2[2]]
    overlapx = 0
    overlapy = 0
    
    # Overlapping area of x-values
    if sq1[0] <= sq2[0]:
        if sq1[1] <= sq2[0]:
            print('no X overlap')
            return -1
        elif sq2[0] < sq1[1] <= sq2[1]:
            overlapx = sq1[1] - sq2[0]
            print('X overlap is ' + str(overlapx))
        else:
            overlapx = lst2[2]
            print(overlapx)
    else:
        if sq2[1] <= sq1[0]:
            print('no X overlap 2')
            return -1
        elif sq1[0] < sq2[1] <= sq1[1]:
            overlapx = sq2[1] - sq1[0]
            print('22 X overlap is ' + str(overlapx))
        else:
            overlapx = lst1[2]
            print(overlapx, '2')

    # Overlapping area of Y-values
    if sq1[2] <= sq2[3]:
        if sq1[3] <= sq2[2]:
            print('no Y overlap')
            return -1
        elif sq2[2] < sq1[3] <= sq2[3]:
            overlapy = sq1[3] - sq2[2]
            print('Y overlap is ' + str(overlapy))
        else:
            overlapy = lst2[2]
            print(overlapy, 'yy')
    else:
        if sq2[1] <= sq1[2]:
            print('no Y overlap 2')
            return -1
        elif sq1[2] < sq2[3] <= sq1[2]:
            overlapy = sq2[3] - sq1[2]
            print('22 Y overlap is ' + str(overlapy))
        else:
            overlapy = lst1[2]
            print(overlapy, 'y')

func5([1,3,2],[1,1,2])

def prime(x):
    if type(x) != int:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    half = int(x/2)
    for i in range(3,half,2):
        if x % i == 0:
            return False
    else:
        return True

def happy(x):
    """Returns True if number is happy."""
    if type(x) != int or x <= 0:
        return False
    num = str(x)
    lst = []
    tot = 0
    loops = 0
    while tot != 1 and loops < 15:
        for i in str(num):
            lst.append(int(i))
        sqd = []
        for i in lst:
            sqd.append(int(i)**2)
        tot = sum(sqd)
        num = tot
        lst = []
        loops += 1
    else:
        if loops == 15:
            return False
        return True

def happyprime(x):
    """Returns True if number is both happy and prime"""
    if happy(x) == True and prime(x) == True:
        return True
    else:
        return False


def happyprimegen():
    """List of first 100 happy prime numbers."""
    lst = []
    num = 1
    while len(lst) < 100:
        if happyprime(num) == True:
            lst.append(num)
            num += 1
        else:
            num += 1
    return lst

def sadprimegen():
    """List of first 100 sad prime numbers."""
    lst = []
    num = 1
    while len(lst) < 100:
        if prime(num) == True and happy(num) == False:
            lst.append(num)
            num += 1
        else:
            num += 1
    return lst

