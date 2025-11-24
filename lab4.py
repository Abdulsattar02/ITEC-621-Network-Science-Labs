"""
ITEC-621 NETWORK SCIENCE (LAB) — LAB 04
Network Measures I: Degree, Paths, Connectivity
File: lab04.py
"""

import networkx as nx
import matplotlib.pyplot as plt

# ------------------------------
# Part 1: Create Graph
# ------------------------------
G = nx.Graph()

edges = [("A", "B"), ("A", "C"), ("B", "C"),
         ("C", "D"), ("D", "E"), ("E", "F")]
G.add_edges_from(edges)

print("Nodes:", G.nodes())
print("Edges:", G.edges())

# Visualize graph
plt.figure(figsize=(7,5))
nx.draw(G, with_labels=True, node_color="lightblue",
        node_size=1200, edge_color="purple", font_size=12)
plt.title("Network Measures - Degree, Paths, Connectivity")
plt.show()

# ------------------------------
# Part 2: Degree
# ------------------------------
print("\n--- Degree of Each Node ---")
for node, deg in G.degree():
    print(f"{node}: degree = {deg}")

# ------------------------------
# Part 3: Paths
# ------------------------------
print("\n--- Shortest Path Examples ---")
print("Shortest path A -> E:", nx.shortest_path(G, "A", "E"))
print("Path length A -> E:", nx.shortest_path_length(G, "A", "E"))
print("Shortest path B -> F:", nx.shortest_path(G, "B", "F"))
print("Path length B -> F:", nx.shortest_path_length(G, "B", "F"))

# ------------------------------
# Part 4: Connectivity
# ------------------------------
print("\n--- Connectivity ---")
print("Is graph connected?", nx.is_connected(G))
print("Number of connected components:", nx.number_connected_components(G))
print("\nConnected Components:")
for component in nx.connected_components(G):
    print(component)
