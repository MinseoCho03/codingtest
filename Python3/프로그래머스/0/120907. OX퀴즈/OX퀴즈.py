def solution(quiz):
    
    result = []
    for exp in quiz:
        left, right = exp.split("=")
        left = left.split(" ")
        x = int(left[0])
        y = int(left[2])
        z = int(right)
        op = left[1]
        
        if op == '+':
            answer = x + y
        elif op == "-":
            answer = x - y
        else:
            break
            

        if answer == z:
            result.append("O")
        else:
            result.append("X")
            
    return result
            