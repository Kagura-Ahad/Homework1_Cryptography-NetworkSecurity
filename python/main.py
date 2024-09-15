import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ['S1', 'S2', 'S3', 'F1', 'F2', 'P1', 'P2', 'D1', 'D2']
G.add_nodes_from(nodes)

# Add edges with labels
edges = [
    ('S1', 'S2', 'control'),
    ('S1', 'S3', 'owner, control'),
    ('S1', 'F1', 'read*'),
    ('S1', 'F2', 'read, owner'),
    ('S1', 'P1', 'wakeup'),
    ('S1', 'P2', 'wakeup'),
    ('S1', 'D1', 'seek'),
    ('S1', 'D2', 'owner'),
    ('S2', 'S1', 'control'),
    ('S2', 'F1', 'write*'),
    ('S2', 'F2', 'execute'),
    ('S2', 'P2', 'owner'),
    ('S2', 'D2', 'seek*'),
    ('S3', 'S1', 'control'),
    ('S3', 'F2', 'write'),
    ('S3', 'P1', 'stop'),
]

for edge in edges:
    G.add_edge(edge[0], edge[1], label=edge[2])

# Draw the graph
plt.figure(figsize=(15, 10))  # Increase figure size

# Use shell layout
# Define the shell structure, placing 'S1' in the center, others in two outer shells
shells = [['S1'], ['S2', 'S3'], ['F1', 'F2', 'P1', 'P2', 'D1', 'D2']]
pos = nx.shell_layout(G, nlist=shells)

# Manually set the position of 'F1'
pos['F1'] = (-0.7, -0.6)
pos['S2'] = (-0.7, 0.2)
pos['D2'] = (-0.35, -0.55)
pos['F2'] = (-0.35, 0.6)
pos['S1'] = (0,0)
pos['D1'] = (0.5, -0.5)
pos['P1'] = (0.6, -0.1)
pos['P2'] = (0.3, 0.1)
pos['S3'] = (0.3, 0.6)



# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)

# Draw edge labels with padding
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', label_pos=0.3)  # label_pos adjusts the position of the label along the edge

plt.show()
