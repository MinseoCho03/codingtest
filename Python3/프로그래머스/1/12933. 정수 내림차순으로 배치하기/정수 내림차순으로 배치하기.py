def solution(n):
    n = str(n)
    answer = int(''.join(sorted(list(n), reverse = True)))
    return answer