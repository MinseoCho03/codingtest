def solution(s):
    
    lst = list(map(int, s.split(" ")))
    minmax = [str(min(lst)), str(max(lst))]
    answer = " ".join(minmax)
    return answer