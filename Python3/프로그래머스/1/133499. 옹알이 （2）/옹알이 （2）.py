def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        flag = True
        prev = ""
        
        while word:
            found = False
            for w in words:
                if word.startswith(w):
                    if prev == w:  
                        flag = False
                        break
                    word = word[len(w):]
                    prev = w
                    found = True
                    break
            
            if not found:
                flag = False
                break

        if flag:
            answer += 1

    return answer
