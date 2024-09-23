import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm

# Function to load data from a JSON file
def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Function to draw the topology graph
def draw_topology(topology_path):
    topology = load_data(topology_path)

    # Create a directed graph from a dictionary
    G = nx.DiGraph()

    # Add nodes and edges
    for key, values in topology.items():
        for value in values:
            G.add_edge(key, value)

    # Set the figure size
    plt.figure(figsize=(15, 15))
    # Create a layout for our nodes 
    pos = nx.kamada_kawai_layout(G)
    # Adjust node sizes based on their degree
    degrees = [G.degree(n) * 100 for n in G.nodes()]
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=degrees, node_color=range(len(G)), cmap=cm.plasma, font_size=8, font_weight='bold', arrowstyle='->', arrowsize=15)
    # Set the title
    plt.title("API Dependency Graph")

    # Save the graph to a file
    save_path = topology_path.replace('.json', '.pdf')
    plt.savefig(save_path)
    plt.close()  # Close the plot to free up memory

# Specify the paths to your data
service_path = 'data/topology/service_maps.json'
endpoint_path = 'data/topology/endpoint_maps.json'

# Draw the topology graphs
draw_topology(service_path)
draw_topology(endpoint_path)
