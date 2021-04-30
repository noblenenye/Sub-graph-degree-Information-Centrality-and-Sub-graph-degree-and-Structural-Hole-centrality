import networkx as nx
import matplotlib.pyplot as plt



# Function to compute the values degree and structural hole  count of nodes
def DSHC(G):
    SHlist = []
    nodeSH = {}
    for node in G:

        SubSH = 0
        summ = 0
        nebor = G[node]

        for ii in nebor:
            s = 0
            hold = []
            for jj in reversed(list(nebor)):
                path = list(nx.all_simple_paths(G, source=ii, target=jj, cutoff=2))

                for patCon in path:
                    if patCon[1]==node and jj not in G[ii]:
                        s += 1
            deg = G.degree(node)
            degNeb = G.degree(ii)
            #print('This is s:{}'.format(s))
            #print('For node {}: originating from node {} := {}'.format(node, ii, s))
            SubSH = round((((1 / deg) + (1 / degNeb)) * (1 / (1 + s))) ** 2, 4)
            summ += SubSH
            nodeSH[node] = summ
        SHlist.append(nodeSH)

    return nodeSH
##########################################################################

#G=nx.Graph()
#G.add_weighted_edges_from([('A','B',3), ('A','C',2), ('A','D',2),
#                            ('A','E',3),('B','J',2),('D','J',2),
#                            ('J','K',1),('E','F',2),('F','G',2),
#                            ('G','I',1),('I','H',1),('F','H',2)])
#
#G0 = nx.read_weighted_edgelist('facebook_like.txt')
#G = nx.read_adjlist('erdos')
#G = nx.Graph(G0)
#G.remove_edges_from(list(nx.selfloop_edges(G)))
#G.remove_nodes_from(list(nx.isolates(G)))
#G = nx.read_gml('power.gml', label='id')
#G = nx.read_weighted_edgelist('adolescent.txt')
#deg_SHcount = DSHC(G)
#print(sorted(deg_SHcount.items(), key=lambda item: item[1]))


#nx.draw(G, with_labels=True)
#pos=nx.spring_layout(G)
#nx.draw_networkx(G,pos)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()