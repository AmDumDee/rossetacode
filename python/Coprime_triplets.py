
def Gcd(v1, v2):
    a, b = v1, v2
    if (a < b):
        a, b = v2, v1
    r = 1
    while (r != 0):
        r = a % b
        if (r != 0):
            a = b
            b = r
    return b


a = [1, 2]

n = 3

while (n < 50):
    gcd1 = Gcd(n, a[-1])
    gcd2 = Gcd(n, a[-2])
    
    
    if (gcd1 == 1 and gcd2 == 1 and not(n in a)):
        
        a.append(n)
        n = 3
    else:
        
        n += 1


for i in range(0, len(a)):
    if (i % 10 == 0):
        print('')
    print("%4d" % a[i], end = '');
    

print("\n\nNumber of elements in coprime triplets = " + str(len(a)), end = "\n")
