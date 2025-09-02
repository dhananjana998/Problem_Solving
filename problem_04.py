"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def palindome(n):
    return str(n)==str(n)[::-1]

palindromic_number= 0
for i in range(100,1000):
    for j in range(100,1000):
        number=i*j
        if palindome(number) and number>palindromic_number:
            palindromic_number=number
print(f"largest palindrome factor:{palindromic_number}")

"""output:

largest palindrome factor:906609

"""