def if_safe(maze, x, y):
    if x < len(maze[0]) and y < len(maze) and maze[x][y] == 1:
        return True
    return False

def solveMaze(maze):
    sol = [[0]*len(maze[0]) for i in range(len(maze))]

    if solve_maze_util(maze, 0, 0, sol) == True:
        print(*sol, sep = "\n")
    else:
        print("No Solution")

def solve_maze_util(maze, x, y, sol):
    if x == len(maze[0]) - 1 and y == len(maze) - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if if_safe(maze, x, y):
        sol[x][y] = 1
        if solve_maze_util(maze, x+1, y, sol) == True:
            return True
        
        if solve_maze_util(maze, x, y+1, sol) == True:
            return True
        sol[x][y] = 0
        
    return False

if __name__ == "__main__": 
    # Initialising the maze 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
               
    solveMaze(maze) 