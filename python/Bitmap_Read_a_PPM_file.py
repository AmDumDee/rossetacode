import io

ppmtxt = '''P3
# feep.ppm
4 4
15
 0  0  0    0  0  0    0  0  0   15  0 15
 0  0  0    0 15  7    0  0  0    0  0  0
 0  0  0    0  0  0    0 15  7    0  0  0
15  0 15    0  0  0    0  0  0    0  0  0
'''


def tokenize(f):
    for line in f:
        if line[0] != '#':
            for t in line.split():
                yield t

def ppmp3tobitmap(f):
    t = tokenize(f)
    nexttoken = lambda : next(t)
    assert 'P3' == nexttoken(), 'Wrong filetype'
    width, height, maxval = (int(nexttoken()) for i in range(3))
    bitmap = Bitmap(width, height, Colour(0, 0, 0))
    for h in range(height-1, -1, -1):
        for w in range(0, width):
            bitmap.set(w, h, Colour( *(int(nexttoken()) for i in range(3))))

    return bitmap
    
print('Original Colour PPM file')
print(ppmtxt)
ppmfile = io.StringIO(ppmtxt)
bitmap = ppmp3tobitmap(ppmfile)
print('Grey PPM:')
bitmap.togreyscale()
ppmfileout = io.StringIO('')
bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())
