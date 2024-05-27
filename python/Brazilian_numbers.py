
from itertools import count, islice

def isBrazil(n):
    
    return 7 <= n and (
        0 == n % 2 or any(
            map(monoDigit(n), range(2, n - 1))
        )
    )



def monoDigit(n):
    
    def go(base):
        def g(b, n):
            (q, d) = divmod(n, b)

            def p(qr):
                return d != qr[1] or 0 == qr[0]

            def f(qr):
                return divmod(qr[0], b)
            return d == until(p)(f)(
                (q, d)
            )[1]
        return g(base, n)
    return go


def main():
    
    for kxs in ([
            (' ', count(1)),
            (' odd ', count(1, 2)),
            (' prime ', primes())
    ]):
        print(
            'First 20' + kxs[0] + 'Brazilians:\n' +
            showList(take(20)(filter(isBrazil, kxs[1]))) + '\n'
        )



def primes():
    
    n = 2
    dct = {}
    while True:
        if n in dct:
            for p in dct[n]:
                dct.setdefault(n + p, []).append(p)
            del dct[n]
        else:
            yield n
            dct[n * n] = [n]
        n = 1 + n



def showList(xs):
    
    return '[' + ','.join(str(x) for x in xs) + ']'


def take(n):
    
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go



def until(p):
    
    def go(f):
        def g(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return g
    return go



if __name__ == '__main__':
    main()
