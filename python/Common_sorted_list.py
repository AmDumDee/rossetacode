from itertools import chain


def main():
    

    print(
        sorted(nub(concat([
            [5, 1, 3, 8, 9, 4, 8, 7],
            [3, 5, 9, 8, 4],
            [1, 3, 7, 9]
        ])))
    )


def concat(xs):

    return list(chain(*xs))

def nub(xs):
    
    return list(dict.fromkeys(xs))


if __name__ == '__main__':
    main()
