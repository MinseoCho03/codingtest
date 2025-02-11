def solution(arr, query):
    index = 0
    for i in query:
        if index%2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
        index += 1
            
    return arr