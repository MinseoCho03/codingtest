def solution(s):
    last = {}
    answer = []
    for i,ch in enumerate(s):
        if ch in last:
            distance = i - last[ch]
            answer.append(distance)
        else:
            answer.append(-1)
        
        last[ch] = i
    return answer