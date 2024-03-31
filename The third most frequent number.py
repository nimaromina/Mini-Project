#The third most frequent number
#nimaromina
lst = [4,1,3,1,4,2,1,2,4]
_dict = {}
for i in lst:
    if i not in _dict:
        _dict[i] = 1
    else:
        _dict[i] +=1
_lst = []
for key in _dict:
    _lst.append([key,_dict[key]])
for i in range(len(_lst)):
    _min = i
    for j in range(i,len(_lst)):
        if _lst[_min][1]>_lst[j][1]:
            _min = j
    _lst[_min],_lst[i]=_lst[i],_lst[_min]
print(_lst[-3][0])