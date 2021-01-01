'''

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

largest_palindrome = 0

for i in range(100,1000):

   for j in range(i, 1000):

      k = i * j

      if str(k) == str(k)[::-1] and k > largest_palindrome:

        largest_palindrome = k

print(largest_palindrome)