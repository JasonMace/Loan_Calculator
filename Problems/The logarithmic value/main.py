from math import log

x = abs(int(input()))
y = int(input())

print(round(log(x, y), 2) if y > 1 else round(log(x), 2))
