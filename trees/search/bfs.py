graph={   'Amin'  : {'Wasim', 'Nick', 'Mike'},
         'Wasim' : {'Imran', 'Amin'}, 
         'Imran' : {'Wasim','Faras'}, 
         'Faras' : {'Imran'},
         'Mike':{'Amin'}, 
         'Nick':{'Amin'}}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbors in neighbors:
                queue.append(neighbors)
    return visited


print(bfs(graph,'Amin'))