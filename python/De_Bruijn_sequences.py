
def de_bruijn(k, n):
    
    try:
        
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)
    
def validate(db):
    
    
    dbwithwrap = db+db[0:3]
    
    digits = '0123456789'
    
    errorstrings = []
    
    for d1 in digits:
        for d2 in digits:
            for d3 in digits:
                for d4 in digits:
                    teststring = d1+d2+d3+d4
                    if teststring not in dbwithwrap:
                        errorstrings.append(teststring)
                        
    if len(errorstrings) > 0:
        print("  "+str(len(errorstrings))+" errors found:")
        for e in errorstrings:
            print("  PIN number "+e+"  missing")
    else:
        print("  No errors found")

db = de_bruijn(10, 4)

print(" ")
print("The length of the de Bruijn sequence is ", str(len(db)))
print(" ")
print("The first 130 digits of the de Bruijn sequence are: "+db[0:130])
print(" ")
print("The last 130 digits of the de Bruijn sequence are: "+db[-130:])
print(" ")
print("Validating the deBruijn sequence:")
validate(db)
dbreversed = db[::-1]
print(" ")
print("Validating the reversed deBruijn sequence:")
validate(dbreversed)
dboverlaid = db[0:4443]+'.'+db[4444:]
print(" ")
print("Validating the overlaid deBruijn sequence:")
validate(dboverlaid)
