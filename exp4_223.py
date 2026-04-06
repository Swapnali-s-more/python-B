# Simple Wumpus World Implementation
# ---------------------------------

# Grid size: 4x4
GRID = 4

# Environment (fixed)
wumpus = (1, 2)
pit = (2, 1)
gold = (3, 3)

# Agent knowledge
safe_cells = set()
visited = set()
possible_pit = set()
possible_wumpus = set()

# Start position
agent_pos = (0, 0)
safe_cells.add(agent_pos)


def neighbors(cell):
    x, y = cell
    n = []
    if x > 0:
        n.append((x - 1, y))
    if x < GRID - 1:
        n.append((x + 1, y))
    if y > 0:
        n.append((x, y - 1))
    if y < GRID - 1:
        n.append((x, y + 1))
    return n


def perceive(cell):
    percepts = []
    for n in neighbors(cell):
        if n == pit:
            percepts.append("Breeze")
        if n == wumpus:
            percepts.append("Stench")
    return percepts


def infer(cell, percepts):
    adj = neighbors(cell)

    if "Breeze" not in percepts:
        for a in adj:
            safe_cells.add(a)
    else:
        for a in adj:
            possible_pit.add(a)

    if "Stench" not in percepts:
        for a in adj:
            safe_cells.add(a)
    else:
        for a in adj:
            possible_wumpus.add(a)


def choose_move(cell):
    for n in neighbors(cell):
        if n in safe_cells and n not in visited:
            return n
    return None


# ---------------- MAIN LOOP ----------------

print("Simple Wumpus World Simulation\n")

for step in range(10):
    print(f"Step {step + 1}")
    print("Agent at:", agent_pos)

    visited.add(agent_pos)

    percepts = perceive(agent_pos)
    print("Percepts:", percepts if percepts else "None")

    infer(agent_pos, percepts)

    move = choose_move(agent_pos)

    if move:
        print("Moving to:", move, "\n")
        agent_pos = move
    else:
        print("No safe move available. Stopping.\n")
        break

print("Visited cells:", visited)
print("Safe cells:", safe_cells)
print("Possible pits:", possible_pit)
print("Possible wumpus:", possible_wumpus)

if agent_pos == gold:
    print("Agent found the gold!")
else:
    print("Agent did not reach the gold.")