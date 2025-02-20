def solution(n):
    answer = []
    num = str(n)
    lst = list(num)
    for i in lst:
        answer.append(int(i))
    return answer[::-1]