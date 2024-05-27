

from itertools import chain, takewhile



def cousinPrimes():
    
    def go(x):
        n = 4 + x
        return [(x, n)] if isPrime(n) else []

    return chain.from_iterable(
        map(go, primes())
    )


def main():
    

    pairs = list(
        takewhile(
            lambda ab: 1000 > ab[1],
            cousinPrimes()
        )
    )

    print(f'{len(pairs)} cousin pairs below 1000:\n')
    print(
        spacedTable(list(
            chunksOf(4)([
                repr(x) for x in pairs
            ])
        ))
    )



def chunksOf(n):
    
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go

def isPrime(n):

    if n in (2, 3):
        return True
    if 2 > n or 0 == n % 2:
        return False
    if 9 > n:
        return True
    if 0 == n % 3:
        return False

    def p(x):
        return 0 == n % x or 0 == n % (2 + x)

    return not any(map(p, range(5, 1 + int(n ** 0.5), 6)))



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


def listTranspose(xss):
    
    def go(xss):
        if xss:
            h, *t = xss
            return (
                [[h[0]] + [xs[0] for xs in t if xs]] + (
                    go([h[1:]] + [xs[1:] for xs in t])
                )
            ) if h and isinstance(h, list) else go(t)
        else:
            return []
    return go(xss)



def spacedTable(rows):
    
    columnWidths = [
        len(str(row[-1])) for row in listTranspose(rows)
    ]
    return '\n'.join([
        ' '.join(
            map(
                lambda w, s: s.rjust(w, ' '),
                columnWidths, row
            )
        ) for row in rows
    ])


if __name__ == '__main__':
    main()
