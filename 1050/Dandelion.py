from collections import deque
for _ in range(int(input())):
    n = int(input())
    fields = list(map(int, input().split()))
    odd = [i for i in fields if i%2]
    even = [i for i in fields if i%2 == 0]
    odd = deque(sorted(odd))
    
    if len(odd) == 0:
        print(0)
    else:
        total = odd.pop()
        total += sum(even)
        on = True
        while odd:
            if on:
                odd.popleft()
                on = False
            else:
                total += odd.pop()
                on = True
                
        print(total) 
    