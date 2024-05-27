from __future__ import division, print_function
from itertools import accumulate 

def combos(sides, n):
    ret = [1] + [0]*(n + 1)*sides 
    for p in range(1, n + 1):
        rolling_sum = 0
        for i in range(p*sides, p - 1, -1):
            rolling_sum += ret[i - sides] - ret[i]
            ret[i] = rolling_sum
        ret[p - 1] = 0
    return ret

def winning(d1, n1, d2, n2):
    c1, c2 = combos(d1, n1), combos(d2, n2)
    ac = list(accumulate(c2 + [0]*(len(c1) - len(c2))))

    return sum(v*a for  v,a in zip(c1[1:], ac)) / (ac[-1]*sum(c1))


print(winning(4, 9, 6, 6))
print(winning(5, 10, 6, 7))
