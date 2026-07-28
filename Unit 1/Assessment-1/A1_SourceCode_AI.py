# =====================================================================
# CSA17 - Artificial Intelligence
# Assessment Tool 1 - Analytical Problem Solving
# Candidate: Y.Roshitha (192424400)
# =====================================================================


# ---------------------------------------------------------------------
# Q1: Water Jug Problem (4-gallon & 3-gallon jugs) - solved using BFS
# ---------------------------------------------------------------------
from collections import deque


def water_jug_bfs(cap_a=4, cap_b=3, target=2):
    """
    Generic BFS solver for the two-jug problem.
    State = (amount_in_a, amount_in_b)
    Goal   = any state where jug A holds exactly `target` gallons.
    """
    start = (0, 0)
    visited = {start}
    parent = {start: None}
    queue = deque([start])

    def next_states(state):
        a, b = state
        moves = [
            (cap_a, b),                                   # fill A
            (a, cap_b),                                   # fill B
            (0, b),                                        # empty A
            (a, 0),                                        # empty B
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),  # pour A -> B
            (a + min(b, cap_a - a), b - min(b, cap_a - a)),  # pour B -> A
        ]
        return moves

    goal_state = None
    while queue:
        state = queue.popleft()
        if state[0] == target:
            goal_state = state
            break
        for nxt in next_states(state):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = state
                queue.append(nxt)

    # reconstruct path from start -> goal
    path = []
    node = goal_state
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


print("Q1: BFS solution to get exactly 2 gallons in the 4-gallon jug\n")
jug_path = water_jug_bfs()
for i, (a, b) in enumerate(jug_path):
    print(f"Step {i}: Jug-A(4gal) = {a}, Jug-B(3gal) = {b}")


# ---------------------------------------------------------------------
# Q2: Mars Rover - Goal/Utility based Intelligent Agent
# ---------------------------------------------------------------------
class MarsRoverAgent:
    """
    A goal-based Mars rover agent with a simple utility check
    (mission is considered a success once >=2 samples are analysed
    and battery reserve stays above a safety threshold).
    """

    SAFE_ENERGY_THRESHOLD = 20

    def __init__(self):
        self.battery = 100
        self.samples_analysed = 0
        self.location = (0, 0)
        self.log = []

    def percepts(self):
        return {
            "camera_feed": "surface_image",
            "spectrometer_reading": "mineral_composition",
            "soil_probe": "regolith_data",
            "ambient_temp_c": -63,
            "terrain_type": "cratered",
            "obstacle_detected": False,
            "dust_storm_alert": False,
        }

    def actions(self):
        return [
            "drive_forward", "drive_backward", "rotate_left", "rotate_right",
            "photograph_surface", "extract_core_sample", "run_spectral_analysis",
            "uplink_to_orbiter",
        ]

    def drive(self, direction):
        self.battery -= 4
        self.log.append(f"Rover drove {direction}, battery={self.battery}")

    def analyse_sample(self):
        self.battery -= 12
        self.samples_analysed += 1
        self.log.append(f"Sample analysed #{self.samples_analysed}, battery={self.battery}")

    def performance_measure(self):
        mission_success = (
            self.samples_analysed >= 2 and self.battery >= self.SAFE_ENERGY_THRESHOLD
        )
        return {
            "battery_remaining": self.battery,
            "samples_analysed": self.samples_analysed,
            "mission_success": mission_success,
        }


print("\nQ2: Mars Rover Agent")
rover = MarsRoverAgent()
print("Percepts:", rover.percepts())
print("Actions:", rover.actions())
rover.drive("north-east")
rover.analyse_sample()
rover.analyse_sample()
print("Performance:", rover.performance_measure())


# ---------------------------------------------------------------------
# Q3: 8-Queens Problem - solved using bitmask backtracking
# ---------------------------------------------------------------------
BOARD_SIZE = 8
ALL_PLACED = (1 << BOARD_SIZE) - 1


def solve_queens_bitmask():
    solutions = []
    placement = []

    def place(row, cols, diag1, diag2):
        if row == BOARD_SIZE:
            solutions.append(placement[:])
            return
        free = ALL_PLACED & ~(cols | diag1 | diag2)
        while free:
            bit = free & (-free)
            col = bit.bit_length() - 1
            placement.append(col)
            place(row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)
            placement.pop()
            free &= free - 1

    place(0, 0, 0, 0)
    return solutions


queen_solutions = solve_queens_bitmask()
print("\nQ3: 8-Queens (bitmask backtracking)")
print("Total solutions found:", len(queen_solutions))
print("Sample solution (row -> col per row):", queen_solutions[0])


# ---------------------------------------------------------------------
# Q4: Cab Booking Goal-Based Agent - ranks cabs on ETA and rating
# ---------------------------------------------------------------------
class CabOption:
    def __init__(self, cab_type, eta_minutes, driver_rating, per_km_rate):
        self.cab_type = cab_type
        self.eta_minutes = eta_minutes
        self.driver_rating = driver_rating
        self.per_km_rate = per_km_rate

    def score(self):
        # lower ETA and higher rating both improve the score
        return self.driver_rating * 10 - self.eta_minutes


def fetch_nearby_cabs():
    return [
        CabOption("mini", 6, 4.6, 11),
        CabOption("sedan", 4, 4.8, 14),
        CabOption("micro", 8, 4.3, 9),
        CabOption("prime", 3, 4.9, 18),
        CabOption("shared", 9, 4.1, 7),
    ]


def book_best_cab(source, destination, preferred_type, distance_km=12):
    cabs = fetch_nearby_cabs()
    if not cabs:
        return "No cabs available in this area"

    candidates = [c for c in cabs if c.cab_type == preferred_type]
    if not candidates:
        candidates = cabs  # fall back to the full list if preference unavailable

    best = max(candidates, key=lambda c: c.score())
    fare = round(best.per_km_rate * distance_km, 2)

    return (
        f"Cab booked: {best.cab_type} | ETA={best.eta_minutes} min | "
        f"Rating={best.driver_rating} | Fare={fare} INR"
    )


print("\nQ4:", book_best_cab("Tambaram", "T.Nagar", "prime"))


# ---------------------------------------------------------------------
# Q5: Uniform Cost Search - least-cost path S -> G (parent-pointer version)
# ---------------------------------------------------------------------
import heapq

delivery_network = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': [],
}


def uniform_cost_search(start, goal):
    frontier = [(0, start)]
    best_cost = {start: 0}
    parent = {start: None}
    explored = set()

    while frontier:
        cost, node = heapq.heappop(frontier)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return cost, path

        if node in explored:
            continue
        explored.add(node)

        for neighbour, step_cost in delivery_network[node]:
            new_cost = cost + step_cost
            if neighbour not in best_cost or new_cost < best_cost[neighbour]:
                best_cost[neighbour] = new_cost
                parent[neighbour] = node
                heapq.heappush(frontier, (new_cost, neighbour))

    return None, None


total_cost, best_path = uniform_cost_search('S', 'G')
print("\nQ5: Uniform Cost Search")
print("Least-cost path:", best_path)
print("Total cost:", total_cost)
