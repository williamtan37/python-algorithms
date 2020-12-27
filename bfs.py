graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

from collections import deque
visited = set() 
queue = deque()

def bfs(visited, graph, node):
  visited.add(node)
  queue.append(node)

  while queue:
    s = queue.popleft() 
    print(s, end=" ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')


#https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python