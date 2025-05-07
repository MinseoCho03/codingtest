def solution(cards1, cards2, goal):
    i, j, k = 0, 0, 0
    while i < len(goal):
        if j < len(cards1) and goal[i] == cards1[j]:
            i += 1
            j += 1
        elif k < len(cards2) and goal[i] == cards2[k]:
            i += 1
            k += 1
        else:
            return 'No'
    return 'Yes'
