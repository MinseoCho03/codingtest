def solution(s, skip, index):
    answer = []
    alphabet, alpha_list = [], []
    
    for i in range(ord('a'), ord('z')+1):
        alphabet.append(chr(i))
    
    for j in alphabet:
        if j not in skip:
            alpha_list.append(j)
    
    for alpha in s:
        idx = alpha_list.index(alpha)
        idx = (idx + index) % len(alpha_list)
        answer.append(alpha_list[idx])
    
    return ''.join(answer)
