"""
ITEC-621 NETWORK SCIENCE (LAB) — Week 01
Simple Triangle Graph
File: lab01_graph.py
"""

import networkx as nx
import matplotlib.pyplot as plt

# ----------------------------
# 1) Create a simple triangle graph
# ----------------------------
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# ----------------------------
# 2) Draw the graph
# ----------------------------
plt.figure(figsize=(5,5))
nx.draw(
    G,
    with_labels=True,    # Show node labels
    node_color="lightgreen",
    node_size=1000,
    font_size=12,
    edge_color="blue",
    width=2
)
plt.title("Triangle Graph", color="darkgreen")
plt.show()
