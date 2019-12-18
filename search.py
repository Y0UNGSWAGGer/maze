import util
import mazeworld


## Abstract Search Classes

class SearchProblem:
    """
    Abstract SearchProblem class. Your classes
    should inherit from this class and override
    all the methods below
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        # abstract

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state should return a list of pairs, (successor,stepCost),
        where 'successor' is a successor to the current state and
        'stepCost' is the incremental cost of expanding to that successor
        """
        # abstract

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        # abstract

    # These methods are used to evaluate SearchAgents

    def displaySearchStats(self):
        """
          Should display statistics regarding the amount of work
          down during search. For instance, the number of nodes
          expanded (how many times getSuccessors is called) and
          how many are discovered (found as a successor)
        """
        # abstract

    def resetSearchStats(self):
        """
          Reset internal state of problem for tracking
          search statistics. All search agents should
          call this method before doing any searching
        """
        # abstract


class SearchAgent:
    """
    Abstract SearchAgent class. Your agents should
    inherit from this class and override the solve
    method.
    """

    def solve(self, searchProblem):
        """
          searchProblem: SearchProblem subclass

        For the passed in 'searchProblem' should return a (solutionPath,cost) pair where
        'solutionPath' is a list of search states representing
        the solution to the problem and 'cost' is total cost of the solution.

        All subclasses should also first call searchProblem.resetSearchStats()
        before doing any searching.
        """
        # abstract


## Specific Search Agents
# ***Implement the classes below***

class DepthFirstSearchAgent(SearchAgent):
    """
      DepthFirstSearchAgent

    Implements depth-first graph search for a given problem.
    """

    def solve(self, msp):
        solution = []
        test = util.Stack()
        # test即DFS所用到的栈
        note = []
        # note记录所有已经探索过的结点，其中包含走不通的路径
        cost = 0.0
        cell = msp.getStartState()
        # 一些init的工作

        # while True:
        #     solution.append(cell)
        #     if mazeSearchProblem.isGoalState(cell):
        #         return solution, cost
        #     nextCell, nextCost = None, 0.0
        #     for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
        #         delta_y = successor[1] - cell[1]
        #         if delta_y == 1:  # right
        #             nextCell = successor
        #             nextCost = stepCost
        #             break
        #     for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
        #         delta_x = successor[0] - cell[0]
        #         if delta_x == 1:  # down
        #             nextCell = successor
        #             nextCost = stepCost
        #             break
        #     for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
        #         delta_y = successor[1] - cell[1]
        #         if delta_y == -1:  # left
        #             nextCell = successor
        #             nextCost = stepCost
        #             break
        #     for successor, stepCost in mazeSearchProblem.getSuccessors(cell):
        #         delta_x = successor[0] - cell[0]
        #         if delta_x == -1:  # up
        #             nextCell = successor
        #             nextCost = stepCost
        #             break
        #     if nextCell != None:
        #         cell = nextCell
        #         cost += nextCost
        #     else:
        #         print("SimpleMazeAgent: Can't move right, quitting")
        #         return (None, 0.0)
        test.push(cell)
        note.append(cell)
        # solution.append(cell)
        while True:
            if test.isEmpty():
                # 栈空了也莫得，就无解
                print("迷宫无解")
                solution = []
                cost = 0.0
                return (solution, cost)

            test_cell = test.pop()
            # test_cost=test_cost_note.pop()
            # print(solution)        just for debug
            solution.append(test_cell)
            note.append(test_cell)
            # 每出栈一个，就代表走了一步，所以要记在note里，同时也记在solution里
            # 但如果这条路错了，下文会处理将这个结点从solution里弹出
            cell = solution[-1]
            have_try = msp.getSuccessors(test_cell)
            # 即是对刚加入solution的这个结点调用自带的方法进行试探
            if msp.isGoalState(cell):
                # 成功
                for term in solution:
                    cost = cost + msp.getCost(term)
                return solution, cost
            else:
                i = 0
                # 这个i即是为了记录所有未经探索过的新结点数目

                for successor, stepCost in have_try:
                    if successor not in note:
                        i = i + 1
                        # print(successor)
                        test.push(successor)
                if i == 0:
                    # 如果一次试探里该数保持零，则说明走到了死胡同,就弹出solution的这步错路，但note仍保持
                    solution.pop()

                    # print(test)


class BreadthFirstSearchAgent(SearchAgent):
    """
       Breadth First Search

     Implements basic breadth-first-search for a given problem
    """

    def solve(self, searchProblem):
        """
            Solves the given searchProblem using Breadth
        first search.

        Returns (solutionPath,cost) pair where
        solutionPath is a list of the states
        starting from the start state to a goal
        state and cost is the total cost of the
        solution.
        """
        return (None, 0.0)


class UniformCostSearchAgent(SearchAgent):
    """
        UniformCostSearchAgent

    Implements uniform cost search
    """

    def solve(self, searchProblem):
        """
            searchProblem: Search problem

         Solves the given searchProblem using
        uniform cost search.

        Returns (solutionPath,cost) pair where
        solutionPath is a list of the states
        starting from the start state to a goal
        state and cost is the total cost of the
        solution.
        """
        return None, 0.0


class AStarSearchAgent(SearchAgent):
    """
       AStarSearchAgent

    Implements A* search. Should take
    a heuristicFn at construction. That
    heuristic function should take a
    state and search problem as its
    arguments.
    """

    def __init__(self, heuristicFn):
        self.heuristicFn = heuristicFn

    def solve(self, searchProblem):
        """
          searchProblem: Search Problem

        Solves the given searchProblem using AStar
        search with the heuristic function passed
        to the constructor.

        Returns (solutionPath,cost) pair where
        solutionPath is a list of the states
        starting from the start state to a goal
        state and cost is the total cost of the
        solution.

        The solution returned is guranteed to be
        the minimal cost solution
        """
        return (None, 0.0)
