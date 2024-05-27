from operator import (mul)

def dotProduct(xs):
    
    return lambda ys: Left('vector sizes differ') if (
        len(xs) != len(ys)
    ) else Right(sum(map(mul, xs, ys)))


def main():
    

    print(
        fTable(main.__doc__ + ':\n')(str)(str)(
            compose(
                either(append('Undefined :: '))(str)
            )(dotProduct([1, 3, -5]))
        )([[4, -2, -1, 8], [4, -2], [4, 2, -1], [4, -2, -1]])
    )


def Left(x):
    
    return {'type': 'Either', 'Right': None, 'Left': x}


def Right(x):
    
    return {'type': 'Either', 'Left': None, 'Right': x}


def append(xs):
    
    return lambda ys: xs + ys

def compose(g):
    
    return lambda f: lambda x: g(f(x))


def either(fl):
    
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


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



if __name__ == '__main__':
    main()
