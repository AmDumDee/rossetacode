
from math import (floor, sqrt)
from itertools import (islice)


def squaresWithSuffix(n):
    
    stem = 10 ** len(str(n))
    i = 0
    while True:
        i = until(lambda x: isPerfectSquare(n + (stem * x)))(
            succ
        )(i)
        yield n + (stem * i)
        i = succ(i)


def isPerfectSquare(n):
    
    r = sqrt(n)
    return r == floor(r)


def main():
    
    print(
        fTable(main.__doc__ + ':\n')(
            lambda n: str(int(sqrt(n))) + '^2'
        )(repr)(identity)(
            take(10)(squaresWithSuffix(269696))
        )
    )

def identity(x):
    
    return x

def succ(x):
    
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


def take(n):
    
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )

def until(p):
    
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)

def fTable(s):
    
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )

if __name__ == '__main__':
    main()
