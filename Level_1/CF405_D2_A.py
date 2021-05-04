# https://codeforces.com/contest/405/problem/A

"""
Gravity Flip

Little Chris is bored during his physics lessons (too easy), so he has built a toy box to keep himself occupied.
The box is special, since it has the ability to change gravity.
There are n columns of toy cubes in the box arranged in a line. The i-th column contains ai cubes.
At first, the gravity in the box is pulling the cubes downwards.
When Chris switches the gravity, it begins to pull all the cubes to the right side of the box.

Given the initial configuration of the toy cubes in the box,
find the amounts of cubes in each of the n columns after the gravity switch!

Input:
The first line of input contains an integer n (1 ≤ n ≤ 100), the number of the columns in the box.
The next line contains n space-separated integer numbers.
The i-th number ai (1 ≤ ai ≤ 100) denotes the number of cubes in the i-th column.

Output:
Output n integer numbers separated by spaces,
where the i-th number is the amount of cubes in the i-th column after the gravity switch.

Example
input:
4
3 2 1 2
output:
1 2 2 3
"""

# SOLUTION:
# Every cube will move to the right until it hit a higher or equally high column with highest column at the end.
# This is in its essence sorting in ascending order

# Get number of columns
n = int(input())

# Get heights of each individual column and store them in a list
box = list(map(int, input().split()))

# Sort the list in ascending order
box.sort()

# Display values from sorted list
print(*box)