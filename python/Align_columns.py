
from functools import reduce
from itertools import repeat



def main():
    

    txt = '''Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$within$its$column.'''

    rows = [x.split('$') for x in txt.splitlines()]
    table = paddedRows(max(map(len, rows)))('')(rows)

    print('\n\n'.join(map(
        alignedTable(table)('  '),
        [-1, 0, 1]  
    )))



def alignedTable(rows):
    
    def go(sep, eAlign):
        lcr = ['ljust', 'center', 'rjust'][1 + eAlign]

        
        def nextAlignedCol(cols, col):
            w = max(len(cell) for cell in col)
            return cols + [
                [getattr(s, lcr)(w, ' ') for s in col]
            ]

        return '\n'.join([
            sep.join(cells) for cells in
            zip(*reduce(nextAlignedCol, zip(*rows), []))
        ])
    return lambda sep: lambda eAlign: go(sep, eAlign)



def paddedRows(n):
    
    def go(v, xs):
        def pad(x):
            d = n - len(x)
            return (x + list(repeat(v, d))) if 0 < d else x
        return [pad(row) for row in xs]
    return lambda v: lambda xs: go(v, xs) if xs else []



if __name__ == '__main__':
    main()
