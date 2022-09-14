# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


def hw2():
    
    
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    
    s.add(Not(C1))
    r = s.check()
    
    if (r == unsat):
        print("C1 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    
    s.reset()
    # I believe it's not valid
    
    # 2. X, Y ⊢ X ∧ Y              -- and introduction
    C2 = Implies(And(X,Y),And(X,Y))
    s.add(Not(C2))
    r = s.check()
    
    if (r == unsat):
        print("C2 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()

    # # 3. X ∧ Y ⊢ X                 -- and elimination left
    C3 = Implies(And(X,Y),X)
    s.add(Not(C3))
    r = s.check()
    
    if (r == unsat):
        print("C3 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    
    # # 4. X ∧ Y ⊢ Y                 -- and elimination right
    C4 = Implies(And(X,Y),Y)
    s.add(Not(C4))
    r = s.check()
    
    if (r == unsat):
        print("C4 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # # 5. ¬¬X ⊢ X                   -- negation elimination 
    C5 = Implies(Not(Not(X)),X)
    s.add(Not(C5))
    r = s.check()
    
    if (r == unsat):
        print("C5 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # # 6. ¬(X ∧ ¬X)                 -- no contradiction
    C6 = Not(And(X,Not(X)))
    s.add(Not(C6))
    r = s.check()
    
    if (r == unsat):
        print("C6 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # # 7. X ⊢ X ∨ Y                 -- or introduction left
    C7 = Implies(X,Or(X,Y))
    s.add(Not(C7))
    r = s.check()
    
    if (r == unsat):
        print("C7 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # # 8. Y ⊢ X ∨ Y                 -- or introduction right
    C8 = Implies(Y,Or(X,Y))
    s.add(Not(C8))
    r = s.check()
    if (r == unsat):
        print("C8 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # # 9. X → Y, ¬X ⊢ ¬ Y           -- denying the antecedent
    C9 = Implies(X,Or(X,Y))
    s.add(Not(C9))
    r = s.check()
    if (r == unsat):
        print("C9 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 10. X → Y, Y → X ⊢ X ↔ Y      -- iff introduction
    C10 = Implies((And(Implies(X,Y), Implies(Y,X))),And(Implies(X,Y),Implies(Y,X)))
    s.add(Not(C10))
    r = s.check()
    if (r == unsat):
        print("C10 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 11. X ↔ Y ⊢ X → Y            -- iff elimination left
    C11 = Implies((And(Implies(X,Y), Implies(Y,X))),And(Implies(X,Y),Implies(Y,X)))
    s.add(Not(C11))
    r = s.check()
    if (r == unsat):
        print("C11 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 12. X ↔ Y ⊢ Y → X            -- iff elimination right
    C12 = Implies(And(Implies(X,Y), Implies(Y,X)),Implies(Y,X))
    s.add(Not(C12))
    r = s.check()
    if (r == unsat):
        print("C12 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 13. X ∨ Y, X → Z, Y → Z ⊢ Z  -- or elimination
    C13 = Implies(And(Or(X,Y),Implies(X,Z),Implies(Y,Z)),Z)
    s.add(Not(C13))
    r = s.check()
    if (r == unsat):
        print("C13 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 14. X → Y, Y ⊢ X             -- affirming the conclusion
    C14 = Implies(And(Implies(X,Y),Y),X)
    s.add(Not(C14))
    r = s.check()
    if (r == unsat):
        print("C14 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 15. X → Y, X ⊢ Y             -- arrow elimination
    C15 = Implies(And(Implies(X,Y),X),Y)
    s.add(Not(C15))
    r = s.check()
    if (r == unsat):
        print("C15 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 16. X → Y, Y → Z ⊢ X → Z     -- transitivity of → 
    C16 = Implies(And(Implies(X,Y),X),Y)
    s.add(Not(C16))
    r = s.check()
    if (r == unsat):
        print("C16 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 17. X → Y ⊢ Y → X            -- converse
    C17 = Implies(Implies(X,Y),Implies(Y,X))
    s.add(Not(C17))
    r = s.check()
    if (r == unsat):
        print("C17 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 18. X → Y ⊢ ¬Y → ¬X          -- contrapositive
    C18 = Implies(Implies(X,Y),Implies(Not(Y),Not(X)))
    s.add(Not(C18))
    r = s.check()
    if (r == unsat):
        print("C18 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y       -- DeMorgan #1 (¬ distributes over ∨)
    C19 = And(Implies(Not(And(X,Y)), And(Not(X),Not(Y))), Implies(And(Not(X),Not(Y)),Not(And(X,Y))))
    s.add(Not(C19))
    r = s.check()
    if (r == unsat):
        print("C19 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()
    # 20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y       -- Demorgan #2 (¬ distributes over ∧)
    C20 = And(Implies(Not(Or(X,Y)), And(Not(X),Not(Y))), Implies(And(Not(X),Not(Y)),Not(Or(X,Y))))
    s.add(Not(C20))
    r = s.check()
    if (r == unsat):
        print("C20 is valid")
    else :
        print("Here's a counter-example: ", s.model() )
    s.reset()

hw2()