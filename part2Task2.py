class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False



class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = []
        

    def collectPackage(self, pk):
        if (self.location == pk.office) and (len(self.packages) < self.size):
            for i in self.packages:
                if i.id == pk.id:
                    pk.collected = True

            if pk.collected == False:
                self.packages.append(pk)
                pk.collected = True
   
                
            
        
    def deliverOnePackage(self, pk):
        if (self.location == pk.address):
            for i in range(len(self.packages)):
                if self.packages[i].id == pk.id:
                    self.packages.pop(i)
                    pk.delivered = True
                    break

        
    

    def deliverPackages(self):
        for pk in self.packages:
            if (pk.address == self.location):
                pk.delivered = True
                self.packages.pop(self.packages.index(pk))

    

 
    def removePackage(self, pk):
        i = 0
        while i < len(self.packages):
            if self.packages[i].id == pk.id:
                pk.office = self.location
                self.packages.pop(i)
                pk.collected = False
            i += 1
    
            

    def driveTo(self, loc):
        self.location = loc

        

    def getPackagesIds(self):
        packageList = []
        for package in self.packages:
            packageList.append(package.id)
        return packageList

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



"""
deliveryService
"""
def deliveryService(map, truck, packages):
    deliveredTo = {}
    stops = [truck.location]
    office_map = packages_to_office(packages)

    for office, pkgs in office_map.items():
        num_trips = len(pkgs) // truck.size + 1
        if len(pkgs) % truck.size == 0:
            num_trips -= 1
        for trip in range(num_trips):
            if stops[-1] != office:
                shortest = dijkstra(map, truck.location)
                for i in shortest.keys():
                    if i == office:
                        for j in shortest[i][1:]:
                            stops.append(j)
                        truck.driveTo(office)
              
            trip_pkgs = pkgs[trip*truck.size:(trip + 1)*truck.size]
            for p in trip_pkgs:
                truck.collectPackage(p)
            for p in trip_pkgs:
                if stops[-1] != p.address:
                    shortest = dijkstra(map, truck.location)
                    for i in shortest.keys():
                        if i == p.address:
                            for j in shortest[i][1:]:
                                stops.append(j)
                            truck.driveTo(p.address)
            
                truck.deliverOnePackage(p)
                deliveredTo[p.id] = p.address
    return deliveredTo, stops


def packages_to_office(packages):
    m = {}
    for p in packages:
        if p.office not in m:
            m[p.office] = []
        m[p.office].append(p)
    return m





