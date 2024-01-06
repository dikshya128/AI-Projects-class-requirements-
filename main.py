import copy
import pydot
import numpy as np
class Node:
    goal_state =np.array([[8,0,3], [2,6,4], [1,7,5]])
    i = 0
    def __init__(self,state,parent,action,depth):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth
        if self.goal_test():
            color = 'blue'
        elif self.solution():
            color = 'green'
        else:
            color = 'red'
        print(f"Node state: {self.state}, Color: {color}")
        self.graph_node = pydot.Node(str(self),style='filled',fillcolor = color)
        if self.goal_test():
            self.graph_node.set_fillcolor('blue')
        Node.i+=1

    def __str__(self):
        return str(self.state)

    def goal_test(self):
        if np.array_equal(self.state, self.goal_state):
            # print(f"Goal Test True for state: {self.state}")
            return True
        # return False

    def findZero(self):
        for i in range(len(self.state)):
            row = self.state[i]
            for j in range(len(row)):
                if row[j] == 0:
                    return (i, j)

    def DrawPossibleStates(self):
        i, j = self.findZero()
        depth = self.depth + 1
        state_list = []

        if i > 0:
            # Move the empty tile up
            new_data = copy.deepcopy(self.state)
            new_data[i][j], new_data[i - 1][j] = new_data[i - 1][j], new_data[i][j]
            action = ['u']
            new_node = Node(new_data,self,action,depth)
            state_list.append(new_node)

        if j > 0:
            # Move the empty tile left
            new_data = copy.deepcopy(self.state)
            new_data[i][j], new_data[i][j - 1] = new_data[i][j - 1], new_data[i][j]
            action = ['l']
            new_node = Node(new_data,self,action,depth)
            state_list.append(new_node)


        if i < 2:
            # Move the empty tile down
            new_data = copy.deepcopy(self.state)
            new_data[i][j], new_data[i + 1][j] = new_data[i + 1][j], new_data[i][j]
            action = ['d']
            new_node = Node(new_data,self,action,depth)
            state_list.append(new_node)

        if j < 2:
            # Move the empty tile right
            new_data = copy.deepcopy(self.state)
            new_data[i][j], new_data[i][j + 1] = new_data[i][j + 1], new_data[i][j]
            action = ['r']
            new_node = Node(new_data,self,action,depth)
            state_list.append(new_node)
        return state_list

    def solution(self):
        soln = [self.state]
        path = self
        while path.parent != None:
            soln.insert(0,path.parent.state)
            path = path.parent
        return soln

