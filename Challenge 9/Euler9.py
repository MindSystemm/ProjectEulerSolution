from math import sqrt
a,b,c = 0
for a in range(0, 1000):
    for b in range(0, 1000):
        c = sqrt((a*a) + (b*b))
        if(a+b+c == 1000 and a < b < c):
            print(str(a*b*c))

print("Finished")
