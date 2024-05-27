s1 = b"A 'byte string' literal \n"
s2 = b'You may use any of \' or " as delimiter'
s3 = b"""This text 
   goes over several lines
       up to the closing triple quote"""


x = b'abc'
x[0] # evaluates to 97


x = b'abc'
list(x) # evaluates to [97, 98, 99]
bytes([97, 98, 99]) # evaluates to b'abc'
