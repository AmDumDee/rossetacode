def _init():
    "digit sections for forming numbers"
    digi_bits = """
#0  1   2  3  4  5  6   7   8   9
#
 .  ‾   _  ╲  ╱  ◸  .|  ‾|  _|  ◻
#
 .  ‾   _  ╱  ╲  ◹  |.  |‾  |_  ◻
#
 .  _  ‾   ╱  ╲  ◺  .|  _|  ‾|  ◻
#
 .  _  ‾   ╲  ╱  ◿  |.  |_  |‾  ◻
 
""".strip()

    lines = [[d.replace('.', ' ') for d in ln.strip().split()]
             for ln in digi_bits.strip().split('\n')
             if '#' not in ln]
    formats = '<2 >2 <2 >2'.split()
    digits = [[f"{dig:{f}}" for dig in line]
              for f, line in zip(formats, lines)]

    return digits

_digits = _init()



def _to_digits(n):
    assert 0 <= n < 10_000 and int(n) == n
    
    return [int(digit) for digit in f"{int(n):04}"][::-1]

def num_to_lines(n):
    global _digits
    d = _to_digits(n)
    lines = [
        ''.join((_digits[1][d[1]], '┃',  _digits[0][d[0]])),
        ''.join((_digits[0][   0], '┃',  _digits[0][   0])),
        ''.join((_digits[3][d[3]], '┃',  _digits[2][d[2]])),
        ]
    
    return lines

def cjoin(c1, c2, spaces='   '):
    return [spaces.join(by_row) for by_row in zip(c1, c2)]
if __name__ == '__main__':
    
    
    for pow10 in range(4):    
        step = 10 ** pow10
        print(f'\nArabic {step}-to-{9*step} by {step} in Cistercian:\n')
        lines = num_to_lines(step)
        for n in range(step*2, step*10, step):
            lines = cjoin(lines, num_to_lines(n))
        print('\n'.join(lines))
    

    numbers = [0, 5555, 6789, 6666]
    print(f'\nArabic {str(numbers)[1:-1]} in Cistercian:\n')
    lines = num_to_lines(numbers[0])
    for n in numbers[1:]:
        lines = cjoin(lines, num_to_lines(n))
    print('\n'.join(lines))
