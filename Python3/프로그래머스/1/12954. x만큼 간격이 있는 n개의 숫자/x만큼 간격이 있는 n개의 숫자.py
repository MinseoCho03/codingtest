def solution(x, n):
    answer = [0]*n
    for i in range(1,n+1):
        answer[i-1] = x*i
    return answer