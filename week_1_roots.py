import sys 
from math import sqrt

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

# ax^2 + bx + c = 0
# d = sqrt(b^2 - 4ac)
# x = (-b +- d)/2a 
d = b*b/4/a/a - c/a

if d >= 0:
    print(int(-b/2/a + sqrt(d)))
    print(int(-b/2/a - sqrt(d)))
else:
    print()
    print()
 
