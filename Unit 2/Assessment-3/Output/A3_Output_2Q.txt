Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit
(AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>
= RESTART: C:/Users/roshitha/OneDrive/Documents/SIMATS/AI/A3_SourceCode_AI.py
Select Algorithm:
1. A* Search
2. Minimax with Alpha-Beta Pruning
Enter choice (1/2): 2

Enter the leaf node values
Leaf 1 : 3
Leaf 2 : 5
Leaf 3 : 6
Leaf 4 : 9
Leaf 5 : 1
Leaf 6 : 2

====================================

---- Evaluating MIN-1 ----
  Evaluating leaf MIN-1[0] = 3
    Alpha = -inf, Beta = 3
  Evaluating leaf MIN-1[1] = 5
    Alpha = -inf, Beta = 3
  Evaluating leaf MIN-1[2] = 6
    Alpha = -inf, Beta = 3
  Selected value for MIN-1 = 3
After MIN-1: Alpha updated to 3

---- Evaluating MIN-2 ----
  Evaluating leaf MIN-2[0] = 9
    Alpha = 3, Beta = 9
  Evaluating leaf MIN-2[1] = 1
    Alpha = 3, Beta = 1
    Pruned remaining leaves of MIN-2 : [2]
  Selected value for MIN-2 = 1
After MIN-2: Alpha updated to 3

====================================
Values returned to MAX : [3, 1]
Final Minimax Value : 3
Best Move : Left Subtree

Run Again?(y/n): n
>>>
