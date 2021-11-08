# This is an implementation of an undirected weighted graph

class Edge:
    def __init__(self, destination_vertex_id, weight = 0):
        """ Both destination_vertex_id and weight are of type int """
        self.destination_vertex_id = destination_vertex_id
        self.weight = weight


class Vertex:
    index = 0
    def __init__(self, state_name, edge_list = None):
        """ id is an unique id for Vertex. It is incremented as new vertex gets created
            name is the actual data,
            edge_list contains all the all edges which the vertex is connected to
        """
        Vertex.index += 1
        self.id = Vertex.index
        self.name = state_name
        self.edge_list = edge_list or []

    def print_edges(self):
        str_edges = ''
        for edge in self.edge_list:
            str_edges += f'{edge.destination_vertex_id} '

        return str_edges


class Graph:
    def __init__(self):
        """ vertices list holds all the vertices of the entire Graph"""
        self.vertices = []

    def display(self):
        for vertex in self.vertices:
            print(f'{vertex.name} ({vertex.id}) -> [{vertex.print_edges()}]')

    def add_vertex(self, new_vertex):
        self.vertices.append(new_vertex)
        print(f'vertex added succesfully')


def main():
    g = Graph()

    v1 = Vertex('TN')
    v2 = Vertex('KA')
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.display()

if __name__ == "__main__":
    main()

