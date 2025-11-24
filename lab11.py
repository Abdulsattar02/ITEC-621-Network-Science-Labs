# --------------------------------------------------------------
# Lab 11: Bipartite Network – Authors & Papers
# Topic: Author–Paper graph and author projection
# --------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

# -------------------------
# 1) Initialize empty graph
# -------------------------
B = nx.Graph()

# -------------------------
# 2) Define node sets
# -------------------------
authors = ["A1", "A2", "A3"]
papers = ["P1", "P2"]

# -------------------------
# 3) Add nodes with bipartite attribute
# -------------------------
B.add_nodes_from(authors, bipartite=0)  # 0 → authors
B.add_nodes_from(papers, bipartite=1)   # 1 → papers

# -------------------------
# 4) Add edges (who wrote which paper)
# -------------------------
edges = [
    ("A1", "P1"),
    ("A2", "P1"),
    ("A2", "P2"),
    ("A3", "P2")
]
B.add_edges_from(edges)

# -------------------------
# 5) Draw the bipartite network
# -------------------------
pos = nx.bipartite_layout(B, authors)  # separate authors and papers
plt.figure(figsize=(6, 4))
nx.draw(B, pos, with_labels=True, node_color='skyblue', font_size=10)
plt.title("Author–Paper Bipartite Network")
plt.show()

# -------------------------
# 6) Project bipartite graph to author network
# -------------------------
author_network = nx.bipartite.projected_graph(B, authors)
plt.figure(figsize=(6, 4))
nx.draw(author_network, with_labels=True, node_color='lightgreen', font_size=10)
plt.title("Author Network (Co-Authorship)")
plt.show()
