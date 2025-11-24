from collections import deque
def bfs_shortest(graph,start_node,end_node):
    queue=deque([[start_node]])
    visited={start_node}
    while queue:
        path=queue.popleft()
        current_node=path[-1]
        if current_node==end_node:
            return path
        for neighbor in graph.get(current_node,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path=list(path)
                new_path.append(neighbor)
                queue.append(new_path)
        return None

NETWORK_GRAPH = {
    'A':['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': ['D'],  
    'E': ['F','H'],
    'F':['I'],
    'G':[],
    'H':['I'],
    'I':['J'],
    'J':[]
}
Start_node='A'
target='I'
shortest=bfs_shortest(NETWORK_GRAPH,Start_node,target)
if shortest:
    print(f"path: {'->'.join(shortest)}")
else:
    print(f'Target {target} unreachable')


