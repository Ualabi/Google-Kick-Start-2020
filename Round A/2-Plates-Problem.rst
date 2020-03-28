Link: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb

Problem
-------
Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.

Input
-----
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.

Output
------
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sum of beauty values that Dr. Patel could pick.

Limits
------
| Time limit: 20 seconds per test set.
| Memory limit: 1GB.
| 1 ≤ **T** ≤ 100.
| 1 ≤ **K** ≤ 30.
| 1 ≤ **P** ≤ **N** * **K**.
| The beauty values are between 1 and 100, inclusive.

Test set 1
~~~~~~~~~~~~~~~~~~~~
1 ≤ **N** ≤ 3.

Test set 2
~~~~~~~~~~~~~~~~~~~
1 ≤ **N** ≤ 50.

Sample
------

::

    Input           Output
    
    2
    3
    5 1 2           Case #1: 1 1 2
    6               Case #2: 1 1 2 2 2 3
    1 3 3 2 2 15

In Sample Case #1, Dr. Patel needs to pick P = 5 plates:

- He can pick the top 3 plates from the first stack (10 + 10 + 100 = 120).
- He can pick the top 2 plates from the second stack (80 + 50 = 130) .
In total, the sum of beauty values is 250.

In Sample Case #2, Dr. Patel needs to pick P = 3 plates:

- He can pick the top 2 plates from the first stack (80 + 80 = 160).
- He can pick no plates from the second stack.
- He can pick the top plate from the third stack (20).
In total, the sum of beauty values is 180.

In Case #2: Tambourine can add up to three sessions. The added sessions are marked in bold: 1 2 3 4 5 6 7 **8** **9** 10. The difficulty is now 1. Note that Tambourine only added two sessions.

- Only Sample #1 is a valid input for Test set 1. Consequently, Sample #1 will be used as a sample test set for your submissions.
- **Note #2:** Unlike previous editions, in Kick Start 2020, all test sets are visible verdict test sets, meaning you receive instant feedback upon submission.

