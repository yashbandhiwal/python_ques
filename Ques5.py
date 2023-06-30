# Ques: Python Program for compound interest
# A = P(1 + R/100)raise to the power t 

# Compound Interest = A - P

p = 10000
r = 8
t = 3

a = p * (pow((1+r/100),t))

ci = a - p

print(ci)