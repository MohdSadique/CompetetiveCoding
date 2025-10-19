
"""
a       b       sum
odd     odd     a.b +1 -> even and max
even    odd     -1  -> a.k is always even + b/k is odd, therefore sum will be always odd
odd     even    a.b/2 + 2 -> b/2 should be even for sum to be even so b should contain 4 as a factor, make k as b/2 if b is divisible by 4 otherwise return -1
even    even    a.b/2 + 2 -> make b as 2, k = b/2
"""    

def max_sum(a, b): # type: ignore
    if a%2 != 0 and b%2 != 0:
        return a*b+1 # type: ignore
    elif a%2 == 0 and b%2 != 0:
        return -1
    elif a%2 == 0 and b%2 == 0:
        return (a*b//2) + 2
    elif a%2 != 0 and b%2 == 0:
        if b%4 == 0:
            return (a*b//2) + 2
        else:
            return -1
    
for _ in range(int(input())): #t
    a, b = map(int, input().split())
    print(max_sum(a,b))