#from random import *
#print(randint(1,7))

import random
skip=random.randint(1,7)
print("python chooses",skip, "randomly")
if skip==1:
    print("sunday")
elif skip==2:
    print("monday")
elif skip==3:
    print("tuesday")
elif skip==4:
    print("wed")
elif skip==5:
    print("thu")
elif skip==6:
    print("fri")
elif skip==7:
    print("sat")
i=0
while i<8:
    if i==skip:
        print("number skipped")
    else:
        print("number is",i)
    i=i+1




