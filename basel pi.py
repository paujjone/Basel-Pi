import random
import math
import time
coprimes = 0
cofactors = 0
die1list = []
die2list = []
a=0

def factory(number):
    factors =[]
    del factors[:]
    for i in range(1, number + 1):
       if number % i == 0:
           factors.append(i)
    return(factors)

while a<1000000:
    a+=1
    die1 = random.randrange(120)
    die2 = random.randrange(120)
    check = set(factory(die1)) & set(factory(die2))
    print(die1)
    time.sleep(0.5)
    print(die2)
    time.sleep(0.5)
    if check != {1}:
        die1list.append(die1)
        die2list.append(die2)
        cofactors +=1
        print('cofactors :-(')
        time.sleep(0.5)
    elif check == {1}:
        die1list.append(die1)
        die2list.append(die2)
        coprimes +=1
        print('coprimes :-)')
        time.sleep(0.5)
    if coprimes == 0:
        print("0...")
    else:
        approx = math.sqrt((6/(coprimes/(coprimes+cofactors))))
        print(approx)
