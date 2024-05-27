
from itertools import chain, cycle, islice



def chao(l):
    '''Chaocipher encoding or decoding for the given
       left and right 'wheels'.
       A ciphertext is returned if the boolean flag
       is True, and a plaintext if the flag is False.
    '''
    def go(l, r, plain, xxs):
        if xxs:
            (src, dst) = (l, r) if plain else (r, l)
            (x, xs) = (xxs[0], xxs[1:])

            def chaoProcess(n):
                return [dst[n]] + go(
                    shifted(1)(14)(rotated(n, l)),
                    compose(shifted(2)(14))(shifted(0)(26))(
                        rotated(n, r)
                    ),
                    plain,
                    xs
                )

            return maybe('')(chaoProcess)(
                elemIndex(x)(src)
            )
        else:
            return []
    return lambda r: lambda plain: lambda xxs: concat(go(
        l, r, plain, xxs
    ))



def rotated(z, s):
    '''Rotation of string s by z characters.'''
    return take(len(s))(
        drop(z)(
            cycle(s)
        )
    )



def shifted(src):
    '''The string s with a set of its characters cyclically
       shifted from a source index to a destination index.
    '''
    def go(dst, s):
        (a, b) = splitAt(dst)(s)
        (x, y) = splitAt(src)(a)
        return concat([x, rotated(1, y), b])
    return lambda dst: lambda s: go(dst, s)



def main():
    '''Print the plain text, followed by
       a corresponding cipher text,
       and a decode of that cipher text.
    '''
    chaoWheels = chao(
        "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    )(
        "PTLNBQDEOYSFAVZKGJRIHWXUMC"
    )
    plainText = "WELLDONEISBETTERTHANWELLSAID"
    cipherText = chaoWheels(False)(plainText)

    print(plainText)
    print(cipherText)
    print(
        chaoWheels(True)(cipherText)
    )



def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}



def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))



def concat(xs):
    '''The concatenation of all the elements
       in a list or iterable.
    '''
    def f(ys):
        zs = list(chain(*ys))
        return ''.join(zs) if isinstance(ys[0], str) else zs

    return (
        f(xs) if isinstance(xs, list) else (
            chain.from_iterable(xs)
        )
    ) if xs else []


def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)



def elemIndex(x):
    '''Just the index of the first element in xs
       which is equal to x,
       or Nothing if there is no such element.
    '''
    def go(xs):
        try:
            return Just(xs.index(x))
        except ValueError:
            return Nothing()
    return lambda xs: go(xs)



def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if None is m or m.get('Nothing') else (
        f(m.get('Just'))
    )



def splitAt(n):
    '''A tuple pairing the prefix of length n
       with the rest of xs.
    '''
    return lambda xs: (xs[0:n], xs[n:])



def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )



if __name__ == '__main__':
    main()
