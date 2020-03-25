Problem
-------
Tambourine has prepared a fitness program so that she can become more fit! The program is made of **N** sessions. During the i-th session, Tambourine will exercise for **M\ :sub:`i`** minutes. The number of minutes she exercises in each session are strictly increasing.

The difficulty of her fitness program is equal to the maximum difference in the number of minutes between any two consecutive training sessions.

To make her program less *difficult*, Tambourine has decided to add up to **K** additional training sessions to her fitness program. She can add these sessions anywhere in her fitness program, and exercise any positive integer number of minutes in each of them. After the additional training session are added, the number of minutes she exercises in each session must still be strictly increasing. What is the minimum difficulty possible?

Input
-----
The first line of the input gives the number of test cases, **T**. **T** test
cases follow. Each test case begins with a line containing **N**, the number of
papers Jorge wrote.

The second line contains **N** integers. The i-th integer is **A**\ |i|, the
number of citations the i-th paper has.

Output
------
For each test case, output one line containing ``Case #x: y``, where ``x`` is
the test case number (starting from 1) and ``y`` is a space-separated list of
integers. The i-th integer is the H-index score after Jorge wrote his i-th
paper.

Limits
------
| Time limit: 50 seconds per test set.
| Memory limit: 1GB.
| 1 ≤ **T** ≤ 100.
| 1 ≤ **A**\ |i| ≤ 10\ :sup:`5`.

Test set 1 (Visible)
~~~~~~~~~~~~~~~~~~~~
1 ≤ **N** ≤ 1000.

Test set 2 (Hidden)
~~~~~~~~~~~~~~~~~~~
1 ≤ **N** ≤ 10\ :sup:`5`.

Sample
------

::

    Input           Output
    
    2
    3
    5 1 2           Case #1: 1 1 2
    6               Case #2: 1 1 2 2 2 3
    1 3 3 2 2 15

In Sample Case #1, Jorge wrote **N** = 3 papers.

- After the 1st paper, Jorge's H-index score is 1, since he has 1 paper with at
  least 1 citation.
- After the 2nd paper, Jorge's H-index score is still 1.
- After the 3rd paper, Jorge's H-index score is 2, since he has 2 papers with
  at least 2 citations (the 1st and 3rd papers).

In Sample Case #2, Jorge wrote **N** = 6 papers.

- After the 1st paper, Jorge's H-index score is 1, since he has 1 paper with at
  least 1 citation.
- After the 2nd paper, Jorge's H-index score is still 1.
- After the 3rd paper, Jorge's H-index score is 2, since he has 2 papers with
  at least 2 citations (the 2nd and 3rd papers).
- After the 4th paper, Jorge's H-index score is still 2.
- After the 5th paper, Jorge's H-index score is still 2.
- After the 6th paper, Jorge's H-index score is 3, since he has 3 papers with
  at least 3 citations (the 2nd, 3rd and 6th papers).
