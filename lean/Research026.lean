import Mathlib

/-!
Research 026: algebraic certificate fragments.
DRAFT: not compiled in the current execution environment.
These lemmas do not establish the infinite tail, density criterion, or RH.
-/

namespace Research026

theorem residual_square_bound (r b : ℝ) (hl : -b ≤ r) (hu : r ≤ b) :
    r^2 ≤ b^2 := by
  have h1 : 0 ≤ b - r := sub_nonneg.mpr hu
  have h2 : 0 ≤ b + r := by linarith
  nlinarith [mul_nonneg h1 h2]

theorem quadratic_update (w r d f : ℝ) :
    w * (r - d*f)^2 = w*r^2 - 2*w*r*d*f + w*d^2*f^2 := by
  ring

#print axioms residual_square_bound
#print axioms quadratic_update

end Research026
