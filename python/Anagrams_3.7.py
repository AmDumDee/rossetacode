from os.path import expanduser
from itertools import groupby
from operator import eq



def main():


    print(unlines(
        largestAnagramGroups(
            lines(readFile('unixdict.txt'))
        )
    ))



def largestAnagramGroups(ws):
    
    def wordChars(w):
        
        return (''.join(sorted(w)), w)

    groups = list(map(
        compose(list)(snd),
        groupby(
            sorted(
                map(wordChars, ws),
                key=fst
            ),
            key=fst
        )
    ))

    intMax = max(map(len, groups))
    return list(map(
        compose(unwords)(curry(map)(snd)),
        filter(compose(curry(eq)(intMax))(len), groups)
    ))





def compose(g):
    
    return lambda f: lambda x: g(f(x))



def curry(f):
    
    return lambda a: lambda b: f(a, b)



def fst(tpl):
    
    return tpl[0]



def lines(s):
    
    return s.splitlines()



def readFile(fp):
    
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()



def snd(tpl):
    
    return tpl[1]



def unlines(xs):
    
    return '\n'.join(xs)



def unwords(xs):
    
    return ' '.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()
