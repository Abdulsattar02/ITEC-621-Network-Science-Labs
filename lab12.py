# --------------------------------------------------------------
# Lab 12: Social Network Visualization & Community Detection
# --------------------------------------------------------------

import csv
import os
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

# -----------------------
# Parameters / file name
# -----------------------
CSV_FILE = "friendship.csv"

# -----------------------
# 1) Create a sample dataset if file doesn't exist
# -----------------------
if not os.path.exists(CSV_FILE):
    print(f"[INFO] '{CSV_FILE}' not found. Creating a small sample network.")
    sample_edges = [
        ("Alice", "Bob"),
        ("Alice", "Carol"),
        ("Bob", "Carol"),
        ("Carol", "David"),
        ("Eve", "Frank"),
        ("Eve", "Grace"),
        ("Frank", "Grace"),
        ("Grace", "Heidi"),
        ("Isaac", "Jack"),
        ("Isaac", "Ken"),
        ("Jack", "Ken"),
        ("Ken", "Liam"),
        # Some cross-group links
        ("Carol", "Eve"),
        ("Grace", "Isaac"),
    ]
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["source", "target"])
        writer.writerows(sample_edges)
    print(f"[INFO] Sample '{CSV_FILE}' created with {len(sample_edges)} edges.\n")
else:
    print(f"[INFO] Found '{CSV_FILE}'. Using existing dataset.\n")

# -----------------------
# 2) Load edges and build graph
# -----------------------
G = nx.Graph()
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        src = row.get("source") or row.get("Source") or row.get("from") or row.get("u")
        tgt = row.get("target") or row.get("Target") or row.get("to") or row.get("v")
        if src is None or tgt is None:
            vals = list(row.values())
            if len(vals) >= 2:
                src, tgt = vals[0], vals[1]
            else:
                continue
        src, tgt = src.strip(), tgt.strip()
        if src and tgt:
            G.add_edge(src, tgt)

print(f"[INFO] Graph ready: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.\n")

# -----------------------
# 3) Detect communities
# -----------------------
if G.number_of_nodes() == 0:
    print("[ERROR] Graph is empty! Check the CSV file.")
    raise SystemExit(1)

communities = list(community.greedy_modularity_communities(G))
print(f"[INFO] Found {len(communities)} communities.")
for i, comm in enumerate(communities, start=1):
    print(f" Community {i}: {sorted(comm)}")

# Map each node to its community index
node_group = {}
for idx, comm in enumerate(communities):
    for node in comm:
        node_group[node] = idx

# -----------------------
# 4) Visualization
# -----------------------
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
    "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"
]

node_colors = [colors[node_group[n] % len(colors)] for n in G.nodes()]
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700, alpha=0.9)
nx.draw_networkx_edges(G, pos, alpha=0.6)
nx.draw_networkx_labels(G, pos, font_size=10)
plt.title("Friendship Network — Nodes colored by group")
plt.axis("off")
plt.tight_layout()
plt.show()

# -----------------------
# 5) Note
# -----------------------
print("\n[NOTE] You can edit 'friendship.csv' to add more people or links and rerun the script.")
