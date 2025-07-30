"""Here is the text version of the question from the image:

The prime factors of **13195** are **5, 7, 13,** and 29.

What is the largest prime factor of the number 600851475143?
"""

n=600851475143
i=2
while n!=1:
    if n%i==0:
        n=n//i
    else:
        i+=1

print("Largest prime  factor :",i)

""" 
Output:

Largest prime  factor : 6857

"""