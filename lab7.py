# ---------------------------------------------------------------
# lab07.py
# Small-World Networks (Watts–Strogatz Model)
# ITEC-621 NETWORK SCIENCE LAB – WEEK 07
# ---------------------------------------------------------------

import networkx as nx          # For graph creation
import matplotlib.pyplot as plt # For visualization

# -----------------------------
# Step 1: Create WS Small-World Graph
# -----------------------------
n = 30    # Number of nodes
k = 4     # Each node connected to its 4 nearest neighbors
p = 0.3   # Rewiring probability (0 = regular, 1 = random)

# Create the Watts–Strogatz graph
G = nx.watts_strogatz_graph(n, k, p)

# -----------------------------
# Step 2: Print Graph Information
# -----------------------------
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average Clustering Coefficient:", nx.average_clustering(G))

# -----------------------------
# Step 3: Plot the Small-World Graph
# -----------------------------
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # spring Layout for better visualization
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    node_color="skyblue",
    font_size=8,
    edge_color="gray"
)
plt.title("Small-World Network (Watts–Strogatz Model)")
plt.show()
