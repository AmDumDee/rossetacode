from itertools import (islice)
from operator import (add)


def nCatalans(n):
    
    def diff(xs):
        
        return (
            xs[0] - (xs[1] if 1 < len(xs) else 0)
        ) if xs else None
    return list(map(
        compose(diff)(uncurry(drop)),
        enumerate(map(fst, take(n)(
            everyOther(
                pascalTriangle()
            )
        )))
    ))



def pascalTriangle():
    
    return iterate(nextPascal)([1])



def nextPascal(xs):
    
    return zipWith(add)([0] + xs)(xs + [0])



def main():
    

    print(
        nCatalans(16)
    )





def compose(g):
    
    return lambda f: lambda x: g(f(x))


def drop(n):
    
    def go(xs):
        if isinstance(xs, list):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)



def everyOther(g):
    
    while True:
        yield take(1)(g)
        take(1)(g)      



def fst(tpl):
    
    return tpl[0]



def iterate(f):
    
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)



def take(n):
    
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )



def uncurry(f):
    
    return lambda xy: f(xy[0])(
        xy[1]
    )



def zipWith(f):
    
    return lambda xs: lambda ys: (
        list(map(f, xs, ys))
    )



if __name__ == '__main__':
    main()
