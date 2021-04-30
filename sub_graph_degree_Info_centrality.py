import math
import networkx as nx
import matplotlib.pyplot as plt
from entropy_weighting_method import entropy_weigth


# Function that computes sub_graph Degree Information Centrality
def subgraph_deg_InfoCentrality(g):
    if nx.is_weighted(g) == False:
        alpha1 = 1; alpha2 = 0
    else:
        alpha1, alpha2 = entropy_weigth(g)

    Inf = []
    nodInf = {}
    for node in g:
        subG = []
        N = 0
        count = 0
        SDIsum = 0
        SDIi = 0
        SDIhold = []

        minusV = 0
        onehop = list(nx.single_source_shortest_path_length(g, node, 1))
        N = len(onehop)
        for myList in onehop:
            deg = g.degree(myList)
            wett = g.degree(myList, weight='weight')
            # print('number of nodes in node i subG= ', N)
            # print('contents of subG are: ', subG)
            # print('degree of node i =', deg)
            # print('strength of node i =', wett)
            SDIi = (((deg ** alpha1) * (wett ** alpha2)) / N)
            SDIhold.append(SDIi)
            SDIsum = SDIsum + SDIi
            #print('Node{}: SD for node {} = {}'.format(node, myList, SDIi))

        for ite in SDIhold:
            try:
                minusV += ((ite / SDIsum) * math.log10(ite))
            except ZeroDivisionError:
                #minusV = 0
                continue
        try:
            nodInf[node] = round((math.log10(SDIsum) - minusV), 4)
        except ValueError:
            #nodInf[node] = 0
            continue
        Inf.append(nodInf)
    return nodInf
##########################################################################

#G = nx.read_adjlist('fiften_node_network.txt')
#G = nx.karate_club_graph()
#G=nx.Graph()
#G.add_weighted_edges_from([('A','B',3), ('A','C',2), ('A','D',2),
#                            ('A','E',3),('B','J',2),('D','J',2),
#                            ('J','K',1),('E','F',2),('F','G',2),
#                            ('G','I',1),('I','H',1),('F','H',2)])
#alpha1, alpha2 = entropy_weigth(G)
#subG_Info = subgraph_deg_InfoCentrality(G)
#print(sorted(subG_Info.items(), key=lambda item: item[1], reverse = True))


#nx.draw(G, with_labels=True)
#pos=nx.spring_layout(G)
#nx.draw_networkx(G,pos)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()