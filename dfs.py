def dfs_traversal(graph,node,visited=None,path=None):
    if visited is None:
        visited=set()
    if path is None:
        path=[]
    visited.add(node)
    path.append(node)
    print(f" Visited:{node}")
    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs_traversal(graph,neighbor,visited,path)
    return path

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
print("-----DFS------")
traversal_path=dfs_traversal(NETWORK_GRAPH,Start_node)
print(f"traversal completed: {'->' .join(traversal_path)}")
