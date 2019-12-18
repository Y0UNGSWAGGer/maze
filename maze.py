import mazeworld as  mz
from search import DepthFirstSearchAgent as dfsA

if __name__ == "__main__":
    simpleMaze = mz.Maze(
    [['#', '#', '_', 'S'],
     ['~', '_', '_', '#'],
     ['_', '#', '_', '#'],
     ['_', '_', '#', 'E'],
     ['_', '_', '_', '_']
    ])
    
    print(simpleMaze)
    simpleMazeAgent = dfsA()
    mz.testAgentOnMaze(simpleMazeAgent, simpleMaze)


