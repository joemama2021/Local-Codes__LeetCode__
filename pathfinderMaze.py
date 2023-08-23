def solver(maze):
    n = len(maze)
    for i in range(n):
        if maze[0][i] == 0:
            start = (0, i)
            break
    
    for i in range(n):
        if maze[n-1][i] == 0:
            end = (n-1, i)
            break

    def moveUP(curr):
        if curr[0]-1 >= 0 and maze[curr[0]-1][curr[1]] == 0:
            return (curr[0]-1, curr[1])
        return None

    def moveDown(curr):
        if curr[0]+1 < n and maze[curr[0]+1][curr[1]] == 0:
            return (curr[0]+1, curr[1])
        return None
            
    def moveLeft(curr):
        if curr[1]-1 >= 0 and maze[curr[0]][curr[1]-1] == 0:
            return (curr[0], curr[1]-1)
        return None
            
    def moveRight(curr):
        if curr[1]+1 < n and maze[curr[0]][curr[1]+1] == 0:
            return (curr[0], curr[1]+1)
        return None
            
    def find_path(curr):
        if curr == end:
            maze[end[0]][end[1]] = 2
            return True

        maze[curr[0]][curr[1]] = 2  # Mark the cell as visited

        next_positions = [
            moveUP(curr),
            moveDown(curr),
            moveLeft(curr),
            moveRight(curr)
        ]

        for next_pos in next_positions:
            if next_pos and maze[next_pos[0]][next_pos[1]] == 0:
                if find_path(next_pos):
                    return True

        maze[curr[0]][curr[1]] = 0  # Unmark the cell if no path found
        return False

    find_path(start)
    return maze


def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end=" ")
        print("")
    print("")

maze = [
    [1,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,0,1,1,1,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,1]
]

print_maze(maze)
result = solver(maze)
print_maze(result)