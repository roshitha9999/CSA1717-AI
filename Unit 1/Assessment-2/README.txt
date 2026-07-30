# Artificial Intelligence – Assessment 2

## Candidate
Roshitha (192424400)

## Title
Constraint-Based Problem Solving

## Objective
To understand and implement constraint satisfaction and search-based problem solving techniques in Artificial Intelligence using Python, covering backtracking search, breadth-first search, and uniform cost search under partial observability.

## Software Used
Python 3.13

## Tools Used
Python IDLE

## Algorithms / AI Concepts Used
- Backtracking Search with Forward Checking and MRV (Minimum-Remaining-Values) heuristic
- Breadth First Search (BFS) with Manhattan Distance evaluation
- Online Uniform Cost Search (UCS) with dynamic sensing and re-planning

## Problems Implemented
1. Doctor-Shift Scheduling (CSP) solved via backtracking + forward checking + MRV variable ordering
2. Robot Grid Navigation (5×5) solved via BFS with step-by-step frontier logging
3. Autonomous Rescue Robot solved via an online UCS agent that senses adjacent cells and re-plans dynamically

## Repository Structure
```
├── Problem/        # Assessment Tool 2 question sheet (A2_Problem_AI.docx / .pdf)
├── Solution/        # Written conceptual solutions (A2_Solution_AI.docx / .pdf)
├── Report/          # Full report with explanations, code, and outputs (A2_Report_AI.docx / .pdf)
├── Source_Code/     # A2_SourceCode_AI.py – runnable Python source for all 3 questions
├── Output/          # A2_OUTPUT_AI.txt – captured console output (IDLE-style)
└── README.md
```

## How to Run
```
python Source_Code/A2_SourceCode_AI.py
```

## Result
Successfully implemented all three Artificial Intelligence programs using Python. The programs demonstrate constraint satisfaction with forward checking, uninformed search (BFS) for shortest-path grid navigation, and an online cost-sensitive search agent operating under partial observability.
