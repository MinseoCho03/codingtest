def solution(n):
    prev_prev = 0
    prev = 1
    
    for i in range(n-1):
        fibo = (prev + prev_prev)   
        prev_prev = prev
        prev = fibo
    
    return fibo % 1234567
