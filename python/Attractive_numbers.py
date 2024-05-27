

from itertools import chain, count, takewhile
from functools import reduce

def attractiveNumbers():
    
    return filter(
        compose(
            isPrime,
            len,
            primeDecomposition
        ),
        count(1)
    )


def main():
    
    for row in chunksOf(15)(list(
            takewhile(
                lambda x: 120 >= x,
                attractiveNumbers()
            )
    )):
        print(' '.join(map(
            compose(justifyRight(3)(' '), str),
            row
        )))


def chunksOf(n):
    
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


def compose(*fs):
    
    return lambda x: reduce(
        lambda a, f: f(a),
        fs[::-1], x
    )

def primeDecomposition(n):
    
    def go(n, p):
        return [p] + go(n // p, p) if (
            0 == n % p
        ) else []
    return list(chain.from_iterable(map(
        lambda p: go(n, p) if isPrime(p) else [],
        range(2, 1 + n)
    )))

def isPrime(n):
    '''True if n is prime.'''
    if n in (2, 3):
        return True
    if 2 > n or 0 == n % 2:
        return False
    if 9 > n:
        return True
    if 0 == n % 3:
        return False

    return not any(map(
        lambda x: 0 == n % x or 0 == n % (2 + x),
        range(5, 1 + int(n ** 0.5), 6)
    ))

def justifyRight(n):
    
    return lambda c: lambda s: s.rjust(n, c)

if __name__ == '__main__':
    main()
