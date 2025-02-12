def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice.sort()  

    a, b, c, d = dice 
    
    if a == d:  
        result = a * 1111
        
    elif a == c or b == d:  
        if a == c:
            result = (a * 10 + d) ** 2
        else:
            result = (b * 10 + a) ** 2
            
    elif (a == b) and (c == d):  
        result = (a + c) * abs(a - c)
    
    elif a==b or b==c or c==d:
        if a==b:
            result = c*d
        elif b==c:
            result = a*d
        else:
            result = a*b
            
    else:  
        result = min(dice)

    return result
