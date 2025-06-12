push pop peek

python uses list

#Stack
## Using List
Common methods
```
#Push
.append()

#Pop
.pop()

#Peek (given that stack is a list)
stack[-`]

```

## Using deque
using python deque
  - similar methods
  - popleft()
  - appendleft()
  - just allowing to append left and right

```
from collections import deque

#Appending Elements 
dq.append(4)        # Adds to the right
dq.appendleft(0)    # Adds to the left
print(dq)  # deque([0, 1, 2, 3, 4])

#FIFO
queue = deque()

queue.append("first")
queue.append("second")

print(queue.popleft())  # first
print(queue.popleft())  # second

#Rotate
dq = deque([1, 2, 3, 4])
dq.rotate(1)    # Right rotation: deque([4, 1, 2, 3])
dq.rotate(-1)   # Left rotation: deque([1, 2, 3, 4])

```

#Key Fundementals

## Match Statements
using match 
  match case: 
  else could be written as case _:

## isnumeric() and isdigit()
Difference between isnumeric and isdigit
  - isnnumeric accounts for isdigit
  - accounts for roman numerals as well

import math.ciel
take one argument
match.ciel

Read direction carefully 
  - truncates towards zero


                    
    
