def solution(x):
    num = list(str(x))
    div = 0
    for i in num:
        div += int(i)
    if x % div == 0:
        return True
    else:
        return False