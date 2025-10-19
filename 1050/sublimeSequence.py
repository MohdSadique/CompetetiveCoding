for _ in range(int(input())): # t
    x, n = map(int, input().split())
    print(x if n%2 else 0)