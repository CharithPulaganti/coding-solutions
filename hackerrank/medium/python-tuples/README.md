# Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Task**  
Given an integer, $n$, and $n$ space-separated integers as input, create a tuple, $t$, of those $n$ integers. Then compute and print the result of $hash(t)$.  

**Note:** [hash()](https://docs.python.org/3/library/functions.html#hash) is one of the functions in the `__builtins__` module, so it need not be imported.  

**Input Format**

The first line contains an integer, $n$, denoting the number of elements in the tuple.	 			
The second line contains $n$ space-separated integers describing the elements in tuple $t$.  

**Constraints**

 

**Output Format**

Print the result of $hash(t)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T09:27:28.539Z  

```py
if __name__ == '__main__':
    N = int(input())
    List = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            List.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(List)
        elif command[0] == "remove":
            List.remove(int(command[1]))
        elif command[0] == "append":
            List.append(int(command[1]))
        elif command[0] == "sort":
            List.sort()
        elif command[0] == "pop":
            List.pop()
        elif command[0] == "reverse":
            List.reverse()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-tuples/problem)