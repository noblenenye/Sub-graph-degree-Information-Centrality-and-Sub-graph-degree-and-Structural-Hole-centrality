import math
import networkx as nx
import matplotlib.pyplot as plt


# Function that computes subG_entropy centrality
def subG_entropy(g):
    Inf = []
    DI = {}
    TI = {}

    for node in g:
        SDIi = 0
        SDIhold = []
        onehop = list(nx.single_source_shortest_path_length(g, node, 1))
        subGraph = g.subgraph(onehop)

        for nebor in onehop:
            deg = subGraph.degree(nebor)
            SDIi += deg
            SDIhold.append(deg)
            #print('Node{}: SDI for node {} = {}'.format(node, nebor, SDIi))

        minusV = 0
        for ite in SDIhold:
            try:
                minusV += ((ite / SDIi) * math.log10(ite))
            except ZeroDivisionError:
                minusV = 0
        try:
            DI[node] = round((math.log10(SDIi) - minusV), 4)
        except ValueError:
            DI[node] = 0
        Inf.append(DI)

    II = {}
    for nod in g:
        twoHNeb = []
        jideAll = 0
        twohop = nx.single_source_shortest_path_length(g, nod, 2)
        for key, value in twohop.items():
            if value == 2:
                twoHNeb.append(key)

        twohoppath = list(nx.all_simple_paths(g, source=nod, target=twoHNeb, cutoff=2))
        for ii in twoHNeb:
            IF = 0
            ID = 0
            ss = 0
            for path in twohoppath:
                if ii == path[2]:
                    ss += 1
                    IF += DI[path[0]] * DI[path[1]]
            ID += IF/ss
            jideAll += round(ID/len(twoHNeb), 4)
        II[nod] = jideAll
        TI[nod] = round((0.6 * DI[nod]) + (0.4 * II[nod]), 4)
    return TI
##########################################################################

#G = nx.Graph()
#G.add_weighted_edges_from([(1,2,2), (1,4,2), (1,6,2), (2,3,1), (2,4,2),
#                          (2,5,3), (3,5,2), (3,8,1), (4,5,3), (5,6,3),
#                           (5,7,2), (6,7,1), (7,8,1)])


#Tot = subG_entropy(G)
#print(sorted(Tot.items(), key=lambda item: item[1], reverse=True))



#nx.draw(G, with_labels=True)
#pos=nx.spring_layout(G)
#nx.draw_networkx(G,pos)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()