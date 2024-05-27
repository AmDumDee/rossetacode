
from datetime import date
from itertools import islice


def xmasIsSunday(y):
    
    return 6 == date(y, 12, 25).weekday()


def main():
    

    xs = list(filter(
        xmasIsSunday,
        enumFromTo(2008)(2121)
    ))
    total = len(xs)
    print(
        fTable(main.__doc__ + ':\n\n' + '(Total ' + str(total) + ')\n')(
            lambda i: str(1 + i)
        )(str)(index(xs))(
            enumFromTo(0)(total - 1)
        )
    )


def enumFromTo(m):
    
    return lambda n: list(range(m, 1 + n))

def index(xs):
    
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
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



if __name__ == '__main__':
    main()
