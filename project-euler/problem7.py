'''

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

'''

def isPrime(n) : 

    if (n <= 1) : 
        return False

    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5

    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True


primeNumber = 0
number      = 1

while True:

    if(isPrime(number)):
        primeNumber += 1

        if(primeNumber == 10001):
            print(number)
            break

    number += 1