pharse = "Don't Panic"
plist = list(pharse)
print(plist) ##on tap
##3,6,5,4
##5476
#Overcoplicated but my chellange was to make it on 6 lines

listHelper = plist[4:8:]
for i in range(4):
    plist.pop((i+1)//4-1)
for i in range(1,-3,-1):
    plist.pop(2)
    plist.append(listHelper[i])

newPharse = ''.join(plist)
print(plist)
print(newPharse)