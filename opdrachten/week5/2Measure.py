import timeit

CODE = '''
import random
import copy
import matplotlib.pyplot as plt

class edge:
    def __init__(self, var1, var2, nactionsx, nactionsy):
        self.rewards = [] #table with the local rewards
        self.x = var1
        self.y = var2
        for i in range(nactionsx):
            rew = []
            for j in range(nactionsy):
                rew.append( random.random() )
            self.rewards.append(rew)

    def localReward(self, xval, yval):
        return self.rewards[xval][yval]


class coordinationGraph:
    def __init__(self, noNodes, pEdge, noActions, seed=random.random()):
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
        result = 0
        for i in range(len(solution)):
            for j in self.nodesAndConnections[i]:
                if(j>i):
                    #print( "("+str(i)+","+str(j)+") -> "+str(self.edges[(i,j)].localReward(solution[i], solution[j])))
                    result += self.edges[(i,j)].localReward(solution[i], solution[j])
        return result

    def evaluateChange(self, oldSolution, variableIndex, newValue):
        oldReward = self.evaluateSolution(oldSolution)
        oldSolution[variableIndex] = newValue
        newReward = self.evaluateSolution(oldSolution)

        delta = newReward - oldReward
        
        return delta

def localSearch4CoG(coordinationGraph, initialSolution):
    solution = initialSolution
    stop = False
    vars = list(coordinationGraph.nodesAndConnections.keys())
    random.shuffle(vars) # shuffle nodes

    while(vars): # loop over nodes
        node = vars.pop(0)
        for state in range(3): # loop over the 3 states
            delta = coordinationGraph.evaluateChange(solution, node, state) # get change
            if(delta > 0): # if better
                solution[node] = state # new state
                random.shuffle(vars) # shuffle nodes again
                break;

    return solution

def multiStartLocalSearch4CoG(coordinationGraph, noIterations):
    solution = None
    reward = 0
    return solution, reward

def iteratedLocalSearch4CoG(coordinationGraph, pChange, noIterations):
    solution = None
    reward = 0
    return solution, reward

nVars = 50
nActs = 3
cog = coordinationGraph(nVars,1.5/nVars,nActs)

# 100 times
for i in range(100):
    cog.evaluateSolution(localSearch4CoG(cog, [2]*nVars))
'''

import random
import copy
import matplotlib.pyplot as plt

class edge:
    def __init__(self, var1, var2, nactionsx, nactionsy):
        self.rewards = [] #table with the local rewards
        self.x = var1
        self.y = var2
        for _ in range(nactionsx):
            rew = []
            for _ in range(nactionsy):
                rew.append( random.random() )
            self.rewards.append(rew)

    def localReward(self, xval, yval):
        return self.rewards[xval][yval]


class coordinationGraph:
    def __init__(self, noNodes, pEdge, noActions, seed=random.random()):
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
        result = 0
        for i in range(len(solution)):
            for j in self.nodesAndConnections[i]:
                if(j>i):
                    result += self.edges[(i,j)].localReward(solution[i], solution[j])
        return result

    def evaluateChange(self, oldSolution, variableIndex, newValue):
        oldReward = self.evaluateSolution(oldSolution)
        oldSolution[variableIndex] = newValue
        newReward = self.evaluateSolution(oldSolution)

        delta = newReward - oldReward
        
        return delta

def localSearch4CoG(coordinationGraph, initialSolution):
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
    solution = None
    reward = 0
    return solution, reward

def iteratedLocalSearch4CoG(coordinationGraph, pChange, noIterations):
    solution = None
    reward = 0
    return solution, reward

nVars = 50
nActs = 3
cog = coordinationGraph(nVars,1.5/nVars,nActs)
rewardList = []

# 100 times
for i in range(100):
    rewardList.append(cog.evaluateSolution(localSearch4CoG(cog, [2]*nVars)))

# Histogram
n, bins, patches = plt.hist(rewardList, 10, facecolor='blue', alpha=0.5)
plt.xlabel("Reward")
plt.ylabel("Count")
plt.show()

print(str(timeit.timeit(stmt = CODE, number = 1) / 100) + " seconds")