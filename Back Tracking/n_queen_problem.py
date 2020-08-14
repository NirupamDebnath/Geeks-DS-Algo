import unittest

N = 8
count = 0

def solveNQ(): 
    board = [ [0]*N for i in range(N) ]   
    solveNQUtil(board, 0)

def printSolution(board):
    print(*board, sep="\n", end="\n\n")

def is_safe(board, y, x):

    for i in range(0,x):
        if board[y][i] == 1:
            return False

    for j, i in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if board[j][i] == 1:
            return False
    
    for j, i in zip(range(y+1, N, 1), range(x-1, -1, -1)):
        if board[j][i] == 1:
            return False

    return True

def solveNQUtil(board, x):
    if x >= N:
        printSolution(board)
        global count
        count += 1
        return

    for y in range(N):
        board[y][x] = 1
        if is_safe(board, y, x) == True:
        #     if solveNQUtil(board, x+1) == True:
        #         return True
        # board[y][x] = 0

            solveNQUtil(board, x+1)
        board[y][x] = 0

class NqueenTests(unittest.TestCase):
    def test_is_safe(self):
        board = [[0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0]]
        self.assertEqual(is_safe(board, 0,2), False)

if __name__ == "__main__":
    # unittest.main()
    solveNQ() 
    print(count)




