import sys
import os
import datetime
import string
import platform
import math
import calendar
import multiprocessing
from os.path import exists
#1
print("Twinkle, twinkle, little star,\n \t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are")

#2
print(sys.version)

#3
cDate = "Current date and time :\n" + str(datetime.datetime.today())[0:19]
print(cDate)
##or
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#4
#r = int(input())
#print(r*r*math.pi)

#5
##firstName = input("Please Give first name\n")
##lastName = input("Please Give last name\n")
##print(str(firstName+ " "+lastName)[::-1])

#6
#numbers = list(str(input()).split(","))
#print("List :", numbers)
#print("Tuple :", tuple(numbers))

#7
#fileName = list(str(input("Inesrt Filename")).split("."))
#print("Extension is", fileName[-1])

#8
color_list = ["Red","Green","White" ,"Black"]
print(color_list[::3])

#9
exam_st_date = (11, 12, 2014)
print(" / ".join([str(item) for item in list(exam_st_date)]))

#10
#vN = str(input("Please Give a number"))
#print(int(vN)+int(vN+vN)+int(vN+vN+)

#11
#function = input("Please Give a function")
#print(function.__doc__)

#12
#monthI = int(input("Please give a month"))
#yearI = int(input("Please give a year"))
#print(calendar.month(yearI,monthI))

#13
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#14
d0 = datetime.date(2008, 8, 18)
d1 = datetime.date(2008, 9, 26)
delta = d1 - d0
print(delta.days)

#15
##sphereRadius = int(input())
##print((sphereRadius**3)*3/4)

#16
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

#17
def within(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

#18
def sumTree(n,m,k):
    if n == m and n == k:
        return n*9
    else:
        return n+m+k

#19
def returnIsString(stringIs):
    if stringIs[:2:] == "Is":
        return stringIs
    else:
        return "Is" + stringIs

#20
def stringNCopies(copyString,n):
    newString = ""
    for i in range(n):
        newString = newString + copyString
    return newString

#21
def evenOrOdd(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")

#22
def count4(givenList):
    a = 0
    for i in givenList:
        if i == 4:
            a+=1
    return a

#23
def isInList(number, givenList):
    for i in givenList:
        if i == number:
            return True
    else:
        return False

#24
def checkIfVowel(letter):
    vowels = ['a','e','i','o','u','y',
              'A','E','I','O','U','Y']
    if letter in vowels:
        return True
    return False

#25
def isInList(list,value):
    if value in list:
        return True
    return False

#26
def histogram(list):
    hist = {}
    for i in list:
        if i in hist:
            hist[i] +=1
        else:
            hist[i] = 0
    return  hist

#27
def concatenateOfList(list):
    strJoin = ""
    for i in list:
        strJoin += str(i)
    return strJoin

#28
def printEvenStop (list):
    for i in list:
        if i < 237:
            if i%2 == 0:
             print(i)
        else:
            return

#29
def setCompare(setOne,setTwo):
    return setOne.difference(setTwo)

#30
def triangleArena(a,h):
    return a*h/2

#31
def GCD(intA,intB):
    divisorA = []
    divisorB = []
    for i in range(1,intA + 1):
        if int(intA/i) == intA/i:
            divisorA.append(i)
    for i in range(1,intB + 1):
        if int(intB/i) == intB/i:
            divisorB.append(i)
    for i in divisorA:
        if i not in divisorB:
            divisorA.remove(i)
    if len(divisorA) == 0: return False
    return divisorA[-1]

#33
def sumOfTree(a,b,c):
    if a==b and b==c: return 0
    return a+b+c

#34
def sum20(a,b):
    if a + b >= 15 or a+b < 20: return 20
    return a+b

#35
def wreidLogicProgram(a,b):
    if a == b or a+b == 5 or abs(a-b) == 5: return True
    return False

#36 or Use isinstance(a, type)
def checkIfIntegerSum(a,b):
    if a == int(a) and b == int(b): return a+b
    return False

#37
def displayInfo(name,age,adress):
    print("Name : {},\nAge : {},\nAdress : {},".format(name,age,adress))

#38
def quadraticEquasion(a,b):
    print("({} + {})^2 = ".format(a,b), (a+b)**2)

#39
def rateOfInterest(amt,inte,years):
    return amt* ((1 + inte/100)**years)

#40
def distance(a,b):
    return math.sqrt((a[1]-a[0])**2 + (b[1] -b[0])**2)

#41
def fileExists(path):
    return exists(path)


#42
def printSysBitVersion():
    print(" ".join(str(sys.version).split(" ")[-3:-1]))

#43
def printOsPlatformReleaseInfoPrint():
    print("Python OS name: {}\nPython Platform: {}\nPython ReleaseInfo: {}".format(os.name,sys.platform, platform.release))

#44 or import site; print(site.getsitepackages())
def printPythonSitePackanges():
    print(sys.path[-1])

#45 to call python external command
def pythonExternalCommand(command):
    os.system(command)


#46
def pythonCurrentlyWorkingFile():
    print(os.getcwd())

#47
def cpuUsage():
    print(multiprocessing.cpu_count())

#48
def stringToFloatOrInteger(givenString):
    if len(givenString.split(".")) == 1 or givenString.split(".")[1] == 0 : return int(givenString)
    return float(givenString)
test48a = stringToFloatOrInteger("233.33")
test48b = stringToFloatOrInteger("233")


#49
def listAllFiles():
    pythonExternalCommand("dir")


#50 PRINTING Wihout spaces or newlines
print("something", end ="")
print("something2", end ="")

#51
def checkCpuUsage():
    import cProfile
    cProfile.run('cpuUsage()')

#52 stderr ???
def printUsingStderr():
    import sys
    sys.stderr.write("Lol Its STDEER")

#53
def printEnviromentVariables():
    print('*----------------------------------*')
    print(os.environ)
    print('*----------------------------------*')

#54 import getpass print(getpass.getuser())
def printEnviromentVariablesUsername():
    print("Username equals{}".format(os.environ['USERNAME']))

#55


#56


#57


#58


#59


#60


#61


#62


#63


#64


#65


#66


#67


#68


#69


#70


#71


#72


#73


#74


#75


#76


#77


#78


#79


#80


#81


#82


#83


#84


#85


#86


#87


#88


#89


#90


#91


#92


#93


#94


#95


#96


#97


#98


#99
