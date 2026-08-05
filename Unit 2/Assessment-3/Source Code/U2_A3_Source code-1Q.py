import heapq
import itertools

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 3), ('D', 7), ('E', 2)],
    'C': [('A', 4), ('B', 3), ('E', 3)],
    'D': [('B', 7), ('E', 2), ('G', 2)],
    'E': [('B', 2), ('C', 3), ('D', 2)],
    'G': [],
}

heuristic = {'A': 7, 'B': 6, 'C': 4, 'D': 3, 'E': 2, 'G': 0}


def reconstruct_path(parent, node):
    path = [node]
    while parent[node] is not None:
        node = parent[node]
        path.append(node)
    path.reverse()
    return path


def a_star(start, goal):

    tie_breaker = itertools.count()
    open_heap = [(heuristic[start], 0, next(tie_breaker), start)]
    open_set = {start}
    closed = []
    g_score = {start: 0}
    parent = {start: None}

    iteration = 1

    while open_heap:

        f, g, _, node = heapq.heappop(open_heap)

        if node in closed:
            continue

        open_set.discard(node)

        print("\n======================================")
        print("Iteration :", iteration)
        print("Current Node :", node)

        print("Open List :", sorted([(n, g_score[n] + heuristic[n]) for n in open_set]))
        print("Closed List :", closed)

        print("g(n) =", g)
        print("h(n) =", heuristic[node])
        print("f(n) =", f)

        if node == goal:

            path = reconstruct_path(parent, node)
            print("\nGoal Reached")
            print("Optimal Path :", " -> ".join(path))
            print("Total Cost :", g)
            return

        closed.append(node)

        for neighbour, cost in graph[node]:

            if neighbour in closed:
                continue

            tentative_g = g + cost

            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                parent[neighbour] = node
                new_f = tentative_g + heuristic[neighbour]
                heapq.heappush(open_heap, (new_f, tentative_g, next(tie_breaker), neighbour))
                open_set.add(neighbour)

        iteration += 1

    print("No path found.")


while True:

    start = input("\nEnter Start Node : ").upper()
    goal = input("Enter Goal Node : ").upper()

    a_star(start, goal)

    ch = input("\nSearch Again?(y/n): ")

    if ch.lower() != 'y':
        break
