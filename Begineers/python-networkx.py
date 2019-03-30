'''
Install below Python Module before You run this code.
>>> pip install networkx --upgrade 

# https://networkx.github.io/
'''

import networkx as nx
print("\n *** NetworkX - Graph Optimization *** \n")

G = nx.Graph() # creating a graph
G.add_node(1) # can add single node
G.add_nodes_from([2,3,4]) # can add list of nodes
H = nx.path_graph(10) # add any iterable container of nodes.
G.add_nodes_from(H)
G.add_node('spam') # adds node 'spam'
G.add_nodes_from('spam') # add 4 nodes like 's', 'p', 'a', 'm'
print(f" Nodes are {list(G.nodes)}") # list nodes in the network

G.add_edge(1, 2) # edges between 1 and 2
e = (2, 3) # edges between 2 and 3
G.add_edge(*e)  #  unpack edge tuple
G.add_edges_from([(2,4), (4,5), (0,9)]) # can add list of edges,
print(f" Edges are {list(G.edges)}")

print(f"\n Node 2 connected with {list(G.adj[2])}")
print(f" Total nodes connected with Node2 : {G.degree[2]}")

print(f"\n Total Nodes : {G.number_of_nodes()}")
print(f" Total Edges : {G.number_of_edges()}" )

