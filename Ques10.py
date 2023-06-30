# Python Program for How to check if a given number is Fibonacci number?

x = 0
y = 1

till = int(input('Please enter a value to check'))
flag = False

print(x, end=", ")
print(y, end=", ")

for k in range(0,till):
    
    temp = x + y
    x = y
    y = temp
    
    print(temp, end=", ")
    
    if temp == till:
        flag = True
    
    if temp >= till:
        break

print()

if flag == True:
    print('Fibonacci Number found')
else:
    print('Fibonacci Number Not Found')