
from itertools import (chain, cycle, islice)
from operator import (eq)


def cycleFound(xs):
    
    return bind(cycleLength(xs))(
        lambda n: bind(
            findIndex(uncurry(eq))(zip(xs, xs[n:]))
        )(lambda iStart: Just(
            (xs[iStart:iStart + n], n, iStart)
        ))
    )


def cycleLength(xs):
    
    def go(pwr, lng, x, ys):
        if ys:
            y, *yt = ys
            return Just(lng) if x == y else (
                go(2 * pwr, 1, y, yt) if (
                    lng == pwr
                ) else go(pwr, 1 + lng, x, yt)
            )
        else:
            return Nothing()

    return go(1, 1, xs[0], xs[1:]) if xs else Nothing()

def main():
    

    print(
        fTable(
            'First cycle detected, if any:\n'
        )(fst)(maybe('No cycle found')(
            showCycle
        ))(
            compose(cycleFound)(snd)
        )([
            (
                'cycle([1, 2, 3])',
                take(1000)(cycle([1, 2, 3]))
            ), (
                '[0..100] + cycle([1..8])',
                take(1000)(
                    chain(
                        enumFromTo(0)(100),
                        cycle(enumFromTo(1)(8))
                    )
                )
            ), (
                '[1..500]',
                enumFromTo(1)(500)
            ), (
                'f(x) = (x*x + 1) modulo 255',
                take(1000)(iterate(
                    lambda x: (1 + (x * x)) % 255
                )(3))
            )
        ])
    )



def showList(xs):

    return ''.join(repr(xs).split())



def showCycle(cli):
    
    c, lng, iStart = cli
    return showList(c) + ' (from:' + str(iStart) + (
        ', length:' + str(lng) + ')'
    )


def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


def Nothing():
    
    return {'type': 'Maybe', 'Nothing': True}


def bind(m):
    
    return lambda mf: (
        m if m.get('Nothing') else mf(m.get('Just'))
    )

def compose(g):
    
    return lambda f: lambda x: g(f(x))

def enumFromTo(m):
    
    return lambda n: list(range(m, 1 + n))


def findIndex(p):
    
    def go(xs):
        try:
            return Just(next(
                i for i, x in enumerate(xs) if p(x)
            ))
        except StopIteration:
            return Nothing()
    return lambda xs: go(xs)


def fst(tpl):
    
    return tpl[0]


def fTable(s):
    
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


def iterate(f):
    
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)


def maybe(v):
    
    return lambda f: lambda m: v if m.get('Nothing') else (
        f(m.get('Just'))
    )


def snd(tpl):
    
    return tpl[1]


def take(n):
    
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )

def uncurry(f):
    
    return lambda xy: f(xy[0], xy[1])
def concat(xxs):
    
    xs = list(chain.from_iterable(xxs))
    unit = '' if isinstance(xs, str) else []
    return unit if not xs else (
        ''.join(xs) if isinstance(xs[0], str) else xs
    )



if __name__ == '__main__':
    main()
