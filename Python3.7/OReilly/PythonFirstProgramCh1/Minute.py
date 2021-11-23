from datetime import datetime
import time
import sys
import random
odds = list(range(1,60,2))
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute is odd")
else:
    print("This minute is even")
####Sys info####
print(sys.api_version)
print(sys.version)
print(sys.platform)
####Date info####
print(datetime.isoformat(datetime.today()))
print(datetime.today().year)
print(datetime.today().month)
####Time info####
print(time.strftime("%H:%M"))
print(time.strftime("%A:%p"))

if datetime.today().day == 'Saturday':
    print('party!!')
elif datetime.today().day == 'Sunday':
    print('recover')
else:
    print('Work Work')

for ch in 'Mariusz Pudzian Pudzianowski':
    print(ch, end = ' ')

for i in range(5):
    print("Grzegorz is Cool guy")



print(dir(random))


for i in range(3):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute is odd")
    else:
        print("This minute is even")
    time.sleep(60)