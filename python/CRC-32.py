from functools import (reduce)
from itertools import (islice)


def crc32(s):
    
    def go(x):
        x2 = x >> 1
        return 0xedb88320 ^ x2 if x & 1 else x2
    table = [
        index(iterate(go)(n))(8)
        for n in range(0, 256)
    ]
    return reduce(
        lambda a, c: (a >> 8) ^ table[
            (a ^ ord(c)) & 0xff
        ],
        s,
        (0xffffffff)
    ) ^ 0xffffffff


def main():
    
    print(
        format(
            crc32('The quick brown fox jumps over the lazy dog'),
            '02x'
        )
    )


def index(xs):
    
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
    )



def iterate(f):
    
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


if __name__ == '__main__':
    main()
