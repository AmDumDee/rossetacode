from math import sqrt, cos, exp

DEG = 0.017453292519943295769236907684886127134  
RE = 6371000                                     
dd = 0.001      
FIN = 10000000  
 
def rho(a):
    
    return exp(-a / 8500.0)
 
def height(a, z,d): 
    return sqrt((RE + a)**2 + d**2 - 2 * d * (RE + a) * cos((180 - z) * DEG)) - RE
 
def column_density(a, z):
    
    dsum, d = 0.0, 0.0
    while d < FIN:
        delta = max(dd, (dd)*d)  
        dsum += rho(height(a, z, d + 0.5 * delta)) * delta
        d += delta
    return dsum

def airmass(a, z):
    return column_density(a, z) / column_density(a, 0)

print('Angle           0 m          13700 m\n', '-' * 36)
for z in range(0, 91, 5):
    print(f"{z: 3d}      {airmass(0, z): 12.7f}    {airmass(13700, z): 12.7f}")
