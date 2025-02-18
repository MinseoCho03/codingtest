def solution(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    i = 0
    
    while i < len(s):
        
        if s[i].isdigit():
            answer += s[i]
            i += 1
        
        else:
            for index, word in enumerate(numbers):
                if s[i:].startswith(word):
                    answer += str(index)
                    i += len(word)
                    break
                
    return int(answer)