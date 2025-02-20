def solution(array):
    arr_set = set(array)
    result = 0
    mode = 0
    
    for i in arr_set:
        if result < array.count(i):
            result = array.count(i)
            mode = i
            flag = True
        elif result == array.count(i):
            flag = False
            
    if flag:
        return mode
    else:
        return -1