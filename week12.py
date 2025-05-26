from collections import deque

d = deque([17, 1, 2, 6, 4, 5])
d.append(7)
d.append(-9)
d.appendleft(100)

for i in range(len(d)):
    print(d.popleft())