# ==========================================
# Week 05 — Network Measures II: Clustering & Centrality
# Run: python lab05.py
# Requirements: networkx, matplotlib
# ==========================================

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

# -------------------------------
# 1. Build Example Graphs
# -------------------------------
def build_graphs():
    """
    Build example graphs:
    - G: small custom graph easy to inspect
    - K: Zachary's karate club (built-in NetworkX)
    """
    G = nx.Graph()
    G.add_edges_from([
        ('A', 'B'), ('A', 'C'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'D'),
        ('D', 'F'), ('E', 'F')
    ])
    K = nx.karate_club_graph()  # undirected
    return G, K

# -------------------------------
# 2. Compute Measures
# -------------------------------
def compute_measures(G, K):
    """
    Compute clustering and centrality measures.
    Returns dictionaries and top-5 betweenness list.
    """

    # Clustering for small graph G
    local_clust = nx.clustering(G)  # local clustering per node
    avg_clust = nx.average_clustering(G)  # average clustering
    trans = nx.transitivity(G)  # transitivity (global)
    print('\n--- Clustering (small graph G) ---')
    print('Local clustering:', local_clust)
    print('Average clustering:', round(avg_clust, 4))
    print('Transitivity (global):', round(trans, 4))

    # Centrality measures for karate graph K
    deg_cent = nx.degree_centrality(K)
    close_cent = nx.closeness_centrality(K)
    between_cent = nx.betweenness_centrality(K)
    
    # Eigenvector centrality may fail; handle convergence
    try:
        eig_cent = nx.eigenvector_centrality(K, max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        eig_cent = {n: 0.0 for n in K.nodes()}
        print("Warning: eigenvector centrality did not converge; using zeros as fallback.")

    # Top 5 nodes by betweenness
    top_bw = sorted(between_cent.items(), key=itemgetter(1), reverse=True)[:5]
    print('\n--- Centrality (karate club example) ---')
    print('Top 5 nodes by betweenness:', top_bw)

    return {
        'local_clust': local_clust,
        'avg_clust': avg_clust,
        'transitivity': trans,
        'deg_cent': deg_cent,
        'close_cent': close_cent,
        'between_cent': between_cent,
        'eig_cent': eig_cent,
        'top_bw': top_bw
    }

# -------------------------------
# 3. Draw Graph with Metric
# -------------------------------
def draw_graph_with_metric(G1, metric, title, cmap='viridis', size_multiplier=2000):
    """
    Draw graph G1 with node color/size representing `metric` values (dict node->value).
    """
    nodes_list = list(G1.nodes())
    values = [metric.get(n, 0.0) for n in nodes_list]

    pos = nx.spring_layout(G1, seed=42)  # reproducible positions

    minv, maxv = min(values), max(values)
    if maxv - minv == 0:
        sizes = [300 for _ in values]
    else:
        sizes = [300 + (v - minv) / (maxv - minv) * size_multiplier for v in values]

    plt.figure(figsize=(7, 5))
    nodes = nx.draw_networkx_nodes(G1, pos,
                                   nodelist=nodes_list,
                                   node_size=sizes,
                                   node_color=values,
                                   cmap=plt.get_cmap(cmap))
    nx.draw_networkx_edges(G1, pos, alpha=0.6)
    nx.draw_networkx_labels(G1, pos, font_size=9)
    plt.colorbar(nodes, label=title)
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# -------------------------------
# 4. Quick Centrality Prints
# -------------------------------
def quick_centrality_prints(K, deg_cent, close_cent, between_cent, eig_cent, max_nodes=10):
    """
    Print a short table comparing centrality values for first `max_nodes` nodes.
    """
    print('\n--- Quick centrality comparisons (karate) ---')
    print('Node : degree, closeness, betweenness, eigenvector')
    nodes_sorted = sorted(K.nodes())[:max_nodes]
    for n in nodes_sorted:
        d = round(deg_cent.get(n, 0), 3)
        c = round(close_cent.get(n, 0), 3)
        b = round(between_cent.get(n, 0), 3)
        e = round(eig_cent.get(n, 0), 3)
        print(f'{n} : {d}, {c}, {b}, {e}')

# -------------------------------
# 5. Main Function
# -------------------------------
def main():
    # Build graphs
    G, K = build_graphs()

    # Compute clustering + centrality measures
    measures = compute_measures(G, K)

    # Visualize: small graph G colored by local clustering
    draw_graph_with_metric(G, measures['local_clust'], 'Local Clustering (G)')

    # Visualize: karate club colored by betweenness centrality
    draw_graph_with_metric(K, measures['between_cent'], 'Betweenness Centrality (Karate Club)', size_multiplier=3000)

    # Print quick centrality comparisons
    quick_centrality_prints(K,
                            measures['deg_cent'],
                            measures['close_cent'],
                            measures['between_cent'],
                            measures['eig_cent'],
                            max_nodes=10)

    # Student tasks
    print('\n--- Student tasks ---')
    print("- Remove edge ('A','B') from G and observe change in average clustering (modify code and re-run).")
    print("- In karate graph, find top-3 nodes by eigenvector centrality and explain why they are central.")
    print("- Compare degree centrality vs eigenvector centrality: are high-degree always high-eigenvector?")
    print("- Save images of plots (use plt.savefig() inside draw_graph_with_metric if needed).")
    print('\nLab complete. See plotted figures and printed outputs for analysis.')

# -------------------------------
# Run main
# -------------------------------
if __name__ == '__main__':
    main()
