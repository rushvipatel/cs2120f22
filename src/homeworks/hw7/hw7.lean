import data.set

/- #1

Formally prove that if there's an object, a, of some 
type, α, having some property (satisfying a predicate), 
P, then not every object of type α fails to have property, 
P. Add a brief comment before each line of your proof 
script to provide what amounts to the outline of a good
English language proof.
-/

example (α : Type) (P : α → Prop) : (∃ a, P a) → (¬(∀ x, ¬ P x)) :=
begin
  intros a b,
  cases a with x y,
  have noty := b x,
  contradiction,
end


/- Extra credit. 

The converse of this proposition is clasically true. If
not every object lacks propery, P, then there must be some
object that has it. If you try to prove the converse in
our constructive logic, what happens? Show you work, and
then briefly but clearly explain exactly what goes wrong.
-/
-- We cannot prove this without classical reasoning


/- #2

Consider the following binary relation, r, with domain
and co-domain both being ℕ. For each following question,
answer yes/no then briefly justify your answer.

( domain = ℕ, r = {(0,0),(1,1),(2,2)}, co-domain=ℕ )

A. Is this relation reflexive? No, the set holds 0 1 and 2 but the domain is all real numbers
B. Is this relation symmetric? Yes, because for every a and b in the set, b = a and a = b
C. Is this relation transitive? Yes, a = b and b = c which means a = c
D. Is this relation an equivalence relation? No, since it is not reflexive
-/



/- #3

A binary relation, r, is said to be *anti-symetric* 
if, for all values in its domain, a and b, if r a b 
and if r b a then a = b. Give an example of a familiar
arithmetic relation that's anti-symmetric, and briefly
explain why it's so.
-/
-- division is an anti-symmetric relation for positive integers because if a is divisible by b and 
-- b is divisible by a then a = b 
--


/- #4
A binary relation, r, is said to be *asymmetric* if
whenever, for any a and b, if r a b then ¬ r b a. Be
careful to note that asymmetry and antisymmetry are
different properties.  Answer each of the following 
sub-questions. We give you a formal definition of anti
-/

def is_asymmetric 
  {α : Type} 
  (r : α → α → Prop) : Prop 
  := ∀ (a b : α), r a b → ¬ r b a 

/- A.

Name a familar arithmetic relation that's asymmetric
and briefly explain why you think it's asymmetric.

Answer here: a - b is asymmetric because a - b is in the relation but b-a is not
-/
/- C: 

An object cannot be related to itself in an asymmetric
relation. First, complete the following informal proof
of this statement.

Proof: Assume α, r, and a are as given (and in particular
assume that r is asymmetric). Now assume r a a. <finish
the proof>. 

Answer here (rest of proof): ¬r a a is true by contradiction
-/ 

/- D.

Now prove a closely related proposition formally. 
Add a comment to each line of your formal proof 
so as to construct a good skeleton for a fluent 
English language proof.
-/

example
  (α : Type) 
  (r : α → α → Prop)
  (h : is_asymmetric r) :
¬ ∃ (a : α), r a a :=
begin
-- proof by negation
  assume h, -- assume premise
  cases h with a b, -- cases 
  unfold is_asymmetric at h,
  have h2 := h a a, --apply a to h
  have nraa := h2 b, --apply ¬raa to raa 
  contradiction, --cannot have a proof of both raa and ¬raa
end


/- #5
Prove that equality on an inhabited (non-empty) type 
is not assymetric. In the following formalization we
assume there is a value (a : α), which establishes 
that α is inhabited.
-/

example (α : Type) (a : α): ¬ is_asymmetric (@eq α) :=
begin
  assume h,
  unfold is_asymmetric at h,
  have x := h a a,
  have neq := x rfl,
  contradiction,
end

/- Extra credit: What exactly goes wrong in a formal 
proof if you drop the "inhibitedness" condition? Give
as much of a formal proof as you can then explain why
it can't be completed (if it can't!).
-/



/- #6
Two natural numbers, p and q, are said to be 
"equivalent mod m" if p % m = q % m, which makes
"equivalence mod m" a binary relation on natural
numbers. Here's a formal definition of this binary
relation on the natural numbers (given an m).
-/

def equiv_mod_m (m : ℕ) : ℕ → ℕ → Prop := 
  λ p q : ℕ, p % m = q % m

/-
Prove using Lean's definition of "equivalence" that 
equiv_mod_m is an equivalence relation for any natural
number, m. Here you'll also use Lean's definitions of
reflexive, symmetric, and transitive. They are as we
have covered in class. 
-/

example : ∀ m : ℕ, equivalence (equiv_mod_m m) :=
begin
  assume h,
  unfold equivalence equiv_mod_m,
  split,
  unfold reflexive,
  assume j,
  exact rfl,
  split,
  unfold symmetric,
  assume a b,
  assume h,
  rw h,
  unfold transitive,
  assume a b c d e,
  rw d,
  rw e,
end



/- #7
Consider the relation, tin_rel, that associates people 
with U.S. taxpayer id numbers, which we'll represent as 
natural numbers here. 

Assume this relation is single-valued. Which of the 
following properties does this relation have? Give
a very brief justification of each answer. Assume
the domain is all living persons, and the co-domain
is all natural numbers.

-- it's a function: yes, its single valued
-- it's total: no, because there are people in the us with id numbers
-- it's injective (where "): yes, every output has one input
-- it's surjective (where the co-domain is all ℕ): no, not every possible output does not have an input
-- it's strictly partial: yes, not every input has an output
-- it's bijective: no, not both injective and surjective
-/



/- #8
Suppose r is the empty relation on the natural 
numbers. Which of the following properties does
it have? Explain each answer enough to show you
know why your answer is correct.

-- reflexive: no, there are no elements in the relation which means it cannot be related it itself
-- symmetric: yes, since the antecedent is always false
-- transitive: yes, since the antecedent is always false
-/



/- #9
Here's a formal definition of this empty relation.
That there are no constructors given here means there 
are no proofs, which is to say that no pair can be 
proved to be in this relation, so it must be empty.
-/

inductive empty_rel : ℕ → ℕ → Prop

/-
Formally state and prove you answer for each of the
three properties. That is, for each property assert
either that empty_rel does have it or does not have it, 
then prove your assertion. Include English-language 
comments on each line to give the essential elements 
of a good English language proof.
-/


example : ¬reflexive empty_rel :=
begin
unfold reflexive,
assume h, -- assume premise and prove false
let x := h 0, --let x be the empty relation
cases x, -- cases for relation
end

example : symmetric empty_rel :=
begin
unfold symmetric, -- unfold definition
assume a b h,-- empty relation with a and b
cases h, -- cases applied with h
end

example : transitive empty_rel :=
begin
assume a b c h k, -- assume empty relations with ab and bc
cases h, -- cases with a b
end

/- #10
A relation, r, is said to have the property of being 
a *partial order* if it's reflexive, anti-symmetric,
and transitive. Give a brief English language proof 
that the subset relation on the subsets of any set, 
S (of objects of some type), is a partial order. 

Pf:  
Suppose S is a set, with a ⊆ S and b ⊆ S subsets. Then

1. reflexive, a is a subset of itself
2. anti-symmetric, if a is a subset of b and b is a subset of a then a is equal to b
3. transitive, if a is a subset of b and b is a subset of c then a is a subset of c

QED.
-/



/- #11 
Finally we return again to DeMorgan's laws, but
now for sets. You'll recall that these "laws" as we
have seent them so far tell us how to distribute ¬  
over ∨ and over ∧. You will also recall that set
intersection (∩) is defined by the conjunction (∧) 
of the membership predicates, set union (∪) by the
disjunction (∨), and set complement (Sᶜ for a set,
S), by negation (¬). It makes sense to hypothesize 
that we can recast DeMorgan's laws in terms of the
distribution of complement over set union and set
intersection. Indeed we can. Your job is to state
and prove (formally) the first DeMorgan laws for 
sets, which states that the complement of a union
of any two sets equals the intersection of their 
complements.

Hint: To prove that two sets are equal, S = T, use
the ext tactic. It applies a bew axiom (called set 
extensionality) that states that to prove S = T it 
suffices to prove S ↔ T, viewing the sets as being
defined by their logical membership predicates. You
know how to handle bi-implications. The rest you 
can do by seeing "not," "and," and "or" in place 
of complement, conjunction, and disjuction, resp.  
-/

example 
  (α : Type) 
  (a b: set α) :
  (a ∪ b)ᶜ = aᶜ ∩ bᶜ := 
begin
  ext,
  split,

  assume notaub, 
  split, 
  assume h,
  have aub := or.inl h, 
  have f := notaub aub,
  contradiction,

  assume j,
  have aub := or.inr j, 
  have f := notaub aub,
  contradiction,

  assume acbc,
  assume aub,
  cases aub with a b,
  have ac := acbc.left,
  contradiction,
  have bc := acbc.right,
  contradiction,

end


