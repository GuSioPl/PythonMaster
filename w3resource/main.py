## w3resource.com/python-exercises/python-basic-exercises.php
def ex1():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t"
          "Up above the world so high,\n\t\tLike a diamond in the sky.\n"
          "Twinkle, twinkle, little star,\n\tHow I wonder what you are")

def ex2():
    import platform
    print(platform.python_version())

def ex3():
    import datetime
    print(datetime.datetime.today())

def ex4():
    import math
    print(math.pi*float(input("Please give me Radius: \n"))**2)

def ex5():
    name = input("Please give yours name: ")
    print("{} {}".format(name.split(' ')[1],name.split(' ')[0]))

def ex6():
    numbers = input("").split(', ')
    print(f'{numbers}\n{tuple(numbers)}')

def ex7():
    exten = input("Please give file name").split('.')[-1]
    print(exten)

def ex8():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[::3])

def ex9():
    from itertools import cycle
    exam_st_date = input("provide examination date")[1:-1].split(', ')
    print(exam_st_date)
    print("exam date will be ", *exam_st_date, sep ='/ ')
    print("exam date will be ", ' / '.join(map(str, exam_st_date)) )

def ex10():
    number = input("Please provide Number")
    sum = 0
    for i in range(1,4):
        sum += int(number*i)
    print(sum)

def ex11():
    function = input()
    print(function.__doc__)

def ex12():
    import calendar
    y = int(input("year : "))
    m = int(input("month : "))
    print(calendar.month(y, m))

def ex13():
    print("""
    a string that you "don't" have to escape
    This
    is a  ....... multi-line
    heredoc string --------> example
    """)

def ex14():
    import datetime
    print(abs((datetime.datetime.strptime(input("Provide first date\n>>>"),"(%Y, %m, %d)") -
          datetime.datetime.strptime(input("Provide second date\n>>>"), "(%Y, %m, %d)"))))

def ex15():
    import math
    print("Volume of that sphere is: ",4/3*math.pi*int(input("please povide r of sphere\n>>>"))**3)

def ex16():
    num=int(input("Please provide number\n>>>"))
    print(17 - num) if num < 17 else print(2*abs(17-num))

def ex21():
    num = int(input("please give number"))
    stringForPrint = input("please give string")
    for i in range(num+1): print(stringForPrint,end="")

def ex26():
    listHist = [1,2,3,5]
    for i in range(len(listHist)+1):
        for j in range(i):
            print('*', end='')
        print('')

def ex27():
    givenList = [1,2,3,5]
    stringFromList = ''
    for i in givenList:
        stringFromList += str(i)
    print(stringFromList)

def ex28():
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]
    for i in numbers:
        if i != 237:
            print(i) if i%2==0 else 0
        else:
            break
def ex29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(set.difference(color_list_1,color_list_2))

def ex32():
    import math
    a = int(input("a"))
    b = int(input("b"))
    print(f"GCD = {math.gcd(a,b)}, LCM = {math.lcm(a,b)}")

def ex01():
    a = int(input("a >>>"))
    b = int(input("b >>>"))
    c = int(input("c >>>"))
    return True if a==b or b==c or c==a or a+b == 5 or b+c == 5 or a+c == 5 else False

def ex01():
    obj1 = 2
    obj2 = 1
    print(type(obj1))
    if type(obj1) == type(obj2) == type(1):
        print(str(obj1 + obj2))

def ex01():
    import math
    point1 = (1,2)
    point2 = (2,3)
    print(math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2))

def ex42():
    fileName = input(">>>")
    try:
        f = open(fileName,'r')
        f.close()
    except FileNotFoundError:
        print("There are no such file")

def ex01():
    import platform
    import os
    print(platform.architecture()[0])
    print(os.name, platform.platform(),platform.release())
    import site
    print(site.getsitepackages())


if __name__ == '__main__':
    ex01()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
