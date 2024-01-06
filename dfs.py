from main_dfs import Node
import numpy as np
import pydot

def dfs(initial_state):
    graph = pydot.Dot(graph_type='digraph',fontsize='20',fontcolor='black',style='filled')
    start_node = Node(initial_state,None,None,0)
    if start_node.goal_test():
        start_node.solution()
    stack = [start_node]
    explored_states = []
    while stack:
        current_node = stack.pop()
        explored_states.append(current_node.state)
        graph.add_node(current_node.graph_node)
        Children = current_node.DrawPossibleStates()
        for child in Children:
            if not any(np.array_equal(child.state, state) for state in explored_states):
                if child.goal_test():
                    path = [child.state]
                    graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, label=str(child.action)))
                    graph.write_png(f'DFS_Image/solutions{child.depth}.png')
                    while child.parent != None:
                        path.insert(0, child.parent.state)
                        child = child.parent
                    return path
                stack.append(child)
                explored_states.append(child.state)
                graph.add_edge(pydot.Edge(current_node.graph_node, child.graph_node, label=str(child.action)))
                graph.write_png(f'DFS_Image/solutions{child.depth}.png')

    return None

initial_state = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
solution = dfs(initial_state)
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print



