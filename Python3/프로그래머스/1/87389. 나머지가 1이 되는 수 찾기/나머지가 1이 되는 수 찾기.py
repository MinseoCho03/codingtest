def solution(n):
    i = 1
    while(i<n):
        if n % i == 1:
            break
        i += 1
    return i