lst = [0,1,0,0,2,3,6,0,0,7,6,4,0,6]
last = lst[-1]
for i in range(len(lst)-1,-1,-1):
    if lst[i] ==0:
        lst[i] =last
        continue
    last = lst[i]
print(lst)