
def array_exist(n, pos):
    ans = [-1] * n
    e = 1
    for k, l in enumerate(pos):
        m = len(l)
        if m == 0:
            continue
        if m % k != 0:
            return -1
        count = 0
        for j in l:
            ans[j] = e
            count += 1
            if count % k == 0:
                e+=1
        
    
    return ans
 
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    pos = [[] for _ in range(n+1)]
    for i, e in enumerate(b):
        pos[e].append(i)
    
    ans = array_exist(n, pos)
    if ans != -1:
        print(*ans, sep=' ')
    else:
        print(ans)
    