from node import Node

class Rack:
    def __init__(self, max_nodes):
        self.max_nodes = max_nodes
        self.nodes = []

    # Adds a node as long as there is capacity in the rack
    def add_node(self, node):
        if self.has_capacity():
            self.nodes.append(node)
        else:
            print("Couldn't add a node in the rack because the rack is full :(")

    # Checks if the rack has capacity for more nodes
    def has_capacity(self):
        return len(self.nodes) < self.max_nodes

    # Returns the total number of processors of all nodes in the rack
    def num_processors(self):
        processor_count = 0
        for node in self.nodes:
            processor_count += node.get_num_processors()
        return processor_count

    # Returns the total number of nodes with memory equal to or greather than target memory.
    def num_nodes_with_memory(self, target_memory):
        num_nodes = 0
        for node in self.nodes:
            if (node.get_memory_size() >= target_memory):
                num_nodes += 1
        return num_nodes
