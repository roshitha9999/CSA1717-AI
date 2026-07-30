Python 3.13.2 (tags/v3.13.2:xxxxxxx, Feb  5 2025, 09:12:44) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=== RESTART: C:/Users/roshitha/OneDrive/Documents/SIMATS/AI/A2_SourceCode_AI.py ===

==============================
QUESTION 1 OUTPUT
==============================
Trying D1 = Morning
Trying D2 = Afternoon
Trying D3 = Night

Final Valid Schedule:
{'D1': 'Morning', 'D2': 'Afternoon', 'D3': 'Night'}

==============================
QUESTION 2 OUTPUT
==============================
Expand step 1: node=(0, 0), h(n)=8, frontier_before=[]
Expand step 2: node=(0, 1), h(n)=7, frontier_before=[(1, 0)]
Expand step 3: node=(1, 0), h(n)=7, frontier_before=[(0, 2)]
Expand step 4: node=(0, 2), h(n)=6, frontier_before=[(2, 0)]
Expand step 5: node=(2, 0), h(n)=6, frontier_before=[(1, 2)]
Expand step 6: node=(1, 2), h(n)=5, frontier_before=[(3, 0)]
Expand step 7: node=(3, 0), h(n)=5, frontier_before=[(2, 2)]
Expand step 8: node=(2, 2), h(n)=4, frontier_before=[(4, 0)]
Expand step 9: node=(4, 0), h(n)=4, frontier_before=[(2, 3)]
Expand step 10: node=(2, 3), h(n)=3, frontier_before=[(4, 1)]
Expand step 11: node=(4, 1), h(n)=3, frontier_before=[(2, 4)]
Expand step 12: node=(2, 4), h(n)=2, frontier_before=[(4, 2)]
Expand step 13: node=(4, 2), h(n)=2, frontier_before=[(3, 4), (1, 4)]
Expand step 14: node=(3, 4), h(n)=1, frontier_before=[(1, 4), (4, 3)]
Expand step 15: node=(1, 4), h(n)=3, frontier_before=[(4, 3), (4, 4)]
Expand step 16: node=(4, 3), h(n)=1, frontier_before=[(4, 4), (0, 4)]
Expand step 17: node=(4, 4), h(n)=0, frontier_before=[(0, 4)]

Optimal Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
Cost: 8

==============================
QUESTION 3 OUTPUT
==============================
At (0, 0), sensed neighbours: {(0, 1): 2, (1, 0): 0}
At (1, 0), sensed neighbours: {(1, 1): 1, (2, 0): 0, (0, 0): 0}
At (2, 0), sensed neighbours: {(2, 1): 0, (3, 0): 2, (1, 0): 0}
At (2, 1), sensed neighbours: {(2, 2): 0, (3, 1): 1, (2, 0): 0, (1, 1): 1}
At (2, 2), sensed neighbours: {(2, 3): 1, (3, 2): 0, (2, 1): 0, (1, 2): 0}
At (3, 2), sensed neighbours: {(3, 3): 0, (4, 2): 2, (3, 1): 1, (2, 2): 0}
At (3, 3), sensed neighbours: {(3, 4): 0, (4, 3): 0, (3, 2): 0, (2, 3): 1}
At (3, 4), sensed neighbours: {(4, 4): 0, (3, 3): 0, (2, 4): 0}

Least-Cost Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]
Total Cost: 8
>>>