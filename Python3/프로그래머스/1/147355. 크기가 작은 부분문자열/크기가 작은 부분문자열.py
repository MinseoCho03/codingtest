def solution(t, p):
    answer = 0
    start = 0
    end = len(p) - 1
    
    while end < len(t):
        if t[start:end+1] <= p:
            answer += 1
        start += 1
        end += 1
    return answer