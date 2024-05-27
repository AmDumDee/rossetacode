def real2cf(x):
    while True:
        t1, f = divmod(x, 1)
        yield int(t1)
        if not f:
            break
        x = 1/f

from fractions import Fraction
from itertools import islice

print(list(real2cf(Fraction(13, 11))))    
print(list(islice(real2cf(2 ** 0.5), 20)))  
