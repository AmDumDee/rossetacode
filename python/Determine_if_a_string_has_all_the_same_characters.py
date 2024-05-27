from itertools import groupby

def firstDifferingCharLR(s):
    
    def details(xs):
        c = xs[1][0]
        return {
            'char': repr(c),
            'hex': hex(ord(c)),
            'index': s.index(c),
            'total': len(s)
        }
    xs = list(groupby(s))
    return Right(details(xs)) if 1 < len(xs) else (
        Left('Total length ' + str(len(s)) + ' - No character changes.')
    )


def main():
    

    print(fTable('First, if any, points of difference:\n')(repr)(
        either(identity)(
            lambda dct: dct['char'] + ' (' + dct['hex'] +
            ') at character ' + str(1 + dct['index']) +
            ' of ' + str(dct['total']) + '.'
        )
    )(firstDifferingCharLR)([
        '',
        '   ',
        '2',
        '333',
        '.55',
        'tttTTT',
        '4444 444'
    ]))


def either(fl):
    
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


def identity(x):
    
    return x


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

def Left(x):
    
    return {'type': 'Either', 'Right': None, 'Left': x}


def Right(x):
    
    return {'type': 'Either', 'Left': None, 'Right': x}


if __name__ == '__main__':
    main()
