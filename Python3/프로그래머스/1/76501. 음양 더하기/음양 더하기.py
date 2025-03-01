def solution(absolutes, signs):
    result = 0
    for i,j in zip(absolutes, signs):
        if j:
            result += i
        else:
            result -= i
    return result