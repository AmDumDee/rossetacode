from functools import (reduce)
import itertools
import random



def treeHTML(tree):
    return foldTree(
        lambda x: lambda xs: (
            f"<{x['tag'] + attribString(x)}>" + (
                str(x['text']) if 'text' in x else '\n'
            ) + ''.join(xs) + f"</{x['tag']}>\n"
        )
    )(tree)



def attribString(dct):
    kvs = dct['kvs'] if 'kvs' in dct else None
    return ' ' + reduce(
        lambda a, k: a + k + '="' + kvs[k] + '" ',
        kvs.keys(), ''
    ).strip() if kvs else ''



def main():
    
    n = 3

    
    strCaption = 'Table generated with Python'
    colNames = take(n)(enumFrom('A'))
    dataRows = map(
        lambda x: (x, map(
            lambda _: random.randint(100, 9999),
            colNames
        )), take(n)(enumFrom(1)))
    tableStyle = {
        'style': "width:25%; border:2px solid silver;"
    }
    trStyle = {
        'style': "border:1px solid silver;text-align:right;"
    }

    
    tableTree = Node({'tag': 'table', 'kvs': tableStyle})([
        Node({
            'tag': 'caption',
            'text': strCaption
        })([]),

        
        (Node({'tag': 'tr'})(
            Node({
                'tag': 'th',
                'kvs': {'style': 'text-align:right;'},
                'text': k
            })([]) for k in ([''] + colNames)
        ))
    ] +
        
        list(Node({'tag': 'tr', 'kvs': trStyle})(
            [Node({'tag': 'th', 'text': tpl[0]})([])] +
            list(Node(
                {'tag': 'td', 'text': str(v)})([]) for v in tpl[1]
            )
        ) for tpl in dataRows)
    )

    print(
        treeHTML(tableTree)
        
    )



def Node(v):
    return lambda xs: {'type': 'Node', 'root': v, 'nest': xs}


def enumFrom(x):
    return itertools.count(x) if type(x) is int else (
        map(chr, itertools.count(ord(x)))
    )


def foldTree(f):
    def go(node):
        return f(node['root'])(
            list(map(go, node['nest']))
        )
    return lambda tree: go(tree)


def take(n):
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(itertools.islice(xs, n))
    )


if __name__ == '__main__':
    main()
