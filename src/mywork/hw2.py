# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def hw2():
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    
    s.add(Not(C1))
    s.reset()
    # I believe it's not valid
    
    # 2. X, Y ⊢ X ∧ Y              -- and introduction
    C2 = Implies(And(X,Y),And(X,Y))
    s.add(Not(C1))
    s.reset()

    # 3. X ∧ Y ⊢ X                 -- and elimination left
    C3 = Implies(And(X,Y),X)
    s.add(Not(C3))
    s.reset()
    
    # 4. X ∧ Y ⊢ Y                 -- and elimination right
    C4 = Implies(And(X,Y),Y)
    s.add(Not(C4))
    s.reset()
    # 5. ¬¬X ⊢ X                   -- negation elimination 
    C5 = Implies(Not(Not(X)),X)
    s.add(Not(C5))
    s.reset()
    # 6. ¬(X ∧ ¬X)                 -- no contradiction
    C6 = Not(And(X,Not(X)))
    s.add(Not(C6))
    s.reset()
    # 7. X ⊢ X ∨ Y                 -- or introduction left
    C7 = Implies(X,Or(X,Y))
    s.add(Not(C7))
    s.reset()
    # 8. Y ⊢ X ∨ Y                 -- or introduction right
    C8 = Implies(y,Or(X,Y))
    s.add(Not(C8))
    s.reset()
    # 9. X → Y, ¬X ⊢ ¬ Y           -- denying the antecedent
    C9 = Implies(X,Or(X,Y))
    s.add(Not(C9))
    s.reset()
    # 10. X → Y, Y → X ⊢ X ↔ Y      -- iff introduction
    # 11. X ↔ Y ⊢ X → Y            -- iff elimination left
    # 12. X ↔ Y ⊢ Y → X            -- iff elimination right
    # 13. X ∨ Y, X → Z, Y → Z ⊢ Z  -- or elimination
    # 14. X → Y, Y ⊢ X             -- affirming the conclusion
    # 15. X → Y, X ⊢ Y             -- arrow elimination
    # 16. X → Y, Y → Z ⊢ X → Z     -- transitivity of → 
    # 17. X → Y ⊢ Y → X            -- converse
    # 18. X → Y ⊢ ¬Y → ¬X          -- contrapositive
    # 19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y       -- DeMorgan #1 (¬ distributes over ∨)
    # 20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y       -- Demorgan #2 (¬ distributes over ∧)
  
    r = s.check()
    
    # If there's a model/solution return it 
    if (r == unsat):
        print("C1 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model() )


hw2()