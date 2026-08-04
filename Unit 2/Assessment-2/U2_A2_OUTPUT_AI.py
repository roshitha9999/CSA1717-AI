Python 3.13.2 (tags/v3.13.2:xxxxxxx, Feb  5 2025, 09:12:44) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=== RESTART: C:/Users/roshitha/OneDrive/Documents/SIMATS/AI/A3_SourceCode_AI.py ===

==============================
QUESTION 1 OUTPUT: Greedy Best-First Search vs A*
==============================

-- Greedy Best-First Search --
  Greedy expands Depot (h=8)
  Greedy expands A (h=6)
  Greedy expands E (h=1)
  Greedy expands FloodZone (h=0)
Greedy path: ['Depot', 'A', 'E', 'FloodZone'] | Total cost: 13

-- A* Search --
  A* expands Depot (g=0, h=8, f=8)
  A* expands A (g=2, h=6, f=8)
  A* expands C (g=4, h=7, f=11)
  A* expands FloodZone (g=6, h=0, f=6)
A* path: ['Depot', 'A', 'C', 'FloodZone'] | Total cost: 6

-- Dynamic change: edge C->FloodZone suddenly blocked --
  A* expands Depot (g=0, h=8, f=8)
  A* expands A (g=2, h=6, f=8)
  A* expands C (g=4, h=7, f=11)
  A* expands E (g=11, h=1, f=12)
  A* expands FloodZone (g=13, h=0, f=13)
A* re-planned path: ['Depot', 'A', 'E', 'FloodZone'] | Total cost: 13

==============================
QUESTION 2 OUTPUT: Hill Climbing vs Simulated Annealing
==============================
Hill Climbing started at signal_timing=20, got stuck at 19 (cost=5.707) after 2 moves -> local optimum
Simulated Annealing started at signal_timing=20, converged near 75 (cost=0.585) -> escapes the local optimum

==============================
QUESTION 3 OUTPUT: Online Search Agent (Mars Rover)
==============================
  Step 1: at (0, 0), replanned route -> [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
  Step 2: at (0, 1), replanned route -> [(0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
  Step 3: at (0, 2), replanned route -> [(0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
  Step 4: at (1, 2), replanned route -> [(1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
  Step 5: at (2, 2), replanned route -> [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
  Step 6: at (2, 3), replanned route -> [(2, 3), (2, 4), (3, 4), (4, 4)]
  Step 7: at (2, 4), replanned route -> [(2, 4), (3, 4), (4, 4)]
  Step 8: at (3, 4), replanned route -> [(3, 4), (4, 4)]
Final path travelled by rover: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

==============================
QUESTION 4 OUTPUT: Exam Timetable CSP
==============================
  Trying AI -> Slot1
  Trying DBMS -> Slot2
  Trying OS -> Slot1
  Trying CN -> Slot2
  Trying ML -> Slot3

Final exam timetable:
  AI: Slot1
  DBMS: Slot2
  OS: Slot1
  CN: Slot2
  ML: Slot3

==============================
QUESTION 5 OUTPUT: Minimax vs Alpha-Beta Pruning
==============================
-- Plain Minimax --
Minimax result: 5 | nodes visited: 15

-- Minimax with Alpha-Beta Pruning --
    Pruned remaining branches (beta cut-off)
    Pruned remaining branches (alpha cut-off)
Alpha-Beta result: 5 | nodes visited: 11
Nodes saved by pruning: 4
>>>