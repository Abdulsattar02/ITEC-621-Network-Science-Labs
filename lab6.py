"""
Week 06 Lab — Random Graphs (Erdős–Rényi) and Degree Distribution

Place this file in:
ITEC-621-NETWORK-SCIENCE-LAB/lab06.py

Dependencies:
pip install networkx matplotlib numpy

What it does:
- Builds an ER random graph G(n, p)
- Computes degree sequence and degree PDF
- Plots PDF (linear) and CCDF on log-log axes
- Saves plots to files and prints a small summary

Author: Instructor-friendly version (for students)
"""

import collections
import sys
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# -------------------------------
# Build ER Graph
# -------------------------------
def build_er_graph(n, p, seed=42):
    """
    Build an Erdős–Rényi random graph G(n, p).
    :param n: number of nodes
    :param p: probability for edge creation
    :param seed: random seed for reproducibility
    :return: networkx.Graph
    """
    G = nx.erdos_renyi_graph(n=n, p=p, seed=seed)
    return G

# -------------------------------
# Degree Sequence
# -------------------------------
def degree_sequence(G):
    """Return degree sequence as a numpy array."""
    return np.array([d for _, d in G.degree()])

# -------------------------------
# PDF from Degrees
# -------------------------------
def pdf_from_degrees(deg_array):
    """
    Compute PDF (probability mass function) of degrees.
    Returns sorted degree values (ks) and corresponding pdf values.
    """
    counts = collections.Counter(deg_array)
    ks = np.array(sorted(counts.keys()))
    freqs = np.array([counts[k] for k in ks], dtype=float)
    pdf = freqs / freqs.sum()
    return ks, pdf

# -------------------------------
# CCDF from PDF
# -------------------------------
def ccdf_from_pdf(pdf):
    """
    Compute CCDF P(K >= k) from pdf (ks assumed sorted ascending).
    Returns ccdf aligned with ks.
    """
    rev_cumsum = np.cumsum(pdf[::-1])[::-1]
    return rev_cumsum

# -------------------------------
# Plot PDF
# -------------------------------
def plot_pdf(ks, pdf, title='Degree Distribution (PDF)', filename='degree_pdf.png'):
    """Plot PDF on linear axes and save to file."""
    plt.figure(figsize=(8, 4.5))
    plt.bar(ks, pdf, width=0.8, align='center', edgecolor='black', alpha=0.8)
    plt.xlabel('Degree k')
    plt.ylabel('P(k)')
    plt.title(title)
    plt.grid(alpha=0.25, axis='y')
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    print(f'[INFO] Saved PDF plot to: {filename}')
    plt.show()

# -------------------------------
# Plot CCDF log-log
# -------------------------------
def plot_ccdf_loglog(ks, ccdf, title='Degree CCDF (log-log)', filename='degree_ccdf_loglog.png'):
    """
    Plot CCDF on log-log axes and save to file.
    Skip deg==0 entries to avoid log(0).
    """
    mask = (ks > 0) & (ccdf > 0)
    if mask.sum() < 2:
        print('[WARN] Not enough points for log-log CCDF plot. Skipping.')
        return
    plt.figure(figsize=(8, 4.5))
    plt.loglog(ks[mask], ccdf[mask], marker='o', linestyle='-')
    plt.xlabel('Degree k (log scale)')
    plt.ylabel('P(K ≥ k) (log scale)')
    plt.title(title)
    plt.grid(which='both', alpha=0.25)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    print(f'[INFO] Saved CCDF (log-log) plot to: {filename}')
    plt.show()

# -------------------------------
# Summary Stats
# -------------------------------
def summary_stats(G, deg_array):
    """Print basic numeric summaries to the console."""
    n = G.number_of_nodes()
    m = G.number_of_edges()
    mean_deg = float(np.mean(deg_array)) if deg_array.size else 0.0
    median_deg = float(np.median(deg_array)) if deg_array.size else 0.0
    max_deg = int(np.max(deg_array)) if deg_array.size else 0
    print('--- Graph Summary ---')
    print(f'Nodes (n): {n}')
    print(f'Edges (m): {m}')
    print(f'Average degree: {mean_deg:.3f}')
    print(f'Median degree: {median_deg:.1f}')
    print(f'Max degree: {max_deg}')
    print('---------------------')

# -------------------------------
# Main Function
# -------------------------------
def main():
    # Parameters (students may change these)
    n = 1000           # number of nodes
    avg_degree = 6     # approximate desired average degree
    p = avg_degree / (n - 1)  # edge probability for ER G(n, p)
    seed = 42

    print('Lab 06 — ER random graphs & degree distribution')
    print(f'Building G(n={n}, p={p:.5f}) ...')

    # Build graph
    G = build_er_graph(n=n, p=p, seed=seed)

    # Compute degrees
    deg = degree_sequence(G)

    # Print summary stats
    summary_stats(G, deg)

    # Compute PDF and CCDF
    ks, pdf = pdf_from_degrees(deg)
    ccdf = ccdf_from_pdf(pdf)

    # Plot PDF (linear)
    plot_pdf(ks, pdf, title=f'Degree Distribution (PDF) — ER G(n={n}, p={p:.4f})', filename='degree_pdf.png')

    # Plot CCDF on log-log
    plot_ccdf_loglog(ks, ccdf, title=f'Degree CCDF (log-log) — ER G(n={n}, p={p:.4f})', filename='degree_ccdf_loglog.png')

    # Print small table for first few degree values
    counts = collections.Counter(deg)
    print('\nDegree Count P(k)')
    for k in ks[:12]:
        print(f'{int(k):6d} {int(counts[k]):5d} {pdf[ks.tolist().index(k)]:6.4f}')

    print('\nDone. Plots saved and displayed. Try changing n and avg_degree to experiment.')

# -------------------------------
# Run Main
# -------------------------------
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error while running lab06.py:', e)
        sys.exit(1)
