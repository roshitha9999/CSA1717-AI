# ============================================================
#              CSA17 - Artificial Intelligence
#      Assessment Tool 2 (CO2) - Scenario Based Assignment
#      Candidate: Roshitha (192424400)
# ============================================================
# Each question is illustrated with a small runnable simulation
# of the algorithm(s) discussed in the written answer.

import heapq
import random
import math

random.seed(42)

# ------------------------------------------------------------
# QUESTION 1: Drone Delivery Routing
# Greedy Best-First Search vs A* on a weighted graph with a
# straight-line-distance heuristic, plus a dynamic blocked edge.
# ------------------------------------------------------------
print("==============================")
print("QUESTION 1 OUTPUT: Greedy Best-First Search vs A*")
print("==============================")

graph = {
    "Depot": [("A", 2), ("B", 5)],
    "A": [("C", 2), ("E", 9)],
    "B": [("D", 2)],
    "C": [("FloodZone", 2)],
    "D": [("E", 2)],
    "E": [("FloodZone", 2)],
    "FloodZone": [],
}
# Heuristic estimate available to the drone (straight-line distance from
# satellite imagery). C's estimate is deliberately inaccurate/overestimated
# (true remaining cost from C is only 2) to illustrate how heuristic
# accuracy affects Greedy Best-First Search in Question 1(iii).
HEURISTIC = {"Depot": 8, "A": 6, "B": 9, "C": 7, "D": 5, "E": 1, "FloodZone": 0}


def h(node, goal="FloodZone"):
    return HEURISTIC[node]


def greedy_best_first(start, goal, blocked=set()):
    frontier = [(h(start), start)]
    parent = {start: None}
    visited = set()
    while frontier:
        _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        print(f"  Greedy expands {node} (h={h(node)})")
        if node == goal:
            break
        for nxt, _ in graph[node]:
            if (node, nxt) in blocked or nxt in visited:
                continue
            if nxt not in parent:
                parent[nxt] = node
                heapq.heappush(frontier, (h(nxt), nxt))
    return reconstruct(parent, goal)


def astar(start, goal, blocked=set()):
    frontier = [(h(start), 0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    visited = set()
    while frontier:
        f, g, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        print(f"  A* expands {node} (g={g}, h={h(node)}, f={g + h(node)})")
        if node == goal:
            break
        for nxt, cost in graph[node]:
            if (node, nxt) in blocked:
                continue
            new_g = g + cost
            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                parent[nxt] = node
                heapq.heappush(frontier, (new_g + h(nxt), new_g, nxt))
    return reconstruct(parent, goal), g_cost.get(goal)


def reconstruct(parent, goal):
    if goal not in parent:
        return None
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))


def path_cost(path):
    edge_cost = {(a, b): c for a in graph for b, c in graph[a]}
    return sum(edge_cost[(path[i], path[i + 1])] for i in range(len(path) - 1))


print("\n-- Greedy Best-First Search --")
greedy_path = greedy_best_first("Depot", "FloodZone")
print("Greedy path:", greedy_path, "| Total cost:", path_cost(greedy_path))

print("\n-- A* Search --")
astar_path, astar_cost = astar("Depot", "FloodZone")
print("A* path:", astar_path, "| Total cost:", astar_cost)

print("\n-- Dynamic change: edge C->FloodZone suddenly blocked --")
astar_path2, astar_cost2 = astar("Depot", "FloodZone", blocked={("C", "FloodZone")})
print("A* re-planned path:", astar_path2, "| Total cost:", astar_cost2)


# ------------------------------------------------------------
# QUESTION 2: Traffic Signal Timing Optimization
# Hill Climbing (gets stuck) vs Simulated Annealing (escapes)
# on a synthetic "total waiting time" cost landscape.
# ------------------------------------------------------------
print("\n==============================")
print("QUESTION 2 OUTPUT: Hill Climbing vs Simulated Annealing")
print("==============================")


def waiting_time_cost(signal_timing):
    """Synthetic multi-modal cost landscape (lower = better) with a
    local minimum near 20 and the true global minimum near 70."""
    x = signal_timing
    return (
        0.002 * (x - 70) ** 2
        + 8 * math.sin(x / 6) ** 2
        + 0.5
    )


def hill_climbing(start, step=1, max_iter=200):
    current = start
    path = [current]
    for _ in range(max_iter):
        neighbours = [current - step, current + step]
        neighbours = [n for n in neighbours if 0 <= n <= 120]
        best = min(neighbours, key=waiting_time_cost)
        if waiting_time_cost(best) >= waiting_time_cost(current):
            break  # local optimum reached, no improving neighbour
        current = best
        path.append(current)
    return current, waiting_time_cost(current), path


def simulated_annealing(start, max_iter=5000, T0=20.0, cooling=0.998):
    current = start
    best, best_cost = current, waiting_time_cost(current)
    T = T0
    for _ in range(max_iter):
        candidate = current + random.choice([-1, 1]) * random.randint(1, 6)
        candidate = max(0, min(120, candidate))
        delta = waiting_time_cost(candidate) - waiting_time_cost(current)
        if delta < 0 or random.random() < math.exp(-delta / max(T, 1e-6)):
            current = candidate
            if waiting_time_cost(current) < best_cost:
                best, best_cost = current, waiting_time_cost(current)
        T *= cooling
    return best, best_cost


hc_result, hc_cost, hc_path = hill_climbing(start=20)
print(f"Hill Climbing started at signal_timing=20, got stuck at {hc_result} "
      f"(cost={hc_cost:.3f}) after {len(hc_path)} moves -> local optimum")

sa_result, sa_cost = simulated_annealing(start=20)
print(f"Simulated Annealing started at signal_timing=20, converged near "
      f"{sa_result} (cost={sa_cost:.3f}) -> escapes the local optimum")


# ------------------------------------------------------------
# QUESTION 3: Mars Rover Online Search (partial observability)
# Reuses the sense -> plan -> act loop with Uniform Cost Search
# re-planning over a grid whose hazards are unknown up front.
# ------------------------------------------------------------
print("\n==============================")
print("QUESTION 3 OUTPUT: Online Search Agent (Mars Rover)")
print("==============================")

# 0 = free, 1 = hazard (crater/rock, blocked)
true_terrain = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
ROVER_START, SAMPLE_GOAL = (0, 0), (4, 4)


def sense(pos, terrain):
    r, c = pos
    info = {}
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            info[(nr, nc)] = terrain[nr][nc]
    return info


def ucs_plan(start, goal, known):
    frontier, dist, parent, visited = [(0, start)], {start: 0}, {start: None}, set()
    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            break
        r, c = node
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nxt = (r + dr, c + dc)
            nr, nc = nxt
            if 0 <= nr < 5 and 0 <= nc < 5 and known.get(nxt, 0) != 1:
                new_cost = cost + 1
                if nxt not in dist or new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    parent[nxt] = node
                    heapq.heappush(frontier, (new_cost, nxt))
    if goal not in parent:
        return None
    path, node = [], goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))


def online_rover_search(start, goal, terrain):
    known = {start: terrain[start[0]][start[1]]}
    current, travelled, steps = start, [start], 0
    while current != goal:
        steps += 1
        known.update(sense(current, terrain))
        plan = ucs_plan(current, goal, known)
        print(f"  Step {steps}: at {current}, replanned route -> {plan}")
        if not plan or len(plan) < 2:
            print("  No known path to goal; rover halts and waits for new data.")
            return travelled
        current = plan[1]
        travelled.append(current)
    return travelled


rover_path = online_rover_search(ROVER_START, SAMPLE_GOAL, true_terrain)
print("Final path travelled by rover:", rover_path)


# ------------------------------------------------------------
# QUESTION 4: Exam Timetable Scheduling as a CSP
# Backtracking Search + Forward Checking over Courses/Timeslots.
# ------------------------------------------------------------
print("\n==============================")
print("QUESTION 4 OUTPUT: Exam Timetable CSP")
print("==============================")

COURSES = ["AI", "DBMS", "OS", "CN", "ML"]
TIMESLOTS = ["Slot1", "Slot2", "Slot3"]

# Two courses conflict if some student is enrolled in both (cannot share a slot)
CONFLICTS = {
    ("AI", "ML"), ("AI", "DBMS"), ("DBMS", "OS"),
    ("OS", "CN"), ("CN", "ML"),
}


def conflicts(c1, c2):
    return (c1, c2) in CONFLICTS or (c2, c1) in CONFLICTS


def forward_check_exam(domains, assigned_course, assigned_slot):
    new_domains = {c: set(v) for c, v in domains.items()}
    for c in COURSES:
        if c != assigned_course and conflicts(c, assigned_course):
            new_domains[c].discard(assigned_slot)
    return new_domains


def select_mrv(domains, assignment):
    unassigned = [c for c in COURSES if c not in assignment]
    return min(unassigned, key=lambda c: len(domains[c]))


def backtrack_exam(assignment, domains):
    if len(assignment) == len(COURSES):
        return dict(assignment)
    course = select_mrv(domains, assignment)
    for slot in sorted(domains[course]):
        print(f"  Trying {course} -> {slot}")
        assignment[course] = slot
        pruned = forward_check_exam(domains, course, slot)
        if all(len(pruned[c]) > 0 for c in COURSES if c not in assignment):
            result = backtrack_exam(assignment, pruned)
            if result is not None:
                return result
        else:
            print(f"    Reject {course} -> {slot}: empty domain for a conflicting course")
        del assignment[course]
    return None


initial = {c: set(TIMESLOTS) for c in COURSES}
timetable = backtrack_exam({}, initial)
print("\nFinal exam timetable:")
for c in COURSES:
    print(f"  {c}: {timetable[c]}")


# ------------------------------------------------------------
# QUESTION 5: Strategic Game AI - Minimax & Alpha-Beta Pruning
# ------------------------------------------------------------
print("\n==============================")
print("QUESTION 5 OUTPUT: Minimax vs Alpha-Beta Pruning")
print("==============================")

# A depth-3 game tree of leaf evaluation scores (evaluation function
# output for each terminal game state).
GAME_TREE = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]],
]

minimax_nodes_visited = 0
alphabeta_nodes_visited = 0


def minimax(tree, depth, maximizing):
    global minimax_nodes_visited
    minimax_nodes_visited += 1
    if depth == 0:
        return tree
    if maximizing:
        return max(minimax(child, depth - 1, False) for child in tree)
    else:
        return min(minimax(child, depth - 1, True) for child in tree)


def alphabeta(tree, depth, alpha, beta, maximizing):
    global alphabeta_nodes_visited
    alphabeta_nodes_visited += 1
    if depth == 0:
        return tree
    if maximizing:
        value = float("-inf")
        for child in tree:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print("    Pruned remaining branches (beta cut-off)")
                break
        return value
    else:
        value = float("inf")
        for child in tree:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                print("    Pruned remaining branches (alpha cut-off)")
                break
        return value


print("-- Plain Minimax --")
best_minimax = minimax(GAME_TREE, 3, True)
print(f"Minimax result: {best_minimax} | nodes visited: {minimax_nodes_visited}")

print("\n-- Minimax with Alpha-Beta Pruning --")
best_alphabeta = alphabeta(GAME_TREE, 3, float("-inf"), float("inf"), True)
print(f"Alpha-Beta result: {best_alphabeta} | nodes visited: {alphabeta_nodes_visited}")
print(f"Nodes saved by pruning: {minimax_nodes_visited - alphabeta_nodes_visited}")