from math import sqrt
from itertools import chain, count, islice


def abundantTuple(n):

    x = divisorSum(n)
    return [(n, x)] if n < x else []

def divisorSum(n):
    
    floatRoot = sqrt(n)
    intRoot = int(floatRoot)
    blnSquare = intRoot == floatRoot
    lows = [x for x in range(1, 1 + intRoot) if 0 == n % x]
    return sum(lows + [
        n // x for x in (
            lows[1:-1] if blnSquare else lows[1:]
        )
    ])

def main():
    
    print('First 25 abundant odd numbers with their divisor sums:')
    for x in take(25)(
            concatMap(abundantTuple)(
                enumFromThen(1)(3)
            )
    ):
        print(x)

    print('\n1000th odd abundant number with its divisor sum:')
    print(
        take(1000)(
            concatMap(abundantTuple)(
                enumFromThen(1)(3)
            )
        )[-1]
    )

    print('\nFirst odd abundant number over 10^9, with its divisor sum:')
    billion = (10 ** 9)
    print(
        take(1)(
            concatMap(abundantTuple)(
                enumFromThen(1 + billion)(3 + billion)
            )
        )[0]
    )

def enumFromThen(m):
    return lambda n: count(m, n - m)
def concatMap(f):
    return lambda xs: (
        chain.from_iterable(map(f, xs))
    )
def take(n):
    return lambda xs: (
        list(islice(xs, n))
    )


if __name__ == '__main__':
    main()
