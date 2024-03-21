import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def create_graph(matrix):
    norm_matrix = matrix / np.max(matrix)
    return nx.from_numpy_array(norm_matrix)

def centrality_katz(graph):
    katz = nx.katz_centrality(graph, normalized=True, weight="weight")
    katz_np = np.array(list(katz.values()))
    return katz_np

def centrality_degree(graph):
    degr_np = np.array(list(graph.degree(weight='weight')))[:, 1]
    degr_np /= np.max(degr_np)
    return degr_np

def recommend_meeting(katz, degr):
    influencial = np.argmax(katz)
    isolated = np.argmin(degr)
    return influencial, isolated

def visualize_graph(graph, katz, degr):
    edges = [(u, v) for (u, v, d) in graph.edges(data=True)]

    pos = nx.spring_layout(graph, seed=7)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(graph, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(graph, pos, edgelist=edges, width=6, alpha=0.5)

    # node labels
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family="sans-serif")

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
