# Company Logo

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string $s$, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.  
- If the occurrence count is the same, sort the characters in alphabetical order.   

For example, according to the conditions described above, 

$\color{green}\texttt{G}\color{red}\texttt{OO}\color{green}\texttt{G}\color{black}\texttt{LE}$ would have it's logo with the letters $\color{green}\texttt{G},\color{red}\texttt{O},\color{black}\texttt{E}$. 




**Input Format**

A single line of input containing the string $S$.  



**Constraints**

+ $ 3 < len(S) \le 10^4 $   
+ $S$ has at least $3$ distinct characters   

**Output Format**

Print the three most common characters along with their occurrence count each on a separate line.  
Sort output in descending order of occurrence count.  
If the occurrence count is the same, sort the characters in alphabetical order.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T12:04:37.060Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    count = Counter(s)
    
    for char, freq in sorted(count.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, freq)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/most-commons/problem)