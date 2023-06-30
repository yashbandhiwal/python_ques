# Python Program for Sum of squares of first n natural numbers

i = int(input("Please Enter A Number"))

temp = 0

for k in range(1, i+1):
    temp = temp + k * k

print(temp)