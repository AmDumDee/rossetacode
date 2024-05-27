
from itertools import groupby

def duplicatedCharIndices(s):
    
    def go(xs):
        if 1 < len(xs):
            duplicates = list(filter(lambda kv: 1 < len(kv[1]), [
                (k, list(v)) for k, v in groupby(
                    sorted(xs, key=swap),
                    key=snd
                )
            ]))
            return Just(second(fmap(fst))(
                sorted(
                    duplicates,
                    key=lambda kv: kv[1][0]
                )[0]
            )) if duplicates else Nothing()
        else:
            return Nothing()
    return go(list(enumerate(s)))


def main():
    

    def showSample(s):
        return repr(s) + ' (' + str(len(s)) + ')'

    def showDuplicate(cix):
        c, ix = cix
        return repr(c) + (
            ' (' + hex(ord(c)) + ') at ' + repr(ix)
        )

    print(
        fTable('First duplicated character, if any:')(
            showSample
        )(maybe('None')(showDuplicate))(duplicatedCharIndices)([
            '', '.', 'abcABC', 'XYZ ZYX',
            '1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ'
        ])
    )


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

def Just(x):
    
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}

def Nothing():
    
    return {'type': 'Maybe', 'Nothing': True}


def fmap(f):
    
    return lambda xs: [f(x) for x in xs]


def fst(tpl):
    
    return tpl[0]


def head(xs):
    
    return xs[0] if isinstance(xs, list) else next(xs)


def maybe(v):
    
    return lambda f: lambda m: v if (
        None is m or m.get('Nothing')
    ) else f(m.get('Just'))


def second(f):
    
    return lambda xy: (xy[0], f(xy[1]))

def snd(tpl):
    
    return tpl[1]

def swap(tpl):
    
    return (tpl[1], tpl[0])


if __name__ == '__main__':
    main()
