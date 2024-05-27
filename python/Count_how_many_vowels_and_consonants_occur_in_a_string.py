
from functools import reduce



def vowelAndConsonantCounts(s):
    
    return both(sorted)(
        partition(lambda kv: isVowel(kv[0]))([
            (k, v) for (k, v) in list(charCounts(s).items())
            if k.isalpha()
        ])
    )


def main():
    

    vs, cs = vowelAndConsonantCounts(
        "Forever Fortran 2018 programming language"
    )
    nv, nc = valueSum(vs), valueSum(cs)
    print(f'{nv + nc} "vowels and consonants"\n')

    print(f'\t{nv} characters drawn from {len(vs)} vowels:')
    print(showCharCounts(vs))
    print(f'\n\t{nc} characters drawn from {len(cs)} consonants:')
    print(showCharCounts(cs))

def showCharCounts(kvs):
    
    return '\n'.join(['\t\t' + repr(kv) for kv in kvs])



def both(f):
    
    def go(ab):
        return f(ab[0]), f(ab[1])
    return go



def charCounts(s):
    
    def go(dct, c):
        dct.update({c: 1 + dct.get(c, 0)})
        return dct

    return reduce(go, list(s), dict())



def isVowel(c):
    
    return c in "aeiouAEIOU"



def partition(p):
    
    def go(a, x):
        ts, fs = a
        return (ts + [x], fs) if p(x) else (ts, fs + [x])
    return lambda xs: reduce(go, xs, ([], []))


def valueSum(kvs):
    
    return sum(kv[1] for kv in kvs)



if __name__ == '__main__':
    main()
