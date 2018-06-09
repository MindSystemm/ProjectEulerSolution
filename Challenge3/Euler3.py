import math
def IsPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return False
    elif number % 2 ==0:
        return False
    else :
        for i in range(3, int(number /2)):
            if number % i ==0:
                return False
    return True

def FindDivisor(number):
    divisor = []
    for i in range(2, int(math.sqrt(number))):
        if number % i ==0 :
            divisor.append(i)
    return divisor

array = FindDivisor(600851475143)
PrimeDivisor = []
for divisor in array:
    if IsPrime(divisor):
        PrimeDivisor.append(divisor)

PrimeDivisor.sort(reverse=True)
print(PrimeDivisor[0])
