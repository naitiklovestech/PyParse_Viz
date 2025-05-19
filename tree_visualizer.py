import networkx as nx
import matplotlib.pyplot as plt

def create_tree_graph(tree, G=None, pos=None, x=0, y=0, level=0):
    if G is None:
        G = nx.DiGraph()
    if pos is None:
        pos = {}

    if isinstance(tree, tuple):
        node_label = tree[0]
        G.add_node(node_label, pos=(x, y))
        pos[node_label] = (x, y)

        for i, child in enumerate(tree[1:]):
            child_label = f"{node_label}_{i}"
            G.add_node(child_label, pos=(x + i, y - 1))
            pos[child_label] = (x + i, y - 1)
            G.add_edge(node_label, child_label)
            create_tree_graph(child, G, pos, x + i, y - 1, level + 1)
    else:
        G.add_node(tree, pos=(x, y))
        pos[tree] = (x, y)

    return G, pos

def visualize_ast(ast):
    if ast is None:
        print("No AST to visualize.")
        return

    G, pos = create_tree_graph(ast)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    plt.title("Abstract Syntax Tree (AST)")
    plt.show()

def visualize_parse_tree(tree):
    if tree is None:
        print("No parse tree to visualize.")
        return

    G, pos = create_tree_graph(tree)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold')
    plt.title("Parse Tree")
    plt.show() 