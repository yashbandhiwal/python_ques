# Ques: Python Program to check Armstrong Number

j = input("Please Enter a Number: ")

str_len = len(j)

check = 0

j = int(j)
flag = j
while j > 0:
    i = j % 10
    check = check + pow(i, str_len)
    j = j // 10

if flag == check:
    print("Armstrong")
else:
    print("Not Armstrong")