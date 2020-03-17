
from util import Queue, Stack
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
    def dfs(self,starting_vertex,target):
        #create a stack
        s = Stack()

        #push a path to the stack!
        s.push([starting_vertex])

        #create a set of visited values
        visited = set()

        #while there are values in the stack to process
        while s.size() > 0:
            #pop the first value
            path = s.pop()
            #grab the final value in the list
            vertex = path[-1]
            #if that value has not been visited
            if vertex not in visited:
                #if it is our target, return the answer!
                if vertex == target:
                    return path
                #if not, continue the process, add the new vertex to the visited set
                visited.add(vertex)
                #Then search for neighbors of the new vertex found
                for neighbor in self.vertices[vertex]:
                    #create a new route with the neighboring node at the end.
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex,visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the vertex has been visited
        # If not...
        if visited == None:
            visited = []
        
        visited.append(starting_vertex)
        #for each neighbor that a starting vertex has
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor,visited)
        return visited
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # Check if it's been visited
            if vertex not in visited:
            # If it hasn't been visited...
                # Mark it as visited
                visited.add(vertex)
                # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.vertices[vertex]:
                    # MAKE A COPY OF THE PATH
                    new_path = list(path)
                    # ENQUEUE THE COPY
                    new_path.append(neighbor)
                    q.enqueue(new_path)
    def dfs_recursive(self,starting_vertex,target, visited=None):
        # if visited == None:
        #     visited = []
        
        # visited.append([starting_vertex])
        # for neighbor in self.verticies[starting_vertex]:
        #     if neighbor not in visited:
        #         if neighbor == target:
        #             return



    def dft_recursive(self, starting_vertex,visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the vertex has been visited
        # If not...
        if visited == None:
            visited = []
        
        visited.append(starting_vertex)
        #for each neighbor that a starting vertex has
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor,visited)
        return visited