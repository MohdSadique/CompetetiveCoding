def calc_op(s, i, t_p):
    if s[i] == t_p:
        return 1
    return 2

  
def helper(s, index, type_pos, rev):
    if len(s) == 0:
        return 0
    
    t_p = type_pos
    
    if not rev:
        curr_sum = 0
        for j in range(index, len(s)):
            curr_sum += calc_op(s, j, t_p)
            t_p = s[j]
        return curr_sum
    else:
        min_sum  = helper(s, index, t_p, False)
        
        for i in range(index+1, len(s)):
            new_str = ''.join(reversed(s[:i+1])) + s[i+1:]
            min_sum = min(min_sum, helper( new_str, index, t_p, False))
        
        curr_sum = calc_op(s, index, t_p)
        t_p = s[index]
        min_sum = min(min_sum, curr_sum + helper(s[index+1:], 0, t_p, rev))
        return min_sum
        
            
            
            

for _ in range(int(input())):
    _ = input(); s = input()
    index = 0
    type_pos = '0'
    rev = True
    
    ans = helper(s, index, type_pos, rev)
    print(ans)
    