class Node:
    def __init__(self,value):
        self.value = value

class Graph:
    dict = {}             # key(nodeNameVale): value( Edges) //edges added here are for the ease of the use on BFS and DFS
    keys = []             # Stores the keys for the dictionary
    edge_matrix = []      # 2D list storing the nodes edges
    edge_position = {}    # used to relate the edges to the nodes

    flagged = []
    stack = []
    queue = []


    def add_vertex(self,value):
        Node(value)                                              # Creates the new Vertex
        self.dict[value] = []
        self.keys.append(value)
        for row in self.edge_matrix:                                   # Increases the length of all the previous rows of edges when inserting a new one
            row.append(-1)
        self.edge_matrix.append([-1] * (len(self.edge_matrix) + 1) )    # Adds the new vertex's(edges) with the size of the previous ones
        sth = str(value)
        self.edge_position[sth] = len(self.edge_position)           # Stores the position of the list of edges related to the vertex

    def add_edge(self,vertex_1,vertex_2,):     # Adds the edge connecting the vertex_1 and vertex_2
        self.edge_matrix[self.edge_position[str(vertex_1)]][self.edge_position[str(vertex_2)]] = 1
        self.edge_matrix[self.edge_position[str(vertex_2)]][self.edge_position[str(vertex_1)]] = 1
        self.dict[vertex_1].append(vertex_2)
        self.dict[vertex_2].append(vertex_1)



    def breath_first(self,node = None,count=1,first = False):

        if node == None:                  # If no starting node passed on to the function it starts with the first added
            node = Graph.keys[0]
        if first == False:                # Initialise the starting node
            Graph.flagged.append(node)    # Flag the node as visited
            Graph.queue.insert(0,node)    # Insert it in a queue( First in / Fist out)
            count = 1
            first = True
        node = Graph.queue.pop()          # Pop the current node
        f = open('traversal', 'a+')          # Printing it in a text file
        f.write("BFS: " + str(node) + "\n")
        f.close()
        for edge in Graph.dict[node]:     # For every edge of the current node, flag it
            if edge not in Graph.flagged:
                Graph.flagged.append(edge)
        try:
            Graph.queue.append(Graph.flagged[count])    # Add the next flagged node to the queue
            self.breath_first(node,count+1,first)       # Call the function updating the count which points to the next flagged node to become current node
        except:                                         # Function stops the recursion when a run-time error occurs ( all items iterated - no more flagged nodes to add)
           pass

    def depth_first(self,node=None,first = False):
        if node == None:                               # If the starting node isn't provided take the first one added
            node = Graph.keys[0]
        if first == False:                             # Initialising the first node
            Graph.flagged.append(node)
            Graph.stack.append(node)
            first = True

        count_edge = len(Graph.dict[node]) - 1         # Counts down the visited edges so we now when all of them have been visited
        for edge in Graph.dict[node]:                  # Goes down on every edge of this node
            count_edge -= 1
            if edge not in Graph.flagged:              # If the edge is not visited, mark it as such and add it to the stack. Then recourse the function with it.
                Graph.stack.append(edge)
                Graph.flagged.append(edge)
                self.depth_first(edge,first)
            if count_edge < 0:                         # If the current node has no more edges that haven't been visited, it gets popped and printed.
                a = Graph.stack.pop()
                f = open('traversal', 'a+')
                f.write("DFS : " + str(a) + "\n")
                f.close()




if __name__ == '__main__':
    G = Graph()
    G.add_vertex(1)
    G.add_vertex(2)
    G.add_vertex(3)
    G.add_vertex(4)
    G.add_vertex(5)
    G.add_vertex(6)
    G.add_vertex(7)
    G.add_vertex(8)
    G.add_vertex(9)
    G.add_vertex(10)

    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(4, 7)
    G.add_edge(5, 8)
    G.add_edge(6, 8)
    G.add_edge(7, 8)
    G.add_edge(9, 8)
    G.add_edge(10, 9)



    G.breath_first()
    #G.depth_first()





