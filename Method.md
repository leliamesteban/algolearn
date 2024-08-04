# Decide on a data structure / algorithm

## Option 1: 0 < n < 100 - Brute force - Worse than O(n²)

If n is very small (n < 100), any answer will be good enough, so look for simplicity and use techniques such as backtracking or recursion.

## Option 2: 100 < n < 1000 - Nested loops - O(n²)

If n is still small enough to allow inefficiency, look for nested loops and inefficient solutions.

## Option 3: 1000 < n < 10 000 - Presorting and / or simulating nested loops- O(n log(n)) to O(n)

If n is very big, you need an efficient solution, so you probably need to split it into steps (sorting and iterating for example), or use faster solutions.

Sorting takes O(n log(n)).

## Option 4: 1,000,000 < n - Binary search or clever tricks - O(log(n)) or constant

O(log(n)) just means the time it takes increases by 1 every time the input increases by x10, which is a very slow increase.

# Methods

## Two pointers

## Sliding subarray / sliding window

Two pointers but applied to subarrays instead of traversing the array.

## Prefix sum / running sum - O(n)

Return an array containing the cumulative sum of every element in the input array.

```python
return [sum(inputArray[0:i + 1]) for i in range(len(inputArray))]
```
