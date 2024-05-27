from math import sqrt
def agm(a0, g0, tolerance=1e-10):
    
    an, gn = (a0 + g0) / 2.0, sqrt(a0 * g0)
    while abs(an - gn) > tolerance:
        an, gn = (an + gn) / 2.0, sqrt(an * gn)
    return an

print (agm(1, 1 / sqrt(2)))
