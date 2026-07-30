# ============================================================
#              CSA17 - Artificial Intelligence
#      Assessment Tool 2 - Constraint-Based Problem Solving
#      Candidate: Roshitha (192424400)
# ============================================================

# ------------------------------------------------------------
# QUESTION 1: Doctor-Shift Scheduling as a CSP
# Solved with backtracking + forward checking (domain pruning)
# and Minimum-Remaining-Values (MRV) variable ordering.
# ------------------------------------------------------------

SHIFT_ORDER = {"Morning": 1, "Afternoon": 2, "Night": 3}
DOCTORS = ["D1", "D2", "D3"]


def build_initial_domains():
    domains = {d: {"Morning", "Afternoon", "Night"} for d in DOCTORS}
    domains["D1"].discard("Night")        # D1 cannot work Night
    domains["D3"].discard("Morning")      # D3 cannot work Morning
    return domains


def forward_check(domains, assigned_doctor, assigned_shift):
    """Remove the used shift from every other doctor's domain, and
    prune shifts that would break the D2-before-D3 ordering."""
    new_domains = {d: set(v) for d, v in domains.items()}

    for d in DOCTORS:
        if d != assigned_doctor:
            new_domains[d].discard(assigned_shift)

    if assigned_doctor == "D2":
        new_domains["D3"] = {s for s in new_domains["D3"]
                              if SHIFT_ORDER[s] > SHIFT_ORDER[assigned_shift]}
    if assigned_doctor == "D3":
        new_domains["D2"] = {s for s in new_domains["D2"]
                              if SHIFT_ORDER[s] < SHIFT_ORDER[assigned_shift]}

    return new_domains


def select_unassigned_variable(domains, assignment):
    """MRV heuristic: pick the unassigned doctor with the fewest legal shifts left."""
    unassigned = [d for d in DOCTORS if d not in assignment]
    return min(unassigned, key=lambda d: len(domains[d]))


def backtracking_csp(assignment, domains, trace):
    if len(assignment) == len(DOCTORS):
        return dict(assignment)

    var = select_unassigned_variable(domains, assignment)
    for shift in sorted(domains[var], key=lambda s: SHIFT_ORDER[s]):
        trace.append(f"Trying {var} = {shift}")
        assignment[var] = shift
        pruned = forward_check(domains, var, shift)

        if all(len(pruned[d]) > 0 for d in DOCTORS if d not in assignment):
            result = backtracking_csp(assignment, pruned, trace)
            if result is not None:
                return result
            trace.append(f"Backtrack: {var} = {shift} led to a dead end")
        else:
            trace.append(f"Reject {var} = {shift}: empty domain produced for another doctor")

        del assignment[var]

    return None


print("==============================")
print("QUESTION 1 OUTPUT")
print("==============================")

csp_trace = []
initial_domains = build_initial_domains()
final_schedule = backtracking_csp({}, initial_domains, csp_trace)

for line in csp_trace:
    print(line)

print("\nFinal Valid Schedule:")
print(final_schedule)


# ------------------------------------------------------------
# QUESTION 2: Robot Grid Navigation (5x5) using BFS
# ------------------------------------------------------------

from collections import deque

# 0 = free cell, 1 = obstacle
navigation_grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

START = (0, 0)
GOAL = (4, 4)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs_with_frontier_log(start, goal, grid):
    frontier = deque([start])
    came_from = {start: None}
    visited = {start}
    step = 0

    while frontier:
        step += 1
        current = frontier.popleft()
        print(f"Expand step {step}: node={current}, "
              f"h(n)={manhattan(current, goal)}, frontier_before={list(frontier)}")

        if current == goal:
            break

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nxt = (current[0] + dx, current[1] + dy)
            r, c = nxt
            if 0 <= r < 5 and 0 <= c < 5 and grid[r][c] == 0 and nxt not in visited:
                visited.add(nxt)
                came_from[nxt] = current
                frontier.append(nxt)

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path


print("\n==============================")
print("QUESTION 2 OUTPUT")
print("==============================")

optimal_path = bfs_with_frontier_log(START, GOAL, navigation_grid)
print("\nOptimal Path:", optimal_path)
print("Cost:", len(optimal_path) - 1)


# ------------------------------------------------------------
# QUESTION 3: Autonomous Rescue Robot - Online Uniform Cost Search
# The robot only "senses" adjacent cells before committing to a
# move, simulating a genuinely online (partially-observable) agent
# rather than a single offline UCS run over a fully known grid.
# ------------------------------------------------------------

import heapq

# 0 = free, 1 = obstacle, 2 = risky zone (extra cost)
true_environment = [
    [0, 2, 0, 0, 0],
    [0, 1, 0, 1, 2],
    [0, 0, 0, 1, 0],
    [2, 1, 0, 0, 0],
    [0, 0, 2, 0, 0],
]

RESCUE_START = (0, 0)
SURVIVOR_GOAL = (4, 4)

MOVE_COST = 1
RISK_EXTRA_COST = 2


def sense_adjacent(position, environment):
    """Return the type of each in-bounds neighbouring cell (the only
    information the robot is allowed to see before it moves)."""
    r, c = position
    info = {}
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dx, c + dy
        if 0 <= nr < 5 and 0 <= nc < 5:
            info[(nr, nc)] = environment[nr][nc]
    return info


def cell_cost(cell_type):
    return MOVE_COST + RISK_EXTRA_COST if cell_type == 2 else MOVE_COST


def online_ucs_rescue(start, goal, environment):
    known_map = {start: environment[start[0]][start[1]]}
    current = start
    total_cost = 0
    travelled = [current]

    while current != goal:
        sensed = sense_adjacent(current, environment)
        known_map.update(sensed)
        print(f"At {current}, sensed neighbours: {sensed}")

        # Plan the next step with UCS restricted to currently known cells only.
        frontier = [(0, current)]
        dist = {current: 0}
        parent = {current: None}
        visited = set()
        reached_goal = False

        while frontier:
            cost, node = heapq.heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            if node == goal:
                reached_goal = True
                break
            r, c = node
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dx, c + dy
                neighbour = (nr, nc)
                if 0 <= nr < 5 and 0 <= nc < 5 and known_map.get(neighbour, 0) != 1:
                    step_cost = cell_cost(known_map.get(neighbour, 0))
                    new_cost = cost + step_cost
                    if neighbour not in dist or new_cost < dist[neighbour]:
                        dist[neighbour] = new_cost
                        parent[neighbour] = node
                        heapq.heappush(frontier, (new_cost, neighbour))

        if not reached_goal or goal not in parent:
            print("Goal not reachable with current knowledge; robot cannot proceed.")
            return travelled, None

        # Reconstruct the planned route and take just the first step (online behaviour).
        route = []
        node = goal
        while node is not None:
            route.append(node)
            node = parent[node]
        route.reverse()

        next_step = route[1] if len(route) > 1 else route[0]
        step_cost = cell_cost(known_map.get(next_step, environment[next_step[0]][next_step[1]]))
        total_cost += step_cost
        current = next_step
        travelled.append(current)

    return travelled, total_cost


print("\n==============================")
print("QUESTION 3 OUTPUT")
print("==============================")

rescue_path, rescue_cost = online_ucs_rescue(RESCUE_START, SURVIVOR_GOAL, true_environment)
print("\nLeast-Cost Path:", rescue_path)
print("Total Cost:", rescue_cost)