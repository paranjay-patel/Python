from asyncio.windows_events import NULL
from lib2to3.pgen2.token import EQUAL
import random

print("\n*** Guess The Number ***")
print("----you will get 5 chances to guess the number----")
r_num = random.randint(0,10)
i_num=NULL

for i in range(5):
    try:
        i_num = int(input("\ninput number from 1 to 10 = "))
        if r_num==i_num:
            print("** You Guessed the RIGHT Number** \n")  
            break  
        if r_num!=i_num:  
            print("!!! You Guessed the WRONG number\n")

    except:
        print("!!! enter number only")
        

    

