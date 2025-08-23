def solution(a, b, n):
    if n < a:
        return 0
    else:
        answer = 0
        i = n
        while i >= a:
            exchanged = (i//a) * b
            answer += exchanged
            i = (i%a) + exchanged
            
    return answer