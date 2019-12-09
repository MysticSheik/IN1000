from rack import Rack
from node import Node

class Cluster:
    def __init__(self, file_name):
        self.nodes_per_rack = 0
        self.racks = []
        
        # =============================================
        # Til deg som retter:
        # =============================================
        # Spar deg selv og hopp over denne kreften her!
        # c':
        # ---------------------------------------------
        cluster_file = open(file_name)
        for line in cluster_file:
            if not line.startswith("#") and line.strip():
                line = line.split()
                if len(line) == 1:
                    self.nodes_per_rack = int(line[0])
                    self.racks.append(Rack(self.nodes_per_rack))
                    self.rack_index = 0
                if len(line) == 3:
                    for i in range(int(line[0])):
                        self.add_node(Node(int(line[1]), int(line[2])))
        cluster_file.close()
        # ================================================

    # Adds a node to the cluster
    def add_node(self, node):
        # Add a new rack if other racks are full
        if not self.racks[self.rack_index].has_capacity():
            self.racks.append(Rack(self.nodes_per_rack))
            self.rack_index += 1

        self.racks[self.rack_index].add_node(node)

    # Returns the total number of processors in the cluster
    def num_processors(self):
        processor_count = 0
        for rack in self.racks:
            processor_count += rack.num_processors()
        return processor_count

    # Returns the number of nodes with memory equal to or greather than target memory
    def num_nodes_with_memory(self, target_memory):
        num_nodes = 0
        for rack in self.racks:
            num_nodes += rack.num_nodes_with_memory(target_memory)
        return num_nodes

    # Return the number of racks in the cluster
    def num_racks(self):
        return len(self.racks)
