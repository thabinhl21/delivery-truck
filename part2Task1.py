class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item) -> object:
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)

"""
BFS
"""

def bfs(map, office):
    visited = []
    q = Queue()
    q.enqueue(office)
    parent = {}

    while not q.isEmpty():
        neighbors = []
        node = q.dequeue()

        for neighbor in map:
            if neighbor[0] == node and neighbor[1] not in visited:
                parent[neighbor[1]] = neighbor[0]
                visited.append(neighbor[1])
                neighbors.append(neighbor[1])
            
            if neighbor[1] == node and neighbor[0] not in visited:
                parent[neighbor[0]] = neighbor[1]
                visited.append(neighbor[0])
                neighbors.append(neighbor[0])
        neighbors.sort()
        for neighbor in neighbors:
            q.enqueue(neighbor)

    parent[office] = None

    def createPaths(parent, office):
        path = {}
        for name in parent:
            path[name] = [office]
        queue = Queue()
        queue.enqueue(office)
        while not queue.isEmpty():
            front = queue.dequeue()
            for name in parent:
                if parent[name] == front:
                    parent_name = parent[name]
                    parent_path = path[parent_name].copy()
                    parent_path.append(name)
                    path[name] = parent_path
                    queue.enqueue(name)
        return path
    return createPaths(parent,office)



"""
DFS
"""
def dfs(map, office):
    visited = []
    s = Stack()
    s.push(office)
    parent = {}

    while not s.isEmpty():
        
        neighbors = []
        node = s.pop()
        if node not in visited:
            visited.append(node)
        
            for neighbor in map:
            
                if neighbor[0] == node and neighbor[1] not in visited:
                    parent[neighbor[1]] = neighbor[0]
                    neighbors.append(neighbor[1])
            
                if neighbor[1] == node and neighbor[0] not in visited:
                    parent[neighbor[0]] = neighbor[1]
                    neighbors.append(neighbor[0])

            neighbors.sort()
            for neighbor in neighbors:
                s.push(neighbor)
    parent[office] = None

    def createPaths(parent, office):
        path = {}
        for name in parent:
            path[name] = [office]
        stack = Stack()
        stack.push(office)
        while not stack.isEmpty():
            front = stack.pop()
            for name in parent:
                if parent[name] == front:
                    parent_name = parent[name]
                    parent_path = path[parent_name].copy()
                    parent_path.append(name)
                    path[name] = parent_path
                    stack.push(name)
        return path
    return createPaths(parent,office)



"""
Dijkstra's
"""
def dijkstra(map, office):
    graph = []
    names = {}
    dest_count = 0
    for edge in map:
        if edge[0] not in names:
            names[edge[0]] = dest_count
            dest_count += 1
        if edge[1] not in names:
            names[edge[1]] = dest_count
            dest_count += 1
    distance = [float('inf')]*len(names)
    parents = [None]*len(names)
    for i in range(len(names)):
        graph.append([-1]*len(names))
    for edge in map:
        dest_num = names[edge[1]]
        source_num = names[edge[0]]
        graph[source_num][dest_num] = edge[2]
        graph[dest_num][source_num] = edge[2]
    post_number = names[office]
    distance[post_number] = -1
    for i in range(len(names)):
        if graph[post_number][i] != -1:
            distance[i] = graph[post_number][i]
            parents[i] = post_number
    finished = [False]*len(names)
    finished[post_number] = True
    while False in finished:
        shortest_dist = float('inf')
        shortest_index = 0
        for i in range(len(distance)):
            if finished[i] == False and distance[i] < shortest_dist:
                shortest_dist = distance[i]
                shortest_index = i
        for i in range(len(names)):
            if graph[shortest_index][i] != -1:
                if graph[shortest_index][i] + shortest_dist < distance[i]:
                    distance[i] = graph[shortest_index][i] + shortest_dist
                    parents[i] = shortest_index
        finished[shortest_index] = True
    num_to_names = {}
    for name in names:
        num_to_names[names[name]] = name
    def createPaths(parents, post_number, num_to_names):
        path = {}
        for i in range(len(parents)):
            name = num_to_names[i]
            path[name] = [num_to_names[post_number]]
        queue = Queue()
        queue.enqueue(post_number)
        while not queue.isEmpty():
            front = queue.dequeue()
            for i in range(len(parents)):
                if parents[i] == front:
                    parent_name = num_to_names[parents[i]]
                    parent_path = path[parent_name].copy()
                    parent_path.append(num_to_names[i])
                    path[num_to_names[i]] = parent_path
                    queue.enqueue(i)
        return path
    return createPaths(parents,post_number,num_to_names)


