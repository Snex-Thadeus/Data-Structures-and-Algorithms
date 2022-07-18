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


def add_edge(v1, v2, cost): #weighted,unweighted and indirected graph #For unwaighted, remove cost
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        #graph[index2][index1] = cost #For directed graph, remove this


def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present")
    else:
        index1 = nodes.index(v) #Getting the index of the node we want to delete
        node_count = node_count - 1
        nodes.remove(v) #Remove the node from the nodes list
        graph.pop(index1) #Remove the row of the given node
        for i in graph:
            i.pop(index1) #Remove the column


def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        #graph[index2][index1] = 0 #Commented out coz of directed graph


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()

nodes = []#All nodes of the graph
graph = [] #All nodes of a matrix
node_count = 0

print("Before adding nodes")
print(nodes)
print(graph)

add_node("A")
add_node("B")
add_node("D")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print(graph)
delete_edge("A", "C")
print("After adding nodes")
print(graph)

print_graph()