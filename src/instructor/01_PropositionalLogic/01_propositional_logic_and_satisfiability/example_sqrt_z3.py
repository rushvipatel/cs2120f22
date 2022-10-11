from z3 import *

def sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(sqrtn**2 == n) # replace True with required declarative spec
    s.add(sqrtn >= 0)
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1
    
print(sqrt(9))