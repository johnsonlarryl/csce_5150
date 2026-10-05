<!-- ABOUT THE PROJECT -->

## About The Project
<div id="readme-top"></div>

# Longest Common Subsequence (LCS)

The **Longest Common Subsequence (LCS)** problem is a sequence comparison problem solved using **Dynamic Programming (DP)**.

Given two sequences, `X` and `Y`, the objective is to find the **longest subsequence common to both sequences** while preserving the relative order of the characters.

A subsequence does **not** require the characters to be contiguous.

For example:

```text
X = ABC
Y = AEC
```

The longest common subsequence is:

```text
AC
```

Therefore, the LCS length is `2`.

---

<b>Table 1 – Dynamic Programming Project Archetype</b>

| Type                | Sub Type            | Algorithm                        |
|---------------------|---------------------|----------------------------------|
| Dynamic Programming | Sequence Comparison | Longest Common Subsequence (LCS) |

<p align="right">(<a href="#readme-top">back to top</a>)

---

## Overview

Given two sequences:

![](https://latex.codecogs.com/png.latex?X%20%3D%20x_%7B1%7D%2Cx_%7B2%7D%2C%5Cldots%2Cx_%7Bm%7D)

and:

![](https://latex.codecogs.com/png.latex?Y%20%3D%20y_%7B1%7D%2Cy_%7B2%7D%2C%5Cldots%2Cy_%7Bn%7D)

the goal is to find the longest sequence:

![](https://latex.codecogs.com/png.latex?Z%20%3D%20z_%7B1%7D%2Cz_%7B2%7D%2C%5Cldots%2Cz_%7Bk%7D)

that is a subsequence of both `X` and `Y`.

The order of the characters must be preserved, but the characters do not have to appear next to one another.

---

## Dynamic Programming Formulation

Let:

![](https://latex.codecogs.com/png.latex?c%5Bi%2Cj%5D)

represent the **length of the Longest Common Subsequence of the prefixes**:

![](https://latex.codecogs.com/png.latex?X_i%20%3D%20x_%7B1%7D%2Cx_%7B2%7D%2C%5Cldots%2Cx_%7Bi%7D)

and:

![](https://latex.codecogs.com/png.latex?Y_j%20%3D%20y_%7B1%7D%2Cy_%7B2%7D%2C%5Cldots%2Cy_%7Bj%7D)

The recurrence is:

![](https://latex.codecogs.com/png.latex?c%5Bi%2Cj%5D%20%3D%20%5Cbegin%7Bcases%7D%200%20%26%20i%3D0%20%5Ctext%7B%20or%20%7D%20j%3D0%20%5C%5C%20c%5Bi-1%2Cj-1%5D%20%2B%201%20%26%20x_i%3Dy_j%20%5C%5C%20%5Cmax%5C%7Bc%5Bi-1%2Cj%5D%2C%20c%5Bi%2Cj-1%5D%5C%7D%20%26%20x_i%20%5Cneq%20y_j%20%5Cend%7Bcases%7D)

---

## Algorithm Steps

1. **Initialize the DP Table**
   * Let `m` be the length of `X`.
   * Let `n` be the length of `Y`.
   * Create a table `c` with `m + 1` rows and `n + 1` columns.
   * Initialize the first row and first column to `0`.

   ![](https://latex.codecogs.com/png.latex?c%5Bi%2C0%5D%20%3D%200)

   ![](https://latex.codecogs.com/png.latex?c%5B0%2Cj%5D%20%3D%200)

2. **Compare the Current Characters**
   * For each `i = 1, ..., m` and `j = 1, ..., n`, compare:

   ![](https://latex.codecogs.com/png.latex?x_i%20%5Ctext%7B%20and%20%7D%20y_j)

3. **Characters Match**
   * If the two current characters match:

   ![](https://latex.codecogs.com/png.latex?x_i%20%3D%20y_j)

   * The matching character contributes one additional character to the common subsequence.
   * Use the LCS length from the prefixes before both current characters and add `1`:

   ![](https://latex.codecogs.com/png.latex?c%5Bi%2Cj%5D%20%3D%20c%5Bi-1%2Cj-1%5D%20%2B%201)

   * This corresponds to moving **diagonally** in the DP table.

4. **Characters Do Not Match**
   * If:

   ![](https://latex.codecogs.com/png.latex?x_i%20%5Cneq%20y_j)

   * The current cell receives the larger value from the cell directly above or directly to the left:

   ![](https://latex.codecogs.com/png.latex?c%5Bi%2Cj%5D%20%3D%20%5Cmax%5C%7Bc%5Bi-1%2Cj%5D%2C%20c%5Bi%2Cj-1%5D%5C%7D)

5. **Determine the LCS Length**
   * Continue until every cell has been evaluated.
   * The bottom-right entry contains the LCS length for the complete sequences:

   ![](https://latex.codecogs.com/png.latex?c%5Bm%2Cn%5D)

6. **Determine the LCS**
   * Starting at `c[m,n]`, trace backward through the matrix.
   * When the current characters match, that character belongs to the LCS.
   * Move diagonally to `c[i-1,j-1]`.
   * When the characters do not match, move toward the larger value: either up or left.
   * Continue until the first row or first column is reached.
   * Reverse the collected characters to obtain the LCS in its original order.

---

## Example

Given:

```python
X = "ABC"
Y = "AEC"
```

The DP table begins with zeros:

```text
        Y
        -  A  E  C
     -  0  0  0  0
X    A  0
     B  0
     C  0
```

### Row 1 — Character `A`

`A` matches the first character of `Y`.

```text
Row 1 (A): [0, 1, 1, 1]
```

### Row 2 — Character `B`

`B` does not match `A`, `E`, or `C`, so the previous LCS length is carried forward.

```text
Row 2 (B): [0, 1, 1, 1]
```

### Row 3 — Character `C`

At the final position:

```text
X[3] = C
Y[3] = C
```

The characters match, so:

![](https://latex.codecogs.com/png.latex?c%5B3%2C3%5D%20%3D%20c%5B2%2C2%5D%20%2B%201)

Since:

![](https://latex.codecogs.com/png.latex?c%5B2%2C2%5D%20%3D%201)

then:

![](https://latex.codecogs.com/png.latex?c%5B3%2C3%5D%20%3D%201%20%2B%201%20%3D%202)

The completed row is:

```text
Row 3 (C): [0, 1, 1, 2]
```

---

## Final DP Matrix

```text
          Y
          -    A    E    C
       --------------------
-         0    0    0    0
A         0    1    1    1
B         0    1    1    1
C         0    1    1    2
```

The bottom-right value is:

![](https://latex.codecogs.com/png.latex?c%5B3%2C3%5D%20%3D%202)

Therefore:

```text
LCS = AC
LCS Length = 2
```

---

## Complexity

For sequences with lengths `m` and `n`, every pair of sequence positions is evaluated once.

### Time Complexity

![](https://latex.codecogs.com/png.latex?O%28mn%29)

### Space Complexity

![](https://latex.codecogs.com/png.latex?O%28mn%29)

---