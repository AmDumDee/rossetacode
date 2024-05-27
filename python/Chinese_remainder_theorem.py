
from operator import (add, mul)
from functools import reduce


def cnRemainder(ms):
    
    def go(ms, rs):
        mp = numericProduct(ms)
        cms = [(mp // x) for x in ms]

        def possibleSoln(invs):
            return Right(
                sum(map(
                    mul,
                    cms, map(mul, rs, invs)
                )) % mp
            )
        return bindLR(
            zipWithEither(modMultInv)(cms)(ms)
        )(possibleSoln)

    return lambda rs: go(ms, rs)


def modMultInv(a, b):
    
    x, y = eGcd(a, b)
    return Right(x) if 1 == (a * x + b * y) else (
        Left('no modular inverse for ' + str(a) + ' and ' + str(b))
    )


def eGcd(a, b):
    
    def go(a, b):
        if 0 == b:
            return (1, 0)
        else:
            q, r = divmod(a, b)
            (s, t) = go(b, r)
            return (t, s - q * t)
    return go(a, b)


def main():
    

    print(
        fTable(
            __doc__ + ':\n\n         (moduli, residues) -> ' + (
                'Either solution or explanation\n'
            )
        )(repr)(
            either(compose(quoted("'"))(curry(add)('No solution: ')))(
                compose(quoted(' '))(repr)
            )
        )(uncurry(cnRemainder))([
            ([10, 4, 12], [11, 12, 13]),
            ([11, 12, 13], [10, 4, 12]),
            ([10, 4, 9], [11, 22, 19]),
            ([3, 5, 7], [2, 3, 2]),
            ([2, 3, 2], [3, 5, 7])
        ])
    )


def Left(x):
    
    return {'type': 'Either', 'Right': None, 'Left': x}


def Right(x):
    
    return {'type': 'Either', 'Left': None, 'Right': x}


def any_(p):
    
    def go(xs):
        for x in xs:
            if p(x):
                return True
        return False
    return lambda xs: go(xs)


def bindLR(m):
    
    return lambda mf: (
        mf(m.get('Right')) if None is m.get('Left') else m
    )


def compose(g):
    
    return lambda f: lambda x: g(f(x))



def curry(f):
    
    return lambda a: lambda b: f(a, b)


def either(fl):
    
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


def fTable(s):
    
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + (' -> ') + fxShow(f(x))
            for x in xs
        ])
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )



def numericProduct(xs):
    
    return reduce(mul, xs, 1)


def partitionEithers(lrs):
    
    def go(a, x):
        ls, rs = a
        r = x.get('Right')
        return (ls + [x.get('Left')], rs) if None is r else (
            ls, rs + [r]
        )
    return reduce(go, lrs, ([], []))


def quoted(c):
    
    return lambda s: c + s + c


def uncurry(f):
    
    return lambda xy: f(xy[0])(xy[1])


def zipWithEither(f):
    
    def go(xs, ys):
        ls, rs = partitionEithers(map(f, xs, ys))
        return Left(ls[0]) if ls else Right(rs)
    return lambda xs: lambda ys: go(xs, ys)


if __name__ == '__main__':
    main()
