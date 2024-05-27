
from itertools import (accumulate, chain)
from functools import (reduce)
from operator import (mul)



def eApprox():
    '''Approximation to the value of e.'''
    return reduce(
        lambda a, x: a + 1 / x,
        scanl(mul)(1)(
            range(1, 18)
        ),
        0
    )
def main():
    '''Test'''

    print(
        eApprox()
    )



def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.'''
    return lambda a: lambda xs: (
        accumulate(chain([a], xs), f)
    )



if __name__ == '__main__':
    main()
