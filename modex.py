def power_y_mod_n(x, y, n):
    res = 1
    x = x % n
    while y:
        if y&1:
            res = (res * x) % n
        x = (x * x) % n
        y >>= 1
    
    return res


while True:
    try:
        B = input()
        if B == "":
            B = input()
        B = int(B)
        P = int(input())
        M = int(input())
        print(power_y_mod_n(B, P, M))
    except EOFError as e:
        break

