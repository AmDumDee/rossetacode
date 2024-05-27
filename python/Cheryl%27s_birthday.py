
from itertools import groupby
from re import split


def main():
    '''Derivation of the date.'''

    month, day = 0, 1
    print(
        
        uniquePairing(month)(
            
            uniquePairing(day)(
                
                monthsWithUniqueDays(False)([
                    
                    tuple(x.split()) for x in
                    split(
                        ', ',
                        'May 15, May 16, May 19, ' +
                        'June 17, June 18, ' +
                        'July 14, July 16, ' +
                        'Aug 14, Aug 15, Aug 17'
                    )
                ])
            )
        )
    )


def monthsWithUniqueDays(blnInclude):
    '''The subset of months with (or without) unique days.
    '''
    def go(xs):
        month, day = 0, 1
        months = [fst(x) for x in uniquePairing(day)(xs)]
        return [
            md for md in xs
            if blnInclude or not (md[month] in months)
        ]
    return go


def uniquePairing(i):
    '''Subset of months (or days) with a unique intersection.
    '''
    def go(xs):
        def inner(md):
            dct = md[i]
            uniques = [
                k for k in dct.keys()
                if 1 == len(dct[k])
            ]
            return [tpl for tpl in xs if tpl[i] in uniques]
        return inner
    return ap(bindPairs)(go)


def bindPairs(xs):
    '''List monad injection operator for lists
       of (Month, Day) pairs.
    '''
    return lambda f: f(
        (
            dictFromPairs(xs),
            dictFromPairs(
                [(b, a) for (a, b) in xs]
            )
        )
    )


def dictFromPairs(xs):
    '''A dictionary derived from a list of
       month day pairs.
    '''
    return {
        k: [snd(x) for x in m] for k, m in groupby(
            sorted(xs, key=fst), key=fst
        )
    }


def ap(f):
    '''Applicative instance for functions.
    '''
    def go(g):
        def fxgx(x):
            return f(x)(
                g(x)
            )
        return fxgx
    return go

def fst(tpl):
    '''First component of a pair.
    '''
    return tpl[0]


def snd(tpl):
    '''Second component of a pair.
    '''
    return tpl[1]


if __name__ == '__main__':
    main()
