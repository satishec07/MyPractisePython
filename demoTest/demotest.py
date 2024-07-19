# Questions: Python program to print all Prime numbers in an Interval
start = 2
end = 17
l = []
l2 = []
for i in range(2,17,1):
    for j in range(2,int(i/2)+1):
        if i % j == 0:
            l.append(i)
            break

    else:
        l2.append(i)
print("l",l)
print("l2",l2)