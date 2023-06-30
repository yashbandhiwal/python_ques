# Ques: Python program to print all Prime numbers in an Interval

lower = int(input("Please enter lower bound:"))
upper = int(input("Please enter upper bound:"))

flag = True

for k in range(lower,upper):
    for i in range(2,k):
        if k % i == 0:
            flag = False
            break
    else:
        if flag == True:
            print(f'{k}')
    flag = True