Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit
(AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>
= RESTART: C:/Users/roshitha/OneDrive/Documents/SIMATS/AI/A3_SourceCode_AI.py
Select Algorithm:
1. A* Search
2. Minimax with Alpha-Beta Pruning
Enter choice (1/2): 1

Enter Start Node : A
Enter Goal Node : G

======================================
Iteration : 1
Current Node : A
Open List : []
Closed List : []
g(n) = 0
h(n) = 7
f(n) = 7

======================================
Iteration : 2
Current Node : B
Open List : [('C', 8)]
Closed List : ['A']
g(n) = 2
h(n) = 6
f(n) = 8

======================================
Iteration : 3
Current Node : E
Open List : [('C', 8), ('D', 12)]
Closed List : ['A', 'B']
g(n) = 4
h(n) = 2
f(n) = 6

======================================
Iteration : 4
Current Node : C
Open List : [('D', 9)]
Closed List : ['A', 'B', 'E']
g(n) = 4
h(n) = 4
f(n) = 8

======================================
Iteration : 5
Current Node : D
Open List : []
Closed List : ['A', 'B', 'E', 'C']
g(n) = 6
h(n) = 3
f(n) = 9

======================================
Iteration : 6
Current Node : G
Open List : []
Closed List : ['A', 'B', 'E', 'C', 'D']
g(n) = 8
h(n) = 0
f(n) = 8

Goal Reached
Optimal Path : A -> B -> E -> D -> G
Total Cost : 8

Search Again?(y/n): n
>>>
