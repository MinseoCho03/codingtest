def solution(wallet, bill):
    
    count = 0
    while True:
        
        if max(wallet) < max(bill) or min(wallet) < min(bill):
            index = bill.index(max(bill))
            bill[index] = max(bill) // 2
            count += 1
        
        else:
            break
            
    return count
