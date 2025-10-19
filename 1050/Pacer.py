for _ in range(int(input())):
    n, m = map(int, input().split())
    pos = 0
    curr_time = 0
    total_score = 0
    for i in range(n):
        a, b = map(int, input().split())
        time_interval = (a - curr_time) 
        if pos == b:
            if time_interval %2 == 0:
                total_score += time_interval
            else:
                total_score += time_interval - 1
        else:
            if time_interval % 2 == 0:
                total_score += (time_interval -1)
            else:
                total_score += (time_interval)
        curr_time, pos = a, b
        
    total_score += (m - curr_time)
    
    print(total_score)
            
        