class Node:
    def __init__(self, memory_size, num_processors):
        self.memory_size = memory_size
        self.num_processors = num_processors

    def get_num_processors(self):
        return self.num_processors

    def get_memory_size(self):
        return self.memory_size
