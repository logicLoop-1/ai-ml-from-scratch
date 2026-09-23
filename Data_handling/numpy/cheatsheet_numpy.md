# NumPy Cheatsheet

## Creating Arrays
| Code | Result |
|---|---|
| `np.array([1,2,3])` | 1D array |
| `np.zeros(5)` | array of 5 zeros |
| `np.ones((2,3))` | 2×3 array of ones |
| `np.arange(0,10,2)` | `[0 2 4 6 8]` |
| `np.linspace(0,1,5)` | 5 evenly spaced points between 0 and 1 |
| `arr.reshape(r, c)` | reshape without changing data (total elements must match) |

## Attributes
| Code | Meaning |
|---|---|
| `.shape` | dimensions, e.g. `(3, 4)` |
| `.ndim` | number of dimensions |
| `.size` | total number of elements |
| `.dtype` | data type stored |

## Indexing / Slicing
| Code | Meaning |
|---|---|
| `arr[i]` | single element |
| `matrix[i, j]` | row i, column j |
| `matrix[:, j]` | entire column j, all rows |
| `matrix[i, :]` | entire row i, all columns |
| `matrix[1:, :2]` | rows 1 onward, first 2 columns |

## Element-wise Operations (vectorized, no loop)
| Code | Result |
|---|---|
| `a + b`, `a - b` | element-wise add/subtract |
| `a * b` | element-wise multiply — SAME SHAPE as input |
| `a ** 2` | element-wise power |
| `a > 5` | boolean array, element-wise comparison |

## Dot Product / Matrix Multiplication
| Code | Result |
|---|---|
| `np.dot(a, b)` | dot product — ONE number (scalar) |
| `a @ b` | same as `np.dot()`, different syntax |

**Key distinction:** `*` keeps the same shape (element-by-element). `dot`/`@` collapses to a single scalar (multiply, then sum).

## Boolean Masking
```python
arr[arr > 30]   # keep only values matching the condition
```

## Aggregation
| Code | Result |
|---|---|
| `.sum()` `.mean()` `.std()` `.min()` `.max()` | summary stats over the whole array |
| `.argmax()` | INDEX of the max value, not the value itself |
| `.mean(axis=1)` | one result PER ROW (columns get squashed) |
| `.mean(axis=0)` | one result PER COLUMN (rows get squashed) |

**Memory anchor:** ask "do I want this per row, per column, or as one total number?" — that decides the axis.

## Broadcasting
```python
matrix + vector   # smaller array auto-stretches to match every row
```
NumPy stretches the smaller array's shape to match the bigger one, instead of requiring a manual loop.

## Common Mistakes
- Confusing `a * b` (element-wise, same shape) with `np.dot(a, b)` (single scalar) — same-looking code, very different results.
- Forgetting which axis squashes which dimension (`axis=1` → per row, `axis=0` → per column).
- Using `>` vs `>=` carelessly in boolean masking when the exercise wording specifies one or the other.
- Assuming reshape works with any numbers — total element count must stay the same.