from queue import Queue
from main import Node
import numpy as np
import pydot
def bfs(initial_state):
    graph = pydot.Dot(graph_type='digraph',fontsize='20',color='gold',fontcolor='black',style='filled')
    start_node = Node(initial_state,None,None,0)
    if start_node.goal_test():
        return start_node.solution()
    q = Queue()
    q.put(start_node)
    explored_states = []
    while not q.empty():
        node = q.get()
        explored_states.append(node.state)
        graph.add_node(node.graph_node)
        children = node.DrawPossibleStates()
        for child in children:
            if not any(np.array_equal(child.state, state) for state in explored_states):
                if child.goal_test():
                    path = [child.state]
                    graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, label=str(child.action)))
                    graph.write_png(f'BFS/solutions{child.depth}.png')
                    while child.parent != None:
                        path.insert(0, child.parent.state)
                        child = child.parent
                    return path
                q.put(child)
                explored_states.append(child.state)
                graph.add_edge(pydot.Edge(node.graph_node, child.graph_node, label=str(child.action)))
                graph.write_png(f'BFS/solutions{child.depth}.png')
    # graph.write_png(f'Final_solution{child.depth}.png')
    return None


initial_state =np.array([[2,8,3], [1,6,4], [7,0,5]])
solution = bfs(initial_state)
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print

