lst = [0,1,0,0,2,3,6,0,0,7,6,4,0,6]
def nim(lst):
    if lst[i] == 0:
        lst[i] = lst[i+1]
        if lst[i+1] == 0:
            nim(lst)
    return lst



for i in range(len(lst)):
    if lst[i] == 0:
        nim(lst)
        
print(lst)

    
   