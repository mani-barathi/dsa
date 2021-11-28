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
            str_edges += f'{edge.destination_vertex_id}({edge.weight}) '
        return str_edges


class Graph:
    def __init__(self):
        """ vertices list holds all the vertices of the entire Graph"""
        self.vertices = []

    def display(self):
        for vertex in self.vertices:
            print(f'{vertex.name} ({vertex.id}) -> [{vertex.print_edges()}]')

    def get_vertex(self, v_id):
        for vertex in self.vertices:
            if vertex.id == v_id:
                return vertex
        return None

    def check_vertex_exists(self, v_id):
        for vertex in self.vertices:
            if vertex.id == v_id:
                return True
        return False

    def check_edge_exists(self, start_v_id, end_v_id):
        start_v = self.get_vertex(start_v_id)
        for edge in start_v.edge_list:
            if edge.destination_vertex_id == end_v_id:
                return True
        return False

    def add_vertex(self, new_vertex):
        self.vertices.append(new_vertex)
        print(f'vertex({new_vertex.id}, {new_vertex.name}) added succesfully')

    def add_edge(self, start_v_id, end_v_id, weight):
        is_start_v_exists = self.check_vertex_exists(start_v_id)
        is_end_v_exists = self.check_vertex_exists(end_v_id)

        if not is_start_v_exists or not is_end_v_exists:
            return print(f'Invalid vertex id!')

        if self.check_edge_exists(start_v_id, end_v_id):
            return print(f'edge already exists between {self.get_vertex(start_v_id).name} & {self.get_vertex(end_v_id).name}')

        for vertex in self.vertices:
            if vertex.id == start_v_id:
                edge = Edge(end_v_id, weight)
                vertex.edge_list.append(edge)
            elif vertex.id == end_v_id:
                edge = Edge(start_v_id, weight)
                vertex.edge_list.append(edge)

        print(f'Edge added between {self.get_vertex(start_v_id).name} & {self.get_vertex(end_v_id).name}')


def main():
    g = Graph()

    v1 = Vertex('TN')
    v2 = Vertex('KA')
    v3 = Vertex('MH')
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.display()
    g.add_edge(1,2,70)
    g.add_edge(1,3,50)
    g.add_edge(1,3,50)
    g.display()

if __name__ == "__main__":
    main()

