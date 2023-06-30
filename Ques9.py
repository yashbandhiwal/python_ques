# Ques: Python Program for n-th Fibonacci number

i = 0
j = 1

flag = 0

upper = int(input("Please enter upper bound: "))

print("Fibonacci Series: ")
print(i, end=" ")
print(j, end=" ")

for k in range(2, upper):
    flag = i + j
    print(flag, end=" ")
    i = j
    j = flag
print()
