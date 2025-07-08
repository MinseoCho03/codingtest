def solution(name, yearning, photo):
    answer = []

    people = {name[i]:yearning[i] for i in range(len(name))}
    
    #또는
    #for i in range(len(name)):
    #   people[name[i]] = yearning[i] 해야 함
    # people = ~ 로 하게 되면 매번 덮어써버림
    
    for row in photo:
        people_sum = 0
        for person in row:
            if person in people:
                people_sum += people[person]
        answer.append(people_sum)
    
    return answer
