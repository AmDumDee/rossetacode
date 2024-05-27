
from math import gcd



def coprime(a, b):
    
    return 1 == gcd(a, b)


def main():
    

    print([
        xy for xy in [
            (21, 15), (17, 23), (36, 12),
            (18, 29), (60, 15)
        ]
        if coprime(*xy)
    ])


if __name__ == '__main__':
    main()
