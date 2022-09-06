from z3 import *

def isValid(P) :
    s = Solver()
    s.add(Not(P)) # replace True with required declarative spec
    return (s.check()==unsat)
# checks if not(x or not x) is unsat

# Declare X to be a Z3 Bool variable
X = Bool('X')
# Print the result of testing (X Or Not X) for validity
print(isValid(Or(X, Not(X)))) # true because x is valid
# Print the result of testing (X And Not X) for validity
print(isValid(And(X, Not(X)))) # false because x is not valid