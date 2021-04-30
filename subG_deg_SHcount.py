import networkx as nx
import matplotlib.pyplot as plt
from entropy_weighting_method import entropy_weigth


# Function to compute the SubGraph Degree and structural hole values of nodes
def subG_deg_SH(G):
    if nx.is_weighted(G) == False:
        alpha1 = 1; alpha2 = 0
    else:
        alpha1, alpha2 = entropy_weigth(G)

    SHlist = []
    nodeSH = {}
    for node in G:

        SubSH = 0
        summ = 0
        N = 0

        nebor = G[node]
        for ii in nebor:
            hold = []
            s = 0
            onehop = list(nx.single_source_shortest_path_length(G, node, 1))
            N = len(onehop)
            for jj in reversed(list(nebor)):
                path = list(nx.all_simple_paths(G, source=ii, target=jj, cutoff=2))

                for patCon in path:
                    if patCon[1] == node and jj not in G[ii]:
                        s += 1
            #print('For node {}: originating from node {} := {}'.format(node, ii, s))
            deg = G.degree(node)
            wett = G.degree(node, weight='weight')
            degNeb = G.degree(ii)
            wettNeb = G.degree(ii, weight='weight')
            SubSH = round((((((deg ** alpha1) * (wett ** alpha2)) / N) + (
                        (degNeb ** alpha1) * (wettNeb ** alpha2)) / N) * (1 + s)), 4)
            #print('For node{}: SD{} = {}'.format(node, ii, SubSH))
            summ += SubSH
            nodeSH[node] = summ
        SHlist.append(nodeSH)

    return nodeSH


##########################################################################
#G = nx.karate_club_graph()
#G=nx.Graph()
#G.add_weighted_edges_from([('A','B',3), ('A','C',2), ('A','D',2),
#                            ('A','E',3),('B','J',2),('D','J',2),
#                            ('J','K',1),('E','F',2),('F','G',2),
#                            ('G','I',1),('I','H',1),('F','H',2)])

#alpha1, alpha2 = entropy_weigth(G)
#subG_deg = subG_deg_SH(G)
#print(sorted(subG_deg.items(), key=lambda item: item[1]))


#nx.draw(G, with_labels=True)
#pos=nx.spring_layout(G)
#nx.draw_networkx(G,pos)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()