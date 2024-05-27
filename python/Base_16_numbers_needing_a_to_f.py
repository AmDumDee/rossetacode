def p(n):
    
    return 9 < n and (9 < n % 16 or p(n // 16))


def main():
    
    xs = [
        str(n) for n in range(1, 1 + 500)
        if p(n)
    ]
    print(f'{len(xs)} matches for the predicate:\n')
    print(
        table(6)(xs)
    )

def chunksOf(n):
    
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go


def table(n):
    
    def go(xs):
        w = len(xs[-1])
        return '\n'.join(
            ' '.join(row) for row in chunksOf(n)([
                s.rjust(w, ' ') for s in xs
            ])
        )
    return go


if __name__ == '__main__':
    main()
