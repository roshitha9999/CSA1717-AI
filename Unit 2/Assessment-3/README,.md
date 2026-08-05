# Artificial Intelligence Lab Assessment (CO2 - AT3 - Dry Run Test)

## Candidate
Roshitha (192424400)

## Title
Implementation of A* Search Algorithm and Minimax Algorithm with Alpha-Beta Pruning

## Description
This assessment implements two Artificial Intelligence algorithms in Python:
- A* Search Algorithm (with parent-pointer path reconstruction)
- Minimax Algorithm with Alpha-Beta Pruning (as a generic recursive function)

Both programs demonstrate step-by-step execution with user input and iteration-wise output.

## Features

### Question 1: A* Search
- Finds the shortest path between the start and goal nodes on the given weighted graph.
- Displays Current Node, Open List, Closed List, g(n), h(n), and f(n) at every iteration.
- Reconstructs the optimal path via parent pointers and reports the total path cost.

### Question 2: Minimax with Alpha-Beta Pruning
- Evaluates the game tree using a single recursive Minimax function.
- Displays Alpha (\u03b1), Beta (\u03b2), selected values, and pruned nodes at every step.
- Determines the best move and final minimax value.

## Requirements
- Python 3.x
- Modules Used: `heapq`, `itertools`, `math`

## Repository Structure
```
├── Problem/         # Problem Statement (A3_Problem_AI.docx / .pdf)
├── Solution/         # Detailed written solutions (A3_Solution_AI.docx / .pdf)
├── Report/           # Full lab report - Aim/Objective/Algorithm/Result (A3_Report_AI.docx / .pdf)
├── Source_Code/      # A3_SourceCode_AI.py - runnable Python source for both questions
├── Output/           # A3_Output_1Q.txt, A3_Output_2Q.txt - captured console output (IDLE-style)
└── README.md
```

## How to Run
```
python Source_Code/A3_SourceCode_AI.py
```
Select `1` for A* Search or `2` for Minimax with Alpha-Beta Pruning when prompted.

## Learning Outcome
This assessment helps understand informed search using A* Search and adversarial search using Minimax with Alpha-Beta Pruning, along with their practical implementation in Python.
