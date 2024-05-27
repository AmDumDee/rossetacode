

from itertools import (chain)
from operator import (ne)


def options(lo, hi, total):
    
    ds = enumFromTo(lo)(hi)
    return bind(filter(even, ds))(
        lambda x: bind(filter(curry(ne)(x), ds))(
            lambda y: bind([total - (x + y)])(
                lambda z: [(x, y, z)] if (
                    z != y and lo <= z <= hi
                ) else []
            )
        )
    )

def main():
    

    xs = options(1, 7, 12)
    print(('Police', 'Sanitation', 'Fire'))
    for tpl in xs:
        print(tpl)
    print('\nNo. of options: ' + str(len(xs)))


def bind(xs):
    
    return lambda f: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


def curry(f):
    
    return lambda a: lambda b: f(a, b)


def enumFromTo(m):
    
    return lambda n: list(range(m, 1 + n))

def even(x):
    
    return 0 == x % 2


if __name__ == '__main__':
    main()
