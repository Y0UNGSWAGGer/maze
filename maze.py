import mazeworld as  mz

if __name__ == "__main__":
    simpleMaze = mz.Maze(
    [['#', ' ', ' ', 'S'], ['~', ' ', ' ', ' '], [' ', ' ', ' ', 'E']])
    
    print(simpleMaze)
    simpleMazeAgent = mz.DepthFirstSearchAgent()

    mz.testAgentOnMaze(simpleMazeAgent, simpleMaze)


