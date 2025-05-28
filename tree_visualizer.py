import pydot
import uuid

def build_dot_graph(tree, graph=None, parent=None):
    if graph is None:
        graph = pydot.Dot(graph_type='digraph', rankdir='LR')  # Horizontal layout

    node_id = str(uuid.uuid4())
    label = str(tree[0]) if isinstance(tree, (list, tuple)) else str(tree)
    graph.add_node(pydot.Node(node_id, label=label, shape='ellipse', style='filled', fillcolor='lightgreen'))

    if parent:
        graph.add_edge(pydot.Edge(parent, node_id))

    if isinstance(tree, (list, tuple)) and len(tree) > 1:
        for child in tree[1:]:
            build_dot_graph(child, graph, node_id)

    return graph

def save_and_return_image(tree, filename="tree.png"):
    graph = build_dot_graph(tree)
    graph.write_png(filename)
    return filename
