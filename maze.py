import mazeworld
simpleMaze=mazeworld.Maze([['#',' ',' ','S'],['~',' ',' ',' '],[' ',' ',' ','E']])
print(simpleMaze)
simpleMazeAgent=mazeworld.DepthFirstSearchAgent()
mazeworld.testAgentOnMaze(simpleMazeAgent,simpleMaze)