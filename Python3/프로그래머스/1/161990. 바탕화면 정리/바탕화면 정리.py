def solution(wallpaper):
    answer = []
    list_x = []
    list_y = []
    count_y = 0
    for i in wallpaper:
        count_y += 1
        if '#' in i:
            count_x = 0
            for j in i:
                if j == '#':
                    list_y.append(count_x)
                count_x += 1
                
            
            list_x.append(count_y)
        
                
    answer = [min(list_x)-1, min(list_y), max(list_x), max(list_y)+1]
                
    return answer