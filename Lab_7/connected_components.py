import graph_EL as graph
import dsf

def connected_components(g):
    vertices = g.vertices
    components = vertices
    s = dsf.DSF(vertices)
    for edge in g.el:
        components -= s.union(edge.source,edge.dest)
    return components