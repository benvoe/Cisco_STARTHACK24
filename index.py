from recommenderSystem import *
from webexAPI import *

# Load weighted social network from CSV
m = np.genfromtxt("graphGenerator/adjacencyMatrix.csv", delimiter=",")

# Generate a undirected graph with weighted edges
graph = create_graph(m)

# Calculate the katz centrality for the graph nodes
katz = centrality_katz(graph)

# Calculate the degree centrality for the graph nodes
degr = centrality_degree(graph)

# Evalutate the most influencial and most isolated persons
infl, isol = recommend_meeting(katz, degr)

# Create a visualization of the weighted social network
visualize_graph(graph, katz, degr)

send_meeting_suggestion(infl, isol)