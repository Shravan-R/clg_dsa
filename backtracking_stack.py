# rules is just going right and left or up not down if u come down then it is a back tracking program

def solve_maze(maze, start, end):
    path_stack = []
    visited = set()

    path_stack.append(start)
    visited.add(start)

    moves = [(-1,0), (0,-1), (0,1)]

    while path_stack:
        r, c = path_stack[-1]

        if (r, c) == end:
            return path_stack

        found_move = False

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if (0 <= nr < len(maze) and
                0 <= nc < len(maze[0]) and
                maze[nr][nc] != 1 and
                (nr, nc) not in visited):

                path_stack.append((nr, nc))
                visited.add((nr, nc))
                found_move = True
                break

        if not found_move:
            path_stack.pop()

    return None


maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [1,1,1,1,0],
    [0,0,0,1,0]
]

start = (0, 0)
end = (4, 4)

path = solve_maze(maze, start, end)
print(path)
