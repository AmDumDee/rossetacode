
from itertools import count
from functools import reduce



def genBankFormatWithBaseCounts(sequence):
    '''DNA Sequence displayed in a subset of the GenBank format.
       See example at foot of:
       https://www.genomatix.de/online_help/help/sequence_formats.html
    '''
    ks, totals = zip(*baseCounts(sequence))
    ns = list(map(str, totals))
    w = 2 + max(map(len, ns))

    return '\n'.join([
        'DEFINITION  len=' + str(sum(totals)),
        'BASE COUNT  ' + ''.join(
            n.rjust(w) + ' ' + k.lower() for (k, n)
            in zip(ks, ns)
        ),
        'ORIGIN'
    ] + [
        str(i).rjust(9) + ' ' + k for i, k
        in zip(
            count(1, 60),
            [
                ' '.join(row) for row in
                chunksOf(6)(chunksOf(10)(sequence))
            ]
        )
    ] + ['//'])

def baseCounts(baseString):
    '''Sums for each base type in the given sequence string, with
       a fifth sum for any characters not drawn from {A, C, G, T}.'''
    bases = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    return zip(
        list(bases.keys()) + ['Other'],
        foldl(
            lambda a: compose(
                nthArrow(succ)(a),
                flip(curry(bases.get))(4)
            )
        )((0, 0, 0, 0, 0))(baseString)
    )



def main():
    '''Base counts and sequence displayed in GenBank format
    '''
    print(
        genBankFormatWithBaseCounts('''\
CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATG\
CTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTG\
AGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGAT\
GGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT\
CGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGG\
TCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA\
TTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTAT\
CGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTG\
TCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGAC\
GACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT''')
    )



def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []



def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, lambda x: x)



def curry(f):
    '''A curried function derived
       from an uncurried function.
    '''
    return lambda x: lambda y: f(x, y)



def flip(f):
    '''The (curried or uncurried) function f with its
       arguments reversed.
    '''
    return lambda a: lambda b: f(b)(a)



def foldl(f):
    '''Left to right reduction of a list,
       using the binary operator f, and
       starting with an initial value a.
    '''
    def go(acc, xs):
        return reduce(lambda a, x: f(a)(x), xs, acc)
    return lambda acc: lambda xs: go(acc, xs)

def nthArrow(f):
    '''A simple function lifted to one which applies
       to a tuple, transforming only its nth value.
    '''
    def go(v, n):
        return v if n > len(v) else [
            x if n != i else f(x)
            for i, x in enumerate(v)
        ]
    return lambda tpl: lambda n: tuple(go(tpl, n))



def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x


if __name__ == '__main__':
    main()
