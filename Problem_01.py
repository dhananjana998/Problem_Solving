
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000."""


Sum=0
Num=0
while Num<1000:
    if Num % 3 == 0 or Num % 5 == 0:
        Sum+= Num
    Num+=1
print("The sum of all the multiples of 3 or 5 below 1000 is : \t",Sum)


"""
Output:

The sum of all the multiples of 3 or 5 below 1000 is : 	 233168
"""

