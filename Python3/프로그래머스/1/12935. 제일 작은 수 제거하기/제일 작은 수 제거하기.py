def solution(arr):
    index = arr.index(min(arr))
    arr.pop(index)
    if len(arr) != 0:
        return arr
    else:
        return [-1]