import random
import igraph as ig
import pandas as pd

def create_graph(nodes, edges):
    g = ig.Graph(directed=True)
    g.add_vertices(nodes)

    edgeset = set()

    while len(edgeset) < edges:
        source = random.randint(0, nodes - 1)
        target = random.randint(0, nodes - 1)
        if source != target:
            edgeset.add((source, target))

    g.add_edges(list(edgeset))
    return g

def create_example_A():
    g = ig.Graph(directed=True)
    g.add_vertices(5)
    g.add_edges([(4, 0), (4, 1), (0, 2), (0, 3)])
    return g

def add_edges(graph, src, nodes):
    graph.add_vertex(src)
    edgeset = set()
    for i in nodes:
        if src != i:
            edgeset.add((src, i))
    graph.add_edges(list(edgeset))

def read_graph_from_csv(file_path):
    df = pd.read_csv(file_path)
    
    # 提取边列表
    edges = list(zip(df['from'], df['to']))
    
    # 创建有向图
    g = ig.Graph(directed=True)
    g.add_vertices(max(df['from'].max(), df['to'].max()) + 1)
    g.add_edges(edges)
    
    return g
