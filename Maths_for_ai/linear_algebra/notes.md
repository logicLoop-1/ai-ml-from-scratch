# Linear Algebra Notes

Worked by hand first, then verified with NumPy.
See `numpy_verification.py` in this folder for the code confirming these results.

---

## 1. Vectors

A vector is an ordered list of numbers. Geometrically, it represents a point in space
(or an arrow from the origin to that point).

**Vector addition** — add corresponding elements:

$$
[2, -1, 3] + [4, 5, -2] = [6, 4, 1]
$$

**Scalar multiplication** — multiply every element by the same number:

$$
4 \times [1, -2, 3] = [4, -8, 12]
$$

**Magnitude (length) of a vector** — Pythagorean theorem, extended:

$$
|[6, 8]| = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10
$$

---

## 2. Dot Product

The dot product takes two vectors and returns a **single number (scalar)** — multiply
corresponding elements, then sum everything.

$$
[1, 2, 3] \cdot [4, 5, 6] = (1 \times 4) + (2 \times 5) + (3 \times 6) = 4 + 10 + 18 = 32
$$

### Why it matters for ML

The dot product is how a model combines inputs with weights — this is the core
mechanic behind linear regression and every neuron in a neural network.

**Example — predicting a house price:**

- Features: `[size, bedrooms, age] = [2000, 4, 2]`
- Weights: `[150, 20000, -1000]`

$$
(2000 \times 150) + (4 \times 20000) + (2 \times -1000) = 300000 + 80000 - 2000 = 378000
$$

The negative weight on `age` correctly pulls the predicted price down for older houses.

---

## 3. Matrices

A matrix is a grid of numbers — rows × columns. In ML, a matrix often represents a
whole dataset: each row is one example, each column is one feature.

---

## 4. Matrix Multiplication

Each entry in the result is the dot product of a row from the first matrix and a
column from the second.

$$
\begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}
\times
\begin{bmatrix} 1 & 3 \\ 2 & 1 \end{bmatrix}
=
\begin{bmatrix} 2 & 6 \\ 7 & 6 \end{bmatrix}
$$

Worked out:
- Top-left: `(2×1) + (0×2) = 2`
- Top-right: `(2×3) + (0×1) = 6`
- Bottom-left: `(1×1) + (3×2) = 7`
- Bottom-right: `(1×3) + (3×1) = 6`

### The rule: inner dimensions must match

For `A (m × n) × B (n × p)`, the number of **columns in A** must equal the number of
**rows in B**. The result has shape `m × p`.

**Why:** each result entry is a dot product of a row from A and a column from B — and
a dot product requires both vectors to be the same length. If A has 3 columns, its
rows have 3 numbers; if B has 2 rows, its columns have 2 numbers. A 3-number list and
a 2-number list can't be paired element-by-element, so the multiplication is undefined.

This is why two `2×3` matrices **cannot** be multiplied directly (`3 ≠ 2`) — one would
need to be transposed first to make the inner dimensions line up.

---

## 5. Still to Come

- Eigenvalues & eigenvectors — deferred until PCA (unsupervised learning section),
  since they only make sense in that context.
- Matrix transpose, inverse, identity matrix — as needed by later algorithms.
- Vector norms (L1 vs L2) — needed for regularization (Ridge/Lasso regression).