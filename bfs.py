#undirected graph, so an edge is stored twice
graph = {
  'A' : ['B','C','6'],
  'B' : ['A', 'D', 'E'],
  'C' : ['A','F'],
  'D' : ['B'],
  'E' : ['B','F'],
  'F' : ['C','E','9'],
  '6' : ['A','7','8'],
  '7' : ['6'],
  '8' : ['6'],
  '9' : ['F'],
}

from collections import deque
visited = set() 
queue = deque()

'''
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
'''

#this dfs example shows what backtracking means
def dfs(visited, graph, node):
  visited.add(node)
  print(node)

  for neighbour in graph[node]:
    if neighbour not in visited:
      dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')
#https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python