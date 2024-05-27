from collections import Counter

def cumulative_freq(freq):
    cf = {}
    total = 0
    for b in range(256):
        if b in freq:
            cf[b] = total
            total += freq[b]
    return cf

def arithmethic_coding(bytes, radix):

    
    freq = Counter(bytes)

    
    cf = cumulative_freq(freq)

    
    base = len(bytes)

    
    lower = 0

    
    pf = 1


    for b in bytes:
        lower = lower*base + cf[b]*pf
        pf *= freq[b]

    
    upper = lower+pf

    pow = 0
    while True:
        pf //= radix
        if pf==0: break
        pow += 1

    enc = (upper-1) // radix**pow
    return enc, pow, freq

def arithmethic_decoding(enc, radix, pow, freq):

    
    enc *= radix**pow;

    
    base = sum(freq.values())

    
    cf = cumulative_freq(freq)

    
    dict = {}
    for k,v in cf.items():
        dict[v] = k

    
    lchar = None
    for i in range(base):
        if i in dict:
            lchar = dict[i]
        elif lchar is not None:
            dict[i] = lchar

    
    decoded = bytearray()
    for i in range(base-1, -1, -1):
        pow = base**i
        div = enc//pow

        c  = dict[div]
        fv = freq[c]
        cv = cf[c]

        rem = (enc - pow*cv) // fv

        enc = rem
        decoded.append(c)

    
    return bytes(decoded)

radix = 10      

for str in b'DABDDB DABDDBBDDBA ABRACADABRA TOBEORNOTTOBEORTOBEORNOT'.split():
    enc, pow, freq = arithmethic_coding(str, radix)
    dec = arithmethic_decoding(enc, radix, pow, freq)

    print("%-25s=> %19s * %d^%s" % (str, enc, radix, pow))

    if str != dec:
    	raise Exception("\tHowever that is incorrect!")
