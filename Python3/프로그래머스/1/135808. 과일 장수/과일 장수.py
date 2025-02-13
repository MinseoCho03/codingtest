def solution(k, m, score):
    score = sorted(score, reverse = True) #내림차순 정렬은 reverse = True
    boxes = [score[i:i+m] for i in range(0, len(score), m)]
    
    profit = 0
    for box in boxes:
        if len(box) == m:
            profit += min(box)*m
        else:
            profit += 0
            
    return profit