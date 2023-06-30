# Python Program for cube sum of first n natural numbers

i = int(input("Enter a Number:"))

temp = 0

for k in range(1,i+1):
    temp = temp + k * k * k

print(temp)