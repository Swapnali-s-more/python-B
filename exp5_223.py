import networkx as nx
import matplotlib.pyplot as plt

# 1. Create a directed graph (DiGraph)
# Directed graphs are ideal for semantic networks where relationships have a specific direction
G = nx.DiGraph()

# 2. Define Objects/Concepts (Nodes)
G.add_nodes_from([
    "Dog", "Cat", "Animal", "Mammal",
    "CanFly", "HasFur", "Meows", "Barks"
])

# 3. Define Interrelationships (Edges)

# 'is-a' relationships
G.add_edge("Dog", "Mammal", label="is-a")
G.add_edge("Cat", "Mammal", label="is-a")
G.add_edge("Mammal", "Animal", label="is-a")

# 'can' / 'has' relationships
G.add_edge("Dog", "Barks", label="can")
G.add_edge("Dog", "HasFur", label="has")
G.add_edge("Cat", "Meows", label="can")
G.add_edge("Cat", "HasFur", label="has")
G.add_edge("Animal", "CanFly", label="cannot")

# 4. Analyze the Network (Inference)
is_dog_an_animal = nx.has_path(G, "Dog", "Animal")
print(f"Is a Dog an Animal? {is_dog_an_animal}")

# 5. Visualize the Network
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 7))

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)

# Edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Simple Semantic Network for Knowledge Representation")
plt.axis('off')
plt.show()