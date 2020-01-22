import random
import copy

class edge:

    def __init__(self, var1, var2, nactionsx, nactionsy):
        """
        Constructor for the edge class
        :param var1: the (index of the) first decision variable
        :param var2: the (index of the) second decision variable
        :param nactionsx: the number of possible values for var1
        :param nactionsy: the number of possible values for var1
        """
        self.rewards = [] #table with the local rewards
        self.x = var1
        self.y = var2
        for _ in range(nactionsx):
            rew = []
            for _ in range(nactionsy):
                rew.append( random.random() )
            self.rewards.append(rew)

    def localReward(self, xval, yval):
        """
        Return the local reward for this edge given the values of the connected decision variables
        :param xval: value of the first decision variable
        :param yval: value of the second decision variable
        :return: the local reward
        """
        return self.rewards[xval][yval]


class coordinationGraph:

    def __init__(self, noNodes, pEdge, noActions, seed=42):
        """
        Constructor for the coordination graph class. It generates a random graph based on a seed.

        :param noNodes: The number of vertices in the graph. Each vertex represents a decision variable.
        :param pEdge: the probability that an edge will be made
        :param noActions: the number of possible values (integers between 0 and noActions) for the decision variables
        :param seed: the pre-set seed for the random number generator
        """
        random.seed(seed)
        self.nodesAndConnections = dict() #for each node, a list of nodes it is connected to
        self.edges = dict() #A dictionary of tuples (of two decision variables) to an object of the edge class
        for i in range(noNodes): #First make sure that the entire graph is connected (connecting all nodes to the next one)
            if i == 0:
                self.nodesAndConnections[i] = [i + 1]
                self.nodesAndConnections[i+1] = [i]
                eddy = edge(i, i+1, noActions, noActions)
                self.edges[(i,i+1)] = eddy
            elif i <noNodes-1:
                self.nodesAndConnections[i].append(i + 1)
                self.nodesAndConnections[i + 1] = [i]
                eddy = edge(i, i + 1, noActions, noActions)
                self.edges[(i, i + 1)] = eddy
        tuplist = [(x, y) for x in range(noNodes) for y in range(x + 2, noNodes)]
        for t in tuplist: #Then, for each possible edge, randomly select which exist and which do not
            r = random.random()
            if r < pEdge:
                self.nodesAndConnections[t[0]].append(t[1])
                self.nodesAndConnections[t[1]].append(t[0])
                self.edges[t] = edge(t[0], t[1], noActions, noActions)
        #For reasons of structure, finally, let's sort the connection lists for each node
        for connections in self.nodesAndConnections.values():
            connections.sort()

    def evaluateSolution(self, solution):
        """
        Evaluate a solution from scratch; by looping over all edges.

        :param solution: a list of values for all decision variables in the coordination graph
        :return: the reward for the given solution.
        """
        result = 0
        for i in range(len(solution)):
            for j in self.nodesAndConnections[i]:
                if(j>i):
                    #print( "("+str(i)+","+str(j)+") -> "+str(self.edges[(i,j)].localReward(solution[i], solution[j])))
                    result += self.edges[(i,j)].localReward(solution[i], solution[j])
        return result

    def evaluateChange(self, oldSolution, variableIndex, newValue):
        """
        TODO: a function that evaluates a local change. Specifically

        :param oldSolution: The original solution
        :param variableIndex: the index of the decision variable that is changing
        :param newValue: the new value for the decision variable
        :return: The difference in reward between the old solution and the new solution (with solution[variableIndex] set to newValue)
        """
        oldReward = self.evaluateSolution(oldSolution)
        oldSolution[variableIndex] = newValue
        newReward = self.evaluateSolution(oldSolution)

        delta = newReward - oldReward
        
        return delta

def localSearch4CoG(coordinationGraph, initialSolution):
    """
    TODO: Implement local search
    :param coordinationGraph: the coordination graph to optimise for
    :param initialSolution: an initial solution for the coordination graph
    :return: a new solution (a local optimum)
    """
    solution = initialSolution

    vars = list(coordinationGraph.nodesAndConnections.keys())
    random.shuffle(vars) # shuffle nodes

    while(vars): # loop over nodes
        node = vars.pop(0)
        for state in range(3): # loop over the 3 states
            delta = coordinationGraph.evaluateChange(solution, node, state) # get change
            if(delta > 0): # if better
                solution[node] = state # new state
                random.shuffle(vars) # shuffle nodes again
                break

    return solution

def multiStartLocalSearch4CoG(coordinationGraph, noIterations):
    """
    TODO: Implement multi-start local search

    :param coordinationGraph: the coordination graph to optimise for
    :param noIterations:  the number of times local search is run
    :return: the best local optimum found and its reward
    """
    solution = None
    reward = 0
    return solution, reward


def iteratedLocalSearch4CoG(coordinationGraph, pChange, noIterations):
    """
    TODO: Implement iterated local search

    :param coordinationGraph: the coordination graph to optimise for
    :param pChange: the perturbation strength, i.e., when mutating the solution, the probability for the value of a given
                    decision variable to be set to a random value.
    :param noIterations:  the number of iterations
    :return: the best local optimum found and its reward
    """
    solution = None
    reward = 0
    return solution, reward

nVars = 50
nActs = 3
cog = coordinationGraph(nVars,1.5/nVars,nActs)
print(cog.evaluateSolution(localSearch4CoG(cog, [2]*nVars)))