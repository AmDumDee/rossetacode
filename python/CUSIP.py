
from itertools import (cycle, islice, starmap)
from functools import (reduce)
from operator import (add)
from enum import (Enum)



def isCusip(dct):
    
    def go(s):
        ns = [dct[c] for c in list(s) if c in dct]
        return 9 == len(ns) and (
            ns[-1] == (
                10 - (
                    sum(zipWith(
                        lambda f, x: add(*divmod(f(x), 10))
                    )(cycle([identity, double]))(
                        take(8)(ns)
                    )) % 10
                )
            ) % 10
        )
    return go



def cusipCharDict():
    
    def kv(a, ic):
        i, c = ic
        a[c] = i
        return a
    return reduce(
        kv,
        enumerate(
            enumFromTo('0')('9') + (
                enumFromTo('A')('Z') + list('*&#')
            )
        ),
        {}
    )


def main():
    
    cusipTest = isCusip(cusipCharDict())

    print(
        tabulated('Valid as CUSIP string:')(
            cusipTest
        )([
            '037833100',
            '17275R102',
            '38259P508',
            '594918104',
            '68389X106',
            '68389X105'
        ])
    )


def double(x):
    
    return 2 * x



def enumFromTo(m):
    
    def go(x, y):
        t = type(m)
        i = fromEnum(x)
        d = 0 if t != float else (x - i)
        return list(map(
            lambda x: toEnum(t)(d + x),
            range(i, 1 + fromEnum(y))
        ) if int != t else range(x, 1 + y))
    return lambda n: go(m, n)



def fromEnum(x):
    
    return ord(x) if str == type(x) else (
        x.value if isinstance(x, Enum) else int(x)
    )



def mul(x):
    
    return lambda y: x * y



def identity(x):
    
    return x


def tabulated(s):
    
    def go(f, xs):
        def width(x):
            return len(str(x))
        w = width(max(xs, key=width))
        return s + '\n' + '\n'.join([
            str(x).rjust(w, ' ') + ' -> ' + str(f(x)) for x in xs
        ])
    return lambda f: lambda xs: go(f, xs)



def take(n):
    
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )



def toEnum(t):
    
    dct = {
        int: int,
        float: float,
        str: chr,
        bool: bool
    }
    return lambda x: dct[t](x) if t in dct else t(x)



def zipWith(f):
    
    return lambda xs: lambda ys: (
        list(starmap(f, zip(xs, ys)))
    )



if __name__ == '__main__':
    main()
