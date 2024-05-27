
import cmath


def dft( x ):

    N                           = len( x )
    result                      = []
    for k in range( N ):
        r                       = 0
        for n in range( N ):
            t                   = -2j * cmath.pi * k * n / N
            r                  += x[n] * cmath.exp( t )
        result.append( r )
    return result

def idft( y ):
    
    N                           = len( y )
    result                      = []
    for n in range( N ):
        r                       = 0
        for k in range( N ):
            t                   = 2j * cmath.pi * k * n / N
            r                  += y[k] * cmath.exp( t )
        r                      /= N+0j
        result.append( r )
    return result


if __name__ == "__main__":
    x                           = [ 2, 3, 5, 7, 11 ]
    print( "vals:   " + ' '.join( f"{f:11.2f}" for f in x ))
    y                           = dft( x )
    print( "DFT:    " + ' '.join( f"{f:11.2f}" for f in y ))
    z                           = idft( y )
    print( "inverse:" + ' '.join( f"{f:11.2f}" for f in z ))
    print( " - real:" + ' '.join( f"{f.real:11.2f}" for f in z ))

    N                           = 8
    print( f"Complex signals, 1-4 cycles in {N} samples; energy into successive DFT bins" )
    for rot in (0, 1, 2, 3, -4, -3, -2, -1):    
        if rot > N/2:
            print( "Signal change frequency exceeds sample rate and will result in artifacts")
        sig                     = [
            
            cmath.rect(
                1, cmath.pi*2*rot/N*i
            )
            for i in range( N )
        ]
        print( f"{rot:2} cycle" + ' '.join( f"{f:11.2f}" for f in sig ))
        dft_sig                 = dft( sig )
        print( f"  DFT:  " + ' '.join( f"{f:11.2f}" for f in dft_sig ))
        print( f"   ABS: " + ' '.join( f"{abs(f):11.2f}" for f in dft_sig ))
