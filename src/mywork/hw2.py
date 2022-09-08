from z3 import *



def hw2():
    
    
    # Create z3 variable(s) representing the unknown
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
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
hw2()