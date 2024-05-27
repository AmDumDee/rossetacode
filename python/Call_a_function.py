def no_args():
    pass

no_args()

def fixed_args(x, y):
    print('x=%r, y=%r' % (x, y))

fixed_args(1, 2)        

fixed_args(y=2, x=1)


myargs=(1,2) 
fixed_args(*myargs)

def opt_args(x=1):
    print(x)

opt_args()              
opt_args(3.141)     

def var_args(*v):
    print(v)

var_args(1, 2, 3)       
var_args(1, (2,3))      
var_args()              

fixed_args(y=2, x=1)    


if 1:
    no_args()


assert no_args() is None

def return_something():
    return 1
x = return_something()

def is_builtin(x):
 print(x.__name__ in dir(__builtins__))

is_builtin(pow)         
is_builtin(is_builtin)  


def takes_anything(*args, **kwargs):
    for each in args:
        print(each)
    for key, value in sorted(kwargs.items()):
        print("%s:%s" % (key, value))
    
    wrapped_fn(*args, **kwargs)
    
