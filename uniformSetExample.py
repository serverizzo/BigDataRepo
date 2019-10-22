'''
Uniform set takes a stream of elements and places it into a datastructure with equally likely probability 

Note: This means that element Xi have a s/i chance of being included into the set, as well as elements already in the set have a probability of 
remaining in the set with probailty s/i. (where s is the size of the set)

'''

from myLib import uniformSet

us = uniformSet(40)
# print(us.returnSet())

for i in range(100000):
    us.addElement(i)

print(us.returnSet())