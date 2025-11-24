# ---------------------------------------------------------------
# lab09.py
# Scale-Free Networks (Barabási–Albert Model)
# ITEC-621 NETWORK SCIENCE LAB – WEEK 09
# ---------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create BA Scale-Free Graph
# -----------------------------
n = 50  # Total nodes
m = 2   # Each new node connects to 2 existing nodes

# Create Scale-Free graph using BA model
G = nx.barabasi_albert_graph(n, m)

# -----------------------------
# Step 2: Print Graph Information
# -----------------------------
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Get degree of every node
degrees = [deg for (node, deg) in G.degree()]

# -----------------------------
# Step 3: Plot the Scale-Free Network
# -----------------------------
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Stable layout
nx.draw(
    G,
    pos,
    node_size=80,
    node_color="orange",
    edge_color="gray",
    with_labels=False
)
plt.title("Scale-Free Network (Barabási–Albert Model)")
plt.show()

# -----------------------------
# Step 4: Plot Degree Distribution (Power-Law Pattern)
# -----------------------------
plt.figure(figsize=(8, 5))

# Count how many nodes have each degree
degree_count = {}
for d in degrees:
    degree_count[d] = degree_count.get(d, 0) + 1

# Plot degree distribution
plt.bar(degree_count.keys(), degree_count.values(), color="skyblue")
plt.xlabel("Node Degree")
plt.ylabel("Number of Nodes")
plt.title("Degree Distribution of Scale-Free Network")
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()
