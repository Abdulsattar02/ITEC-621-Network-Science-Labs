"""
ITEC-621 NETWORK SCIENCE (LAB) — Week 02
Graph Basics: Create, Add/Remove Nodes & Edges
File: lab02_graph_basics.py
"""

# Import required libraries
import networkx as nx   # For creating and working with graphs
import matplotlib.pyplot as plt  # For drawing and displaying the graph

# ----------------------------
# 1) Create an empty graph
# ----------------------------
G = nx.Graph()  # By default, creates an undirected graph
print("Empty Graph created!")

# ----------------------------
# 2) Add nodes to the graph
# ----------------------------
# Add nodes one by one
G.add_node("A")
G.add_node("B")

# Add multiple nodes at once
G.add_nodes_from(["C", "D", "E"])  # Adds nodes C, D, and E

# Display the list of nodes
print("Nodes after adding:", list(G.nodes()))

# ----------------------------
# 3) Add edges (connections between nodes)
# ----------------------------
# Add a single edge between two nodes
G.add_edge("A", "B")  # Connects A with B

# Add multiple edges at once
G.add_edges_from([("A", "C"), ("B", "D"), ("C", "E")])

# Display the list of edges
print("Edges after adding:", list(G.edges()))

# ----------------------------
# 4) Remove a node and an edge
# ----------------------------
# Remove a node (this will also remove its connected edges)
G.remove_node("E")

# Remove a specific edge
G.remove_edge("A", "B")

# Display updated nodes and edges
print("Node E removed. Now nodes:", list(G.nodes()))
print("Edge (A,B) removed. Now edges:", list(G.edges()))

# ----------------------------
# 5) Draw the graph
# ----------------------------
plt.figure(figsize=(7,5))
nx.draw(
    G,
    with_labels=True,        # Show node labels
    node_color="plum",       # Node color
    node_size=1500,          # Node size
    font_size=12,            # Font size of labels
    font_color="black",      # Font color of labels
    edge_color="purple"      # Edge color
)

# Add a title to the graph
plt.title("Graph Basics - Week 02 Lab", color="purple")

# Display the graph
plt.show()
