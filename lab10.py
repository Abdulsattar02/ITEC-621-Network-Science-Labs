# Week 10 - Evolving Networks: Growth & Preferential Attachment
# This file:
# - Builds a small evolving network using a manual preferential-attachment routine.
# - Generates a NetworkX Barabasi–Albert (BA) graph for comparison.
# - Visualizes a final network and plots degree histograms.
# - Saves plots to files and shows them.
# Dependencies:
# pip install networkx matplotlib numpy

import random
import collections
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def manual_preferential_attachment(n_total=100, m0=3, m=2, seed=42):
    """
    Build a network manually using preferential attachment.

    Parameters:
    n_total : int - final number of nodes (>= m0)
    m0 : int - initial fully connected seed nodes
    m : int - number of edges each new node will create
    seed : int - random seed
    """
    if m0 < 1 or m < 1:
        raise ValueError("m0 and m must be >= 1")
    if m > m0:
        raise ValueError("m must be <= m0 (initial seed node count)")

    random.seed(seed)
    np.random.seed(seed)

    G = nx.Graph()

    # Create initial m0 fully-connected seed nodes
    for i in range(m0):
        G.add_node(i)
    for u in range(m0):
        for v in range(u + 1, m0):
            G.add_edge(u, v)

    # Add new nodes one-by-one
    for new_node in range(m0, n_total):
        G.add_node(new_node)

        existing_nodes = list(G.nodes())
        degrees = np.array([G.degree(n) for n in existing_nodes], dtype=float)

        if degrees.sum() == 0:
            probs = np.ones_like(degrees) / len(degrees)
        else:
            probs = degrees / degrees.sum()

        chosen = np.random.choice(existing_nodes, size=m, replace=False, p=probs)

        for target in chosen:
            G.add_edge(new_node, int(target))

    return G


def plot_graph(G, title="Graph (manual PA)", filename="pa_graph.png"):
    """Visualize a graph using spring layout."""
    plt.figure(figsize=(8, 6))

    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=80, node_color="skyblue")
    nx.draw_networkx_edges(G, pos, alpha=0.6)
    nx.draw_networkx_labels(G, pos, font_size=8)

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    print(f"[INFO] Saved graph visualization to {filename}")
    plt.show()


def plot_degree_histogram(G_manual, G_ba=None, filename="degree_hist.png"):
    """Plot degree histograms for manual PA graph and optional BA model."""
    degs_manual = [d for _, d in G_manual.degree()]
    plt.figure(figsize=(10, 4))

    # Manual PA histogram
    plt.subplot(1, 2, 1)
    counts_manual = collections.Counter(degs_manual)
    ks_manual = sorted(counts_manual.keys())
    vals_manual = [counts_manual[k] for k in ks_manual]
    plt.bar(ks_manual, vals_manual, alpha=0.7)
    plt.xlabel("Degree (k)")
    plt.ylabel("Count")
    plt.title("Degree Histogram - Manual PA")

    # BA histogram
    if G_ba is not None:
        degs_ba = [d for _, d in G_ba.degree()]
        counts_ba = collections.Counter(degs_ba)
        ks_ba = sorted(counts_ba.keys())
        vals_ba = [counts_ba[k] for k in ks_ba]

        plt.subplot(1, 2, 2)
        plt.bar(ks_ba, vals_ba, alpha=0.7, color="orange")
        plt.xlabel("Degree (k)")
        plt.ylabel("Count")
        plt.title("Degree Histogram - BA Model")

    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    print(f"[INFO] Saved degree histogram to {filename}")
    plt.show()


def summary_stats(G, label="Graph"):
    """Print summary statistics."""
    n = G.number_of_nodes()
    m = G.number_of_edges()
    degrees = [d for _, d in G.degree()]
    avg_deg = np.mean(degrees) if degrees else 0
    max_deg = max(degrees) if degrees else 0

    print(f"--- {label} Summary ---")
    print(f"Nodes: {n}, Edges: {m}, Avg Degree: {avg_deg:.3f}, Max Degree: {max_deg}")
    print("-----------------------")


def main():
    n_total = 200
    m0 = 3
    m = 2
    seed = 42

    print("Lab 10 - Evolving Networks: Growth & Preferential Attachment")
    print(f"Building manual PA graph with n={n_total}, m0={m0}, m={m}, seed={seed} ...")

    G_manual = manual_preferential_attachment(n_total=n_total, m0=m0, m=m, seed=seed)
    summary_stats(G_manual, label="Manual PA Graph")

    print("Building NetworkX BA graph for comparison ...")
    G_ba = nx.barabasi_albert_graph(n=n_total, m=m, seed=seed)
    summary_stats(G_ba, label="NetworkX BA Graph")

    plot_graph(G_manual, title="Manual Preferential Attachment Graph", filename="pa_graph.png")

    plot_degree_histogram(G_manual, G_ba, filename="degree_hist.png")

    print("\nExperiment ideas:")
    print(" - Increase n_total to see smoother degree distribution.")
    print(" - Increase m to increase average degree.")
    print(" - Try different random seeds.")
    print(" - Remove random edges and see how hubs change.")


if __name__ == "__main__":
    main()
