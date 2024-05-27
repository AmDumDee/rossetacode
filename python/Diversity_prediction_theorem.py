
from itertools import chain
from functools import reduce

def diversityValues(x):
    
    def go(ps):
        mp = mean(ps)
        return {
            'mean-error': meanErrorSquared(x)(ps),
            'crowd-error': pow(x - mp, 2),
            'diversity': meanErrorSquared(mp)(ps)
        }
    return go

def meanErrorSquared(x):
    
    def go(ps):
        return mean([
            pow(p - x, 2) for p in ps
        ])
    return go


def main():
    

    print(unlines(map(
        showDiversityValues(49),
        [
            [48, 47, 51],
            [48, 47, 51, 42],
            [50, '?', 50, {}, 50],  
            []                      
        ]
    )))
    print(unlines(map(
        showDiversityValues('49'),  
        [
            [50, 50, 50],
            [40, 35, 40],
        ]
    )))

def showDiversityValues(x):
    
    def go(ps):
        def showDict(dct):
            w = 4 + max(map(len, dct.keys()))

            def showKV(a, kv):
                k, v = kv
                return a + k.rjust(w, ' ') + (
                    ' : ' + showPrecision(3)(v) + '\n'
                )
            return 'Predictions: ' + showList(ps) + ' ->\n' + (
                reduce(showKV, dct.items(), '')
            )

        def showProblem(e):
            return (
                unlines(map(indented(1), e)) if (
                    isinstance(e, list)
                ) else indented(1)(repr(e))
            ) + '\n'

        return 'Observation:  ' + repr(x) + '\n' + (
            either(showProblem)(showDict)(
                bindLR(numLR(x))(
                    lambda n: bindLR(numsLR(ps))(
                        compose(Right, diversityValues(n))
                    )
                )
            )
        )
    return go


def Left(x):
    
    return {'type': 'Either', 'Right': None, 'Left': x}

def Right(x):
    
    return {'type': 'Either', 'Left': None, 'Right': x}

def bindLR(m):
    
    def go(mf):
        return (
            mf(m.get('Right')) if None is m.get('Left') else m
        )
    return go


def compose(*fs):
    
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, identity)



def concatMap(f):
    
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


def either(fl):
    
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


def identity(x):
    
    return x

def indented(n):
    
    return lambda s: (4 * ' ' * n) + s


def mean(xs):
    
    return sum(xs) / float(len(xs))


def numLR(x):
    
    return Right(x) if (
        isinstance(x, (float, int))
    ) else Left(
        'Expected number, saw: ' + (
            str(type(x)) + ' ' + repr(x)
        )
    )


def numsLR(xs):
    
    def go(ns):
        ls, rs = partitionEithers(map(numLR, ns))
        return Left(ls) if ls else Right(rs)
    return bindLR(
        Right(xs) if (
            bool(xs) and isinstance(xs, list)
        ) else Left(
            'Expected a non-empty list, saw: ' + (
                str(type(xs)) + ' ' + repr(xs)
            )
        )
    )(go)


def partitionEithers(lrs):
    
    def go(a, x):
        ls, rs = a
        r = x.get('Right')
        return (ls + [x.get('Left')], rs) if None is r else (
            ls, rs + [r]
        )
    return reduce(go, lrs, ([], []))

def showList(xs):

    return '[' + ','.join(str(x) for x in xs) + ']'


def showPrecision(n):
    
    def go(x):
        return str(round(x, n))
    return go

def unlines(xs):
    
    return '\n'.join(xs)


if __name__ == '__main__':
    main()
