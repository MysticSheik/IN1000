from cluster import Cluster
from node import Node

def main():
    abel = Cluster("abel.cluster")

    print("Noder med minst 32 GB:", str(abel.num_nodes_with_memory(32)))
    print("Noder med minst 64 GB:", str(abel.num_nodes_with_memory(64)))
    print("Noder med minst 128 GB:", str(abel.num_nodes_with_memory(128)))
    print()
    print("Processors:", abel.num_processors())
    print("Racks:", abel.num_racks())

main()
