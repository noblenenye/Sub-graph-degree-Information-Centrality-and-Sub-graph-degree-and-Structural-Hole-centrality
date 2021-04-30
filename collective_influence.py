import networkx as nx
import matplotlib.pyplot as plt




# Function to compute the Collective Influence values of nodes
def Collective_Influence(G):
    CIlist = []
    nodeCI = {}

    for node in G:
        deg1stSum = 0
        deg2ndSum = 0
        allNebSUM = 0
        degNodeminus1 = 0

        twohop = nx.single_source_shortest_path_length(G, node, 2)

        for key, value in twohop.items():
            if value == 0:
                continue
            elif value == 1:
                deg1stSum += (G.degree(key) - 1)
            else:
                value == 2
                deg2ndSum += (G.degree(key) - 1)

        degNodeminus1 = (G.degree(node) - 1)
        allNebSUM = deg1stSum + deg2ndSum
        nodeCI[node] = degNodeminus1 * allNebSUM
        CIlist.append(nodeCI)

    return nodeCI

#G = nx.karate_club_graph()
#G0 = nx.read_weighted_edgelist('facebook_like.txt')
#G = nx.Graph(G0)
#G.remove_edges_from(list(nx.selfloop_edges(G)))
#G.remove_nodes_from(list(nx.isolates(G)))
#print(nx.info(G))
#G = nx.read_gml('power.gml', label='id')
#G = nx.read_edgelist('erdos')
#G=nx.Graph()
#G.add_weighted_edges_from([('A','B',3), ('A','C',2), ('A','D',2),
#                            ('A','E',3),('B','J',2),('D','J',2),
#                            ('J','K',1),('E','F',2),('F','G',2),
#                            ('G','I',1),('I','H',1),('F','H',2)])
#CI = Collective_Influence(G)
#print(sorted(CI.items(), key=lambda item: item[1], reverse = True))
#G.remove_node(33)


#nx.draw(G, with_labels=True)
#pos=nx.spring_layout(G)
#nx.draw_networkx(G,pos)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()