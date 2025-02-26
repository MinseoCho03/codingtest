def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    result = 0
    for x,y in zip(A,B):
        result += x*y
    return result