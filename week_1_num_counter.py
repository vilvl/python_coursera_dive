from sys import argv

param = argv[1]

sum_ = 0
if param.isdigit():
    for c in param:
        sum_ += int(c)

print(sum_)