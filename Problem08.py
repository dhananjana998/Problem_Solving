"""Here is the question written out as plain text:

" n! means n × (n-1) × ⋯ × 3 × 2 × 1.

For example, 10! = 10 × 9 × ⋯ × 3 × 2 × 1 = 3,628,800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!."python code"""
fact = 1
for i in range(1, 101):
    fact = fact * i


digit_sum = 0
for d in str(fact):
    digit_sum = digit_sum + int(d)

print(digit_sum)

#output:648
