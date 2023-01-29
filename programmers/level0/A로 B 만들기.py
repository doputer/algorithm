def solution(before, after):
    s = set(before)
    
    for i in s:
        if before.count(i) != after.count(i):
            return 0
        
    return 1