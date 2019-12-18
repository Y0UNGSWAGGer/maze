from builtins import len, range, Exception, list, open, abs
import search
import util


## Module Classes

class Maze:
    """
    A Maze is represented by a 2-D matrix, or grid, of spaces,
    which are either clear or blocked. The grid passed in
    should be square (have the same number of rows as columns)

    Note: When you alter cell (x,y), the x corresponds to the
    row number (the vertical axis) and the y corresponds to the
    column or horizontal axis

    Each cell of the grid should be a single character.
      '#': Indicates an obstacle cell (impassable)
      '~': Indicates a water cell (passable but expensive)
      ' ': Empty Square (passable)
      'S': Indicates the starting cell
      'E': Indicates the exit cell
    """

    def __init__(self, grid):
        """
          grid: Should be a 2-D matrix: a list of lists
          e.g. [['#','S',' '],['#',' ','E']]
          Each of the sub-lists should be of the same
          length so that the grid is rectangular

         Constructs a maze from the passed in grid
        """
        self.grid = grid
        self.numRows = len(grid)
        self.numCols = len(grid[0])
        for i in range(self.numRows):
            for j in range(self.numCols):
                if len(grid[i]) != self.numCols:
                    raise Exception("Grid is not Rectangular")
                if grid[i][j] == 'S':
                    self.startCell = (i, j)
                if grid[i][j] == 'E':
                    self.exitCell = (i, j)
        if self.exitCell == None:
            raise Exception("No Start Cell in Grid")
        if self.startCell == None:
            raise Exception("No Exit Cell in Grid")

    def isPassable(self, x, y):
        """
          x: row position
          y: col position

        Returns true if the (x,y) cell
        is passable, i.e is a ' ' or '~'
        """
        #判断是否可行
        return self.isWater(x, y) or self.isClear(x, y)

    def isWater(self, x, y):
        """
          x: row position
          y: col position

        Returns true if the (x,y) cell
        is water, i.e is a '~'
        """
        #ez
        return self.grid[x][y] == '~'

    def isClear(self, x, y):
        """
          x: row position
          y: col position

        Returns true if the (x,y) cell
        is clear, i.e is a ' '
        """
        #ez
        return self.grid[x][y] == ' '

    def isBlocked(self, x, y):
        """
          x: row position
          y: col position

        Returns true if the (x,y) cell
        is blocked, i.e has a '#' char
        """
        #ez
        return self.grid[x][y] == '#'

    def setBlock(self, x, y):
        """
          x: row position
          y: col position

         Place a block at the (x,y) position
         of the grid. The cell must be clear
        """
        if (self.grid[x][y] != 'S' and self.grid[x][y] != 'E'):
            self.grid[x][y] = '#'

    def setClear(self, x, y):
        """
          x: row position
          y: col position

        Sets the (x,y) to be clear if
        the cell is not the start or the
        exit of the maze
        """
        if (self.grid[x][y] != 'S' and self.grid[x][y] != 'E'):
            self.grid[x][y] = ' '

    def setWater(self, x, y):
        """
          x: row position
          y: col position

        Sets the (x,y) to be clear if
        the cell is not the start or the
        exit of the maze
        """
        if (self.grid[x][y] != 'S' and self.grid[x][y] != 'E'):
            self.grid[x][y] = '~'

    def getNumRows(self):
        """
          Returns number of rows in maze
        """
        return self.numRows

    def getNumCols(self):
        """
          Return number of cols in maze
        """
        return self.numCols

    def getStartCell(self):
        """
          Returns (x,y) position of start cell
        """
        return self.startCell

    def getExitCell(self):
        """
          Returns (x,y) position of exit cell
        """
        return self.exitCell

    def __getAsciiString(self):
        """
          Returns a display string for the maze
        """
        lines = []
        headerLine = ' ' + ('-' * (self.numCols)) + ' '
        lines.append(headerLine)
        for row in self.grid:
            rowLine = '|' + ''.join(row) + '|'
            lines.append(rowLine)
        lines.append(headerLine)
        #加个头和尾
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()


class MazeSearchProblem(search.SearchProblem):
    """
      Implementation of a SearchProblem for the 
      Maze World domain
      
      Each state is encoded as a (x,y) pair for the 
      position in the grid. The start state is the 
      start cell for the maze and the only goal is the
      Maze exit cell. 
    """

    def __init__(self, maze):
        """

        """
        self.maze = maze
        self.numNodesExpanded = 0
        self.expandedNodeSet = {}

    def getStartState(self):
        """

        """
        return self.maze.getStartCell()

    def isGoalState(self, state):
        """

        """
        return state == self.maze.getExitCell()

    def __isValidState(self, state):
        """
          state: Cell position

        Returns true is the given state corresponds
        to an unblocked and valid maze position
        """
        x, y = state
        if x < 0 or x >= self.maze.getNumRows():
            return False
        if y < 0 or y >= self.maze.getNumCols():
            return False
        return not self.maze.isBlocked(x, y)

    def getSuccessors(self, state):
        """
          state: Cell position 
        
        Returns list of (successor,cost) pairs where
        each succesor is either left, right, up, or down 
        from the original state and the cost is 1.0 for each
        """
        # Update Search Stats
        self.numNodesExpanded += 1
        self.expandedNodeSet[state] = 1
        states = []
        x, y = state
        # Right
        states.append((x, y + 1))
        # Down
        states.append((x + 1, y))
        # Left
        states.append((x, y - 1))
        # Up 
        states.append((x - 1, y))

        # So successors appear in order (Right,Down,Left,Up)
        states.reverse()
        return [(x, self.getCost(x)) for x in states if self.__isValidState(x)]

    def getCost(self, state):
        """
          Returns the step cost of entering each terrain type.

          Blank spaces have cost 1.
          Water spaces have cost 5.
        """
        x, y = state
        if self.maze.isClear(x, y):
            return 1
        elif self.maze.isWater(x, y):
            return 5
        elif state == self.maze.getStartCell() or state == self.maze.getExitCell():
            return 1
        else:
            raise Exception("The cost of an impassable cell is undefined.")

    def getMaze(self):
        return self.maze

    # Search Stats

    def displaySearchStats(self):
        """
          Display number of nodes expanded by 'getSuccessors'
        """
        print('Number of nodes expanded:', self.numNodesExpanded)
        print('Number of unique nodes expanded:', len(self.expandedNodeSet))

    def resetSearchStats(self):
        self.numNodesExpanded = 0
        self.expandedNodeSet = {}


class DepthFirstSearchAgent(search.SearchAgent):
    """
      DepthFirstSearchAgent

    Implements depth-first graph search for a given problem.
    """

    def solve(self, mazeSearchProblem):
        solution = []
        cost = 0.0
        cell = mazeSearchProblem.getStartState()
        while True:
            solution.append(cell)
            if mazeSearchProblem.isGoalState(cell):
                return solution, cost
            nextCell, nextCost = None, 0.0
            for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
                delta_y = successor[1] - cell[1]
                if delta_y == 1:  # right
                    nextCell = successor
                    nextCost = stepCost
                    break
            for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
                delta_x = successor[0] - cell[0]
                if delta_x == 1:  # down
                    nextCell = successor
                    nextCost = stepCost
                    break
            for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
                delta_y = successor[1] - cell[1]
                if delta_y == -1:  # left
                    nextCell = successor
                    nextCost = stepCost
                    break
            for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
                delta_x = successor[0] - cell[0]
                if delta_x == -1:  # up
                    nextCell = successor
                    nextCost = stepCost
                    break
            if nextCell != None:
                cell = nextCell
                cost += nextCost
            else:
                print("SimpleMazeAgent: Can't move right, quitting")
                return (None, 0.0)
    ## Simple Maze Agent


class SimpleMazeAgent(search.SearchAgent):
    """
      Keeps moving to the right as long as it can
    """

    def solve(self, mazeSearchProblem):
        solution = []
        cost = 0.0
        cell = mazeSearchProblem.getStartState()
        # Move to the right as long as we can
        while True:
            solution.append(cell)
            if mazeSearchProblem.isGoalState(cell):
                return solution, cost
            nextCell, nextCost = None, 0.0
            for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
                delta_y = successor[0] - cell[0]
                if delta_y == 1:  # Right
                    nextCell = successor
                    nextCost = stepCost
                    break
            if nextCell != None:
                cell = nextCell
                cost += nextCost
            else:
                print("SimpleMazeAgent: Can't move right, quitting")
                return (None, 0.0)


## Maze Heuristic Function Classes

def manhattanDistance(state, mazeSearchProblem):
    """
      Returns the Manhattan distance between the state
      and the goal for the provided maze.
      
      The manhattan distance between points (x0,y0)
      and (x1,y1) is |x0-x1| + |y0-y1|
    """
    maze = mazeSearchProblem.maze
    delta_x = maze.getExitCell()[0] - state[0]
    delta_y = maze.getExitCell()[1] - state[1]
    return abs(delta_x) + abs(delta_y)


## Module Methods

def testAgentOnMaze(agent, maze, verbose=True):
    """
       Test the search agent 'agent' on the 'maze'
       and prints the cost of the solution and also
       displays the maze along with 'x' for the cells
       used in the solution and 'o' for cells expanded
       but not used in the solution
    """
    problem = MazeSearchProblem(maze)
    solution, cost = agent.solve(problem)
    if solution == None:
        print('No solution found!')
        problem.displaySearchStats()
        problem.resetSearchStats()
        return
    if verbose:
        grid_copy = []
        for row in maze.grid:
            grid_copy.append([x for x in row])
        for x, y in problem.expandedNodeSet:
            ch = maze.grid[x][y]
            if ch != 'S' and ch != 'E': grid_copy[x][y] = 'o'
        for x, y in solution:
            ch = maze.grid[x][y]
            if ch != 'S' and ch != 'E': grid_copy[x][y] = 'x'
        maze_copy = Maze(grid_copy)
        print(maze_copy)
        print("x - cell used in solution")
        print("o - cell expanded during search")
        print("-------------------------------")
    print('Solution cost:', cost)
    problem.displaySearchStats()


def readMazeFromFile(file):
    """
      file: Name of file containing maze
      
     Returns a Maze instance 
    """
    fin = open(file)
    lines = fin.read().splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))
    return Maze(grid)


def createEmptyMaze(rows, cols):
    """
    Returns an empty (rows x cols) maze with a central entrace
    and an exit at the right
    """
    grid = []
    for i in range(rows):
        grid.append([' ' for x in range(cols)])
    grid[rows / 2][cols / 2] = 'S'
    grid[rows / 2][cols - 1] = 'E'
    return Maze(grid)
