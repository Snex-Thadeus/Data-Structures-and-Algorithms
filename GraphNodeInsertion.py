#Adjacency Matrix
def add_node(v):
    global node_count
    if v in nodes:
        print(v, "Is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0) #New column
        temp = [] #New row
        for i in range(node_count):
            temp.append(0)
        graph.append(temp) #Append new row to the graph

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()

nodes = []#All nodes of the graph
graph = [] #All nodes of a matrix
node_count = 0

print("Before adding nodes")
print(nodes)
print(graph)

add_node("A")
add_node("B")
print("After adding nodes")
print(nodes)
print(graph)

print_graph()