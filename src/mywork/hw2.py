<<<<<<< HEAD
from z3 import *



=======
# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
>>>>>>> 5779e4baff43c1917c72c67c9391c88923ed1090
def hw2():
    
    
    # Create z3 variable(s) representing the unknown
<<<<<<< HEAD
=======
    # Here, the unknown, x, is the square root of n.
>>>>>>> 5779e4baff43c1917c72c67c9391c88923ed1090
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
<<<<<<< HEAD
    # X ∨ Y, X ⊢ ¬Y 
    # in propositional logic "or" is not exclusive
    
    
    C1 = Implies(And(Or(X,Y), X), Not(Y))
    s.add(Not(C1))
    # I believe it's not valid because if x is true doesnt mean that y is false because or doesnt mean 'only' one or the other
    
    # Run the Z3 model finder, capturing "sat"
    # or "unsat" as the return value 
    r = s.check()


    
    if (r == unsat) :
        print("C1 is valid")
    else : #counter example: look for model of not c1
        print("Heres a counter example: ", s.model) 

# 2. X, Y ⊢ X ∧ Y              -- and introductio
# n  x ^ y  x ^ y if we know x and y is true then we know they are both true
=======
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    
    s.add(Not(C1))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    if (r == unsat):
        print("C1 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model() )


>>>>>>> 5779e4baff43c1917c72c67c9391c88923ed1090
hw2()