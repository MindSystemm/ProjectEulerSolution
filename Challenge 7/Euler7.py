def IsPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 ==0:
        return False
    else :
        for i in range(2, int(number /2)):
            if number % i ==0:
                return False
    return True

numberprime = 1
maxprime = 2
i = 1
while numberprime != 10002:
        if(IsPrime(i)):
            maxprime= i
            i+=1
            numberprime+=1
        else:
            i+=1
print(maxprime)
