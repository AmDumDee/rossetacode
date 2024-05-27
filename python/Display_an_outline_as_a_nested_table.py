
from itertools import chain, cycle, takewhile
from functools import reduce
from operator import add

def wikiTablesFromOutline(colorSwatch):
    
    def go(outline):
        return '\n\n'.join([
            wikiTableFromTree(colorSwatch)(tree) for tree in
            forestFromLevels(
                indentLevelsFromLines(
                    outline.splitlines()
                )
            )
        ])
    return go


def wikiTableFromTree(colorSwatch):
    '''A wikitable rendered from a single tree.
    '''
    return compose(
        wikiTableFromRows,
        levels,
        paintedTree(colorSwatch),
        widthMeasuredTree,
        ap(paddedTree(""))(treeDepth)
    )

def main():
    '''A colored wikitable rendering of a given outline'''

    outline = '''Display an outline as a nested table.
    Parse the outline to a tree,
        measuring the indent of each line,
        translating the indentation to a nested structure,
        and padding the tree to even depth.
    count the leaves descending from each node,
        defining the width of a leaf as 1,
        and the width of a parent node as a sum.
            (The sum of the widths of its children)
    and write out a table with 'colspan' values
        either as a wiki table,
        or as HTML.'''

    print(
        wikiTablesFromOutline([
            "#ffffe6",
            "#ffebd2",
            "#f0fff0",
            "#e6ffff",
            "#ffeeff"
        ])(outline)
    )


def indentLevelsFromLines(xs):
    
    indentTextPairs = [
        (n, s[n:]) for (n, s)
        in (
            (len(list(takewhile(isSpace, x))), x)
            for x in xs
        )
    ]
    indentUnit = len(next(
        x for x in indentTextPairs if x[0]
    )) or 1
    return [
        (x[0] // indentUnit, x[1])
        for x in indentTextPairs
    ]


def forestFromLevels(levelValuePairs):
    
    def go(xs):
        if xs:
            level, v = xs[0]
            children, rest = span(
                lambda x: level < x[0]
            )(xs[1:])
            return [Node(v)(go(children))] + go(rest)
        else:
            return []
    return go(levelValuePairs)

def paddedTree(padValue):
    
    def go(tree):
        def pad(n):
            prev = n - 1
            return Node(tree.get('root'))([
                go(x)(prev) for x in (
                    tree.get('nest') or [Node(padValue)([])]
                )
            ]) if prev else tree
        return pad
    return go


def treeDepth(tree):
    
    def go(_, xs):
        return 1 + max(xs) if xs else 1
    return foldTree(go)(tree)


def widthMeasuredTree(tree):
    
    def go(x, xs):
        return Node((x, 1))([]) if not xs else (
            Node((x, reduce(
                lambda a, child: a + (
                    child.get('root')[1]
                ),
                xs,
                0
            )))(xs)
        )
    return foldTree(go)(tree)

def paintedTree(swatch):
    
    colors = cycle(swatch)

    def go(tree):
        return fmapTree(
            lambda x: ("", x)
        )(tree) if not swatch else (
            Node(
                (next(colors), tree.get('root'))
            )(
                list(map(
                    lambda k, child: fmapTree(
                        lambda v: (k, v)
                    )(child),
                    colors,
                    tree.get('nest')
                ))
            )
        )
    return go


def Node(v):
    
    return lambda xs: {'root': v, 'nest': xs}

def fmapTree(f):
    
    def go(x):
        return Node(
            f(x.get('root'))
        )([go(v) for v in x.get('nest')])
    return go


def foldTree(f):
    
    def go(node):
        return f(
            node.get('root'),
            [go(x) for x in node.get('nest')]
        )
    return go


def levels(tree):
    
    return [[tree.get('root')]] + list(
        reduce(
            zipWithLong(add),
            map(levels, tree.get('nest')),
            []
        )
    )


def wikiTableFromRows(rows):
    
    def cw(color, width):
        def go(w):
            return f' colspan={w}' if 1 < w else ''
        return f'style="background: {color}; "{go(width)}'

    def cellText(cell):
        color, (txt, width) = cell
        return f'| {cw(color,width) if txt else ""} | {txt}'

    def go(row):
        return '\n'.join([cellText(cell) for cell in row])

    return '{| class="wikitable" ' + (
        'style="text-align: center;"\n|-\n'
    ) + '\n|-\n'.join([go(row) for row in rows]) + '\n|}'


def ap(f):
    
    def go(g):
        return lambda x: f(x)(g(x))
    return go



def compose(*fs):

    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, lambda x: x)


def head(xs):
    
    return xs[0] if isinstance(xs, list) else next(xs)


def isSpace(s):
    
    return s.isspace()


def span(p):
    
    def match(ab):
        b = ab[1]
        return not b or not p(b[0])

    def f(ab):
        a, b = ab
        return a + [b[0]], b[1:]

    def go(xs):
        return until(match)(f)(([], xs))
    return go


def until(p):
    
    def go(f):
        def g(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return g
    return go


def zipWithLong(f):
    
    def go(xs, ys):
        lxs = list(xs)
        lys = list(ys)
        i = min(len(lxs), len(lys))
        return chain.from_iterable([
            map(f, lxs, lys),
            lxs[i:],
            lys[i:]
        ])
    return go

if __name__ == '__main__':
    main()
