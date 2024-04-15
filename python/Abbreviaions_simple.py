
from functools import reduce
import re
def withExpansions(table):
    return lambda s: unwords(map(
        expanded(table), words(s)
    ))
def expanded(table):
    def expansion(k):
        u = k.upper()
        lng = len(k)

        def p(wn):
            w, n = wn
            return w.startswith(u) and lng >= n
        return find(p)(table) if k else Just(('', 0))

    return lambda s: maybe('*error*')(fst)(expansion(s))
def cmdsFromString(s):
    def go(a, x):
        xs, n = a
        return (xs, int(x)) if x.isdigit() else (
            ([(x.upper(), n)] + xs, 0)
        )
    return fst(reduce(
        go,
        reversed(re.split(r'\s+', s)),
        ([], 0)
    ))
def main():
    table = cmdsFromString(
    )
    tests = [
        'riG   rePEAT copies  put mo   rest    types   fup.    6      poweRin',
        ''
    ]

    print(
        fTable(__doc__ + ':\n')(lambda s: "'" + s + "'")(
            lambda s: "\n\t'" + s + "'"
        )(withExpansions(table))(tests)
    )
def compose(g):
    return lambda f: lambda x: g(f(x))
def Just(x):
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}
def Nothing():
    return {'type': 'Maybe', 'Nothing': True}
def find(p):
    def go(xs):
        for x in xs:
            if p(x):
                return Just(x)
        return Nothing()
    return lambda xs: go(xs)
def fst(tpl):
    return tpl[0]
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
def maybe(v):
    return lambda f: lambda m: v if m.get('Nothing') else (
        f(m.get('Just'))
    )
def unwords(xs):
    return ' '.join(xs)
def words(s):
    return re.split(r'\s+', s)
if __name__ == '__main__':
    main()
