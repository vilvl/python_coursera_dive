from sys import argv

n = int(argv[1])

for i in range(n):
    print(' ' * (n-1-i) + '#' * (i+1) )
