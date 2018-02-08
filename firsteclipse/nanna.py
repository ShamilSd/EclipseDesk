import random
from random import choice
def picks(filename):
    with open(filename) as f:
        lines=[line.strip() for line in f]
        return choice(lines).split()[0]
for x in range(130):
     print random.randint(1001,1999),
     print(","),    
     print random.randint(2001,2018),
     print(","),    
     print random.randint(001,500), 
     nselect=picks('genders.txt')
     print(","),        
     print(nselect)