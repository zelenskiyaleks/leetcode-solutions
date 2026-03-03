# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Topic:** Arrays, Greedy, Kadane Pattern

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on the i-th day.

You want to maximize your profit by choosing:
- one day to buy
- a different future day to sell

Return the maximum possible profit.
If no profit is possible, return 0.

## Approach

We use a greedy strategy:

- Track the minimum price seen so far
- At each day, compute potential profit
- Update maximum profit

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)