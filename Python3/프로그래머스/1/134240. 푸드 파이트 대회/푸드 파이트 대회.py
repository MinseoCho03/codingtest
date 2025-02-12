def solution(food):
    contest = []
    i = 0 #왜냐면 food[0]은 물이니까 for문 실행했을 때 아무것도 출력 안하게 하기 위함.
    for num in food:
        num = num // 2  
        for _ in range(num): #range(num)은 num만큼 반복 (0 ~ num-1)
            contest.append(str(i))
        i += 1
    
    contest2 = "".join(reversed(contest))
    contest = "".join(contest)
    
    answer = contest + str(0) + contest2
    return answer