'''

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

'''

number  = 600851475143
# Start with 3 since number is odd
divisor = 3

while divisor < number:
    if number % divisor == 0:
        # Reduce number of factors by dividing by smaller numbers
        number /= divisor
    else:
        # Apart from 2 all prime factors are odd 
        divisor += 2

print(divisor)