"""
ITEC-621 NETWORK SCIENCE (LAB) — LAB 03
Bridges of Königsberg & Graph Representations
File: lab03.py
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# Part 1: Bridges of Königsberg
# ------------------------------

# Graph with 4 land areas: A, B, C, D
# Bridges connect them (multi-edges)
G = nx.MultiGraph()
edges = [
    ("A", "B"), ("A", "B"),  # two bridges
    ("A", "C"),
    ("A", "D"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D")
]
G.add_edges_from(edges)

print("Nodes:", G.nodes())
print("Edges:", G.edges())

# Eulerian check
print("Eulerian Circuit exists?", nx.is_eulerian(G))
print("Eulerian Path exists?", nx.has_eulerian_path(G))

# Visualize graph
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(7,5))
nx.draw(G, pos, with_labels=True, node_color="lightblue",
        node_size=1500, edge_color="purple", font_size=12)
plt.title("Bridges of Königsberg")
plt.show()

# ------------------------------
# Part 2: Adjacency List
# ------------------------------
print("\nAdjacency List:")
for node in G.nodes():
    print(node, "->", list(G.neighbors(node)))

# ------------------------------
# Part 3: Adjacency Matrix
# ------------------------------

# Convert to simple graph (no multiple edges) for matrix
simple_G = nx.Graph(G)
matrix = nx.to_numpy_array(simple_G, nodelist=sorted(simple_G.nodes()))

print("\nAdjacency Matrix:\n", matrix)

# Display matrix with labels
print(" ", " ".join(sorted(simple_G.nodes())))
for i, row in enumerate(matrix.astype(int)):
    print(sorted(simple_G.nodes())[i], row)
