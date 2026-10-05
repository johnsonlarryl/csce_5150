<!-- ABOUT THE PROJECT -->

## About The Project
<div id="readme-top"></div>

# 0/1 Knapsack Problem

The **0/1 Knapsack Problem** is a combinatorial optimization problem solved using **Dynamic Programming (DP)**.

Given a collection of items, where each item has a **weight** and an associated **profit**, the objective is to select a subset of items that maximizes the total profit without exceeding the maximum capacity of the knapsack.

Each item can be selected **once (1)** or **not selected (0)**.

---

<b>Table 1 – Dynamic Programming Project Archetype</b>

| Type                 | Sub Type                  | Algorithm             |
|----------------------|---------------------------|-----------------------|
| Dynamic Programming  | Combinatorial Optimization | 0/1 Knapsack Problem |

<p align="right">(<a href="#readme-top">back to top</a>)


---

## Overview

Given **n items**, each item has a weight and profit:

![](https://latex.codecogs.com/png.latex?w_i%20%3D%20%5Ctext%7Bweight%20of%20item%20%7Di)

![](https://latex.codecogs.com/png.latex?p_i%20%3D%20%5Ctext%7Bprofit%20of%20item%20%7Di)

The knapsack has a maximum capacity:

![](https://latex.codecogs.com/png.latex?W%20%3D%20%5Ctext%7Bmaximum%20knapsack%20capacity%7D)

The objective is to maximize:

![](https://latex.codecogs.com/png.latex?%5Cmax%20%5Csum_%7Bi%3D1%7D%5En%20p_i%20x_i)

subject to:

![](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D1%7D%5En%20w_i%20x_i%20%5Cleq%20W)

where:

![](https://latex.codecogs.com/png.latex?x_i%20%5Cin%20%5C%7B0%2C1%5C%7D)

An item is therefore either **included** or **excluded** from the knapsack.

---

## Dynamic Programming Formulation

Let:

![](https://latex.codecogs.com/png.latex?c%5Bi%2Cw%5D)

represent the **maximum profit that can be obtained using the first `i` items with a knapsack capacity of `w`**.

The recurrence is:

![](https://latex.codecogs.com/png.latex?c%5Bi%2Cw%5D%20%3D%20%5Cbegin%7Bcases%7D%200%20%26%20i%3D0%20%5Ctext%7B%20or%20%7D%20w%3D0%20%5C%5C%20c%5Bi-1%2Cw%5D%20%26%20w_i%20%3E%20w%20%5C%5C%20%5Cmax%5C%7Bc%5Bi-1%2Cw%5D%2C%20p_i%20%2B%20c%5Bi-1%2Cw-w_i%5D%5C%7D%20%26%20w_i%20%5Cleq%20w%20%5Cend%7Bcases%7D)

---

## Algorithm Steps

1. **Initialize the DP Table**
   * Create a table with `n + 1` rows and `W + 1` columns.
   * Initialize row `0` to zero because no profit can be obtained when no items are available.

2. **Evaluate Each Item**
   * Process items from `1` through `n`.
   * For each item, evaluate every possible knapsack capacity from `0` through `W`.

3. **Exclude the Item**
   * If the current item's weight is greater than the current capacity, the item cannot be selected:

     ![](https://latex.codecogs.com/png.latex?c%5Bi%2Cw%5D%20%3D%20c%5Bi-1%2Cw%5D)

4. **Include or Exclude the Item**
   * If the item fits, compare the profit obtained by excluding the item with the profit obtained by including it:

     ![](https://latex.codecogs.com/png.latex?c%5Bi%2Cw%5D%20%3D%20%5Cmax%5C%7Bc%5Bi-1%2Cw%5D%2C%20p_i%20%2B%20c%5Bi-1%2Cw-w_i%5D%5C%7D)

5. **Determine the Optimal Profit**
   * The bottom-right entry of the DP table contains the maximum achievable profit:

     ![](https://latex.codecogs.com/png.latex?c%5Bn%2CW%5D)

6. **Backtrack to Determine Selected Items**
   * Starting at `c[n,W]`, compare the current value with the value directly above it.
   * If the values differ, the current item contributed to the optimal solution.
   * Subtract its weight from the remaining capacity and continue upward.

---

## Example

Given:

```python
weights = [3, 2, 4, 5, 1]
profits = [50, 40, 70, 80, 10]
capacity = 7