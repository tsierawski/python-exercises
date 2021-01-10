'''

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

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

sum = 0

for i in range(2000000):
    if(isPrime(i)):
        sum += i

print(sum)