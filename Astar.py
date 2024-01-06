from mainA import Node
import numpy as np
import pydot
from queue import PriorityQueue
def Astar(initial_state):
    graph = pydot.Dot(graph_type='digraph',fontsize='20',fontcolor='black',style='filled')
    count = 0
    start_node = Node(initial_state,None,None,0)
    # if start_node.goal_test():
    #     start_node.solution()
    q = PriorityQueue()
    explored_states = []
    q.put((start_node.evaluation_function,count,start_node))
    while not q.empty():
        current_node = q.get()
        current_node = current_node[2]
        explored_states.append(current_node.state)
        graph.add_node(current_node.graph_node)
        if current_node.goal_test():
            return current_node.solution()
        Children = current_node.DrawPossibleStates()
        for child in Children:
            if not any(np.array_equal(child.state, state) for state in explored_states):
                if child.goal_test():
                    path = [child.state]
                    graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, label=str(child.action)))
                    graph.write_png(f'AStar/solutions{child.depth}.png')
                    while child.parent != None:
                        path.insert(0, child.parent.state)
                        child = child.parent
                    return path
                count +=1
                q.put((child.evaluation_function,count,child))
                explored_states.append(child.state)
                graph.add_edge(pydot.Edge(current_node.graph_node, child.graph_node, label=str(child.action)))
                graph.write_png(f'AStar/solutions{child.depth}.png')

    return None

initial_state = np.array([[2,8,3], [1,6,4], [7,0,5]])
solution = Astar(initial_state)
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print

