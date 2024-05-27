def square(n):
    return n * n
  
numbers = [1, 3, 5, 7]

squares1 = [square(n) for n in numbers]     

squares2a = map(square, numbers)            

squares2b = map(lambda x: x*x, numbers)     

squares3 = [n * n for n in numbers] 
                                            

isquares1 = (n * n for n in numbers)        

import itertools
isquares2 = itertools.imap(square, numbers) 
