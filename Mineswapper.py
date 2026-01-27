import random
import matplotlib.pyplot as plt
import time

rows, cols = 8, 8
games_per_step = 100
mine_range = range(1, 30, 4)

def create_board(num_mines):
    board = [['_' for _ in range(cols)] for _ in range(rows)]
    backend = [['0' for _ in range(cols)] for _ in range(rows)]
    mines_pos = set()
    while len(mines_pos) < num_mines:
        mines_pos.add((random.randint(0, rows - 1), random.randint(0, cols - 1)))
    for r, c in mines_pos:
        backend[r][c] = 'X'
    for r in range(rows):
        for c in range(cols):
            if backend[r][c] == 'X': continue
            count = sum(1 for i, j in get_neighbors(r, c) if backend[i][j] == 'X')
            backend[r][c] = str(count)
    return board, backend, list(mines_pos)

def get_neighbors(r, c):
    return [(i, j) for i in range(r-1, r+2) for j in range(c-1, c+2) 
            if 0 <= i < rows and 0 <= j < cols and (i, j) != (r, c)]

def flood_fill(r, c, board, backend):
    if board[r][c] != '_': return 0
    board[r][c] = backend[r][c]
    count = 1
    if backend[r][c] == '0':
        for nr, nc in get_neighbors(r, c):
            count += flood_fill(nr, nc, board, backend)
    return count

#AI Moves
def random_ai_move(board):
    hidden = [(r, c) for r in range(rows) for c in range(cols) if board[r][c] == '_']
    return random.choice(hidden) if hidden else None


def rule1_logic(board):
    for r in range(rows):
        for c in range(cols):
            if board[r][c].isdigit() and int(board[r][c]) > 0:
                neighbors = get_neighbors(r, c)
                flags = [n for n in neighbors if board[n[0]][n[1]] == 'F']
                hidden = [n for n in neighbors if board[n[0]][n[1]] == '_']
                if int(board[r][c]) == len(flags) and hidden:
                    return hidden[0]
    return None

def rule2_logic(board):
    for r in range(rows):
        for c in range(cols):
            if not board[r][c].isdigit(): continue
            n1_hidden = set(n for n in get_neighbors(r, c) if board[n[0]][n[1]] == '_')
            n1_needed = int(board[r][c]) - sum(1 for n in get_neighbors(r, c) if board[n[0]][n[1]] == 'F')
            if n1_needed <= 0: continue
            for nr, nc in get_neighbors(r, c):
                if not board[nr][nc].isdigit(): continue
                n2_hidden = set(n for n in get_neighbors(nr, nc) if board[n[0]][n[1]] == '_')
                n2_needed = int(board[nr][nc]) - sum(1 for n in get_neighbors(nr, nc) if board[n[0]][n[1]] == 'F')
                if n1_hidden.issubset(n2_hidden) and n1_hidden:
                    if n2_needed == n1_needed and len(n2_hidden) > len(n1_hidden):
                        return list(n2_hidden - n1_hidden)[0] 
    return None

#Game Rules
def place_flags(board):
    changed = True
    while changed:
        changed = False
        for r in range(rows):
            for c in range(cols):
                if board[r][c].isdigit():
                    num = int(board[r][c])
                    neighbors = get_neighbors(r, c)
                    hidden = [n for n in neighbors if board[n[0]][n[1]] == '_']
                    flags = [n for n in neighbors if board[n[0]][n[1]] == 'F']
                    if num == len(hidden) + len(flags) and hidden:
                        for hr, hc in hidden:
                            board[hr][hc] = 'F'
                            changed = True

def play_game(ai_type, num_mines):
    board, backend, m_list = create_board(num_mines)
    revealed_count, target = 0, (rows * cols) - len(m_list)
    start_time = time.time()
    
    first_move = True
    
    while revealed_count < target:
        if ai_type != "random": place_flags(board)
        
        if ai_type == "random": move = random_ai_move(board)
        elif ai_type == "rule1": move = rule1_logic(board) or random_ai_move(board)
        elif ai_type == "rule2": move = rule1_logic(board) or rule2_logic(board) or random_ai_move(board)
        if not move: break
        r, c = move
        
        if first_move:
            while backend[r][c] != '0':
                board, backend, m_list = create_board(num_mines)
            first_move = False
        if backend[r][c] == 'X': return 0, time.time() - start_time
        revealed_count += flood_fill(r, c, board, backend)
    return 1, time.time() - start_time

#Data
win_data = {"random": [], "rule1": [], "rule2": []}
time_data = {"random": [], "rule1": [], "rule2": []}

for m in mine_range:
    for ai in win_data.keys():
        wins, durations = 0, 0
        for _ in range(games_per_step):
            res, dur = play_game(ai, m)
            wins += res
            durations += dur
        win_data[ai].append((wins / games_per_step) * 100)
        time_data[ai].append(durations / games_per_step)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

colors = {'random': 'red', 'rule1': 'blue', 'rule2': 'green', 'rule3': 'purple'}

for ai in win_data.keys():
    ax1.plot(list(mine_range), win_data[ai], label=ai, marker='o', color=colors[ai])
    ax2.plot(list(mine_range), time_data[ai], label=ai, marker='s', color=colors[ai])

ax1.set_title('AI Accuracy (Win Rate %)'); ax1.set_ylabel('Win %')
ax2.set_title('Computational Cost (Seconds)'); ax2.set_ylabel('Seconds')
ax1.set_xlabel('Number of Mines')
ax2.set_xlabel('Number of Mines')
ax1.set_ylabel('Win Rate (%)')
ax2.set_ylabel('Average Time (s)')
ax1.grid(True); ax2.grid(True)
ax1.legend(); ax2.legend()
plt.show()