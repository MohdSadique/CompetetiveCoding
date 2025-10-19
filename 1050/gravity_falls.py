for _ in range(int(input())):
    n = int(input())
    stacking = []
    for i in range(n):
        k, *s = input().split()
        stacking.append(" ".join(s))
    stacking.sort()
    
    max_index = 0
    bottom = []
    for s in stacking:
        ele = list(s.split())
        if len(ele) > max_index:
            bottom.extend(ele[max_index:])
            max_index = len(ele)

    print(*bottom)
