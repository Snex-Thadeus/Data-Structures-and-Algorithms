#Adjacency List
#Key represnts the nodes of the graph
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = [] #Adding v to the graph


def add_edge(v1, v2, cost): #Remove cost if you want directed, unweighted graph
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        list1 = [v2, cost] #For weighted graph
        #list2 = [v1, cost]
        graph[v1].append(list1)
        #graph[v2].append(list2) #Enable for undirected and unweghted graph replace list2 with v1


def delete_node(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v) #Delete key-value pair of v from the graph
        for i in graph:
            list1 = graph[i] #Value of every key
            #For weighted graph and undirected
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break
                    #For unweighted graph
            # if v in list1:
            #     list1.remove(v)


def delete_edge(v1, v2, cost): #Remove cost if you want undirected, unweighted graph
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        temp = [v1, cost] #For weighted & undirected graph
        temp1 = [v2, cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)
            #-------------------------------
        if v2 in graph[v1]: #Check if v2 is the value of v1
            graph[v1].remove(v2) #This works for undirected unweighted graph
            graph[v2].remove(v1) #Disable this for directed graph


def DFS(node, visited, graph):
    if node not in graph:
        print(node, "is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]: #List of adjacent value of key
            DFS(i, visited, graph) #Visiting every node recursively


def DFSiterative(node, graph):
    visited = set()
    if node not in graph:
        print(node, "is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)




visited = set()
graph = {}
add_node("A")
add_node("B")

add_edge("A", "B", 10)
delete_node("A")

print(graph)