import mazeworld

if __name__ == "__main__":
    simpleMaze = mazeworld.Maze(
    [['#', ' ', ' ', 'S'], ['~', ' ', ' ', ' '], [' ', ' ', ' ', 'E']])
    
    print(simpleMaze)
    simpleMazeAgent = mazeworld.DepthFirstSearchAgent()

    mazeworld.testAgentOnMaze(simpleMazeAgent, simpleMaze)


