"""
verify.py
---------
Verifies eigenvalues and eigenvectors for matrix A = [[2,1],[1,2]]
by algebraic substitution and NumPy matrix multiplication.

Matrix A:
    [ 2  1 ]
    [ 1  2 ]

Eigenvalues:
    λ₁ = 3
    λ₂ = 1

Eigenvectors:
    v₁ = [ 1,  1 ]ᵀ for λ₁ = 3
    v₂ = [ 1, -1 ]ᵀ for λ₂ = 1
"""

import numpy as np

# 1. Define Matrix A
A = np.array([
    [2.0, 1.0],
    [1.0, 2.0]
])

# 2. Define expected eigenvalues and eigenvectors
lambda_1 = 3.0
v_1 = np.array([1.0, 1.0])

lambda_2 = 1.0
v_2 = np.array([1.0, -1.0])

print("=" * 60)
print("EIGENPAIR SUBSTITUTION VERIFICATION")
print("Matrix A:")
print(A)
print("=" * 60)

# Check 1: Characteristic equation det(A - λI) = 0
I = np.eye(2)
det_1 = np.linalg.det(A - lambda_1 * I)
det_2 = np.linalg.det(A - lambda_2 * I)

print(f"\n1. Characteristic Equation Check det(A - λI) == 0:")
print(f"   det(A - {lambda_1}I) = {det_1:.6f}")
print(f"   det(A - {lambda_2}I) = {det_2:.6f}")
assert np.isclose(det_1, 0.0), f"det(A - {lambda_1}I) != 0"
assert np.isclose(det_2, 0.0), f"det(A - {lambda_2}I) != 0"
print("   -> Both determinant checks PASSED!")

# Check 2: Direct substitution Av = λv
Av1 = A @ v_1
lambda1_v1 = lambda_1 * v_1

print(f"\n2. Verification of Eigenpair (λ₁ = 3, v₁ = [1, 1]ᵀ):")
print(f"   A @ v₁        = {Av1}")
print(f"   λ₁ * v₁       = {lambda1_v1}")
assert np.allclose(Av1, lambda1_v1), f"Mismatch: A @ v₁ != λ₁ * v₁"
print("   -> Av₁ == λ₁v₁ PASSED!")

Av2 = A @ v_2
lambda2_v2 = lambda_2 * v_2

print(f"\n3. Verification of Eigenpair (λ₂ = 1, v₂ = [1, -1]ᵀ):")
print(f"   A @ v₂        = {Av2}")
print(f"   λ₂ * v₂       = {lambda2_v2}")
assert np.allclose(Av2, lambda2_v2), f"Mismatch: A @ v₂ != λ₂ * v₂"
print("   -> Av₂ == λ₂v₂ PASSED!")

# Check 3: Determinant as product of eigenvalues
det_A = np.linalg.det(A)
product_lambdas = lambda_1 * lambda_2
print(f"\n4. Determinant vs Product of Eigenvalues:")
print(f"   det(A)        = {det_A:.4f}")
print(f"   λ₁ * λ₂       = {product_lambdas:.4f}")
assert np.isclose(det_A, product_lambdas), f"det(A) != λ₁ * λ₂"
print("   -> det(A) == λ₁ * λ₂ PASSED!")

print("\n" + "=" * 60)
print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
print("=" * 60)
