def solution(n, m, section):
    answer = 0
    
    i = 0
    while (i < len(section)):
        start = section[i]
        end = section[i] + m -1
        answer += 1
        
        while (i < len(section) and section[i] <= end):
            i += 1
            
    return answer