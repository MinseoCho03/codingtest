def solution(n, lost, reserve): 
    
    lst = [1]*n
    
    for i in reserve:
        lst[i-1] += 1
        
    for j in lost:
        lst[j-1] -= 1
        
    for k in range(n):
        if lst[k] == 0:
            if k > 0 and lst[k - 1] == 2: 
                lst[k] = 1
                lst[k - 1] = 1
            elif k < n - 1 and lst[k + 1] == 2:  
                lst[k] = 1
                lst[k + 1] = 1
    answer = lst.count(1) + lst.count(2)
    return answer