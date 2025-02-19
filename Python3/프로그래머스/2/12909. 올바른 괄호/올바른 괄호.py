def solution(s):
    
    if s[0] == '(' and s[-1] == ')':
        i = 0
        opened, closed = 0, 0
        while(opened>=closed and i < len(s)):
            if s[i] == '(':
                opened += 1
            else:
                closed += 1
            i += 1
            
        if i == len(s) and opened == closed:
            return True
        else:
            return False
        
    else:
        return False