import math
import networkx as nx


# Function to calculate the values of alpha1 and alpha2
def entropy_weigth(g):
    sum1 = 0
    sum2 = 0

    sumR1 = 0
    sumR2 = 0

    for node in g:
        deg = g.degree(node)
        wett = g.degree(node, weight='weight')
        #print('Node {} Deg:{}, weight: {}'.format(node, deg, wett))
        #print('')

        sum1 += (deg) ** 2
        sum2 += (wett) ** 2

    sqsm1 = math.sqrt(sum1)
    sqsm2 = math.sqrt(sum2)
    #print('sum {}:; sqrt sum {}:'.format(sum1, sqsm1))
    #print('sum wett {}:; sqrt wett sum {}:'.format(sum2, sqsm2))

    for node in g:
        deg2 = g.degree(node)
        wett2 = g.degree(node, weight='weight')

        M1 = (deg2 / sqsm1)
        #
        M2 = (wett2 / sqsm2)
        #print('for node{}, M1 and M2: {} and and {}'.format(node, M1, M2))

        # sumR1+=(M1 * math.log10(M1))
        # sumR2+=(M2 * math.log10(M2))
        try:
            sumR1 += (M1 * math.log10(M1))
            sumR2 += (M2 * math.log10(M2))
        except ValueError:
            sumR1 += 0
            sumR2 += 0
    #print(sumR1, sumR2)
    #print(len(g))
    #H1 = -((1 / math.log10(len(g))) * sumR1)
    #H2 = -((1 / math.log10(len(g))) * sumR2)
    try:
        H1 = -((1 / math.log10(len(g))) * sumR1)
        H2 = -((1 / math.log10(len(g))) * sumR2)
    except ValueError:
        H1 = 0
        H2 = 0
    #print('H1: {}; H2: {}'.format(H1, H2))
    #print(H1 + H2)
    alpha1 = round((1 - H1) / (2 - (H1 + H2)), 4)
    alpha2 = round((1 - H2) / (2 - (H1 + H2)), 4)

    return alpha1, alpha2
#############################################################

#G=nx.Graph()
#G.add_weighted_edges_from([('A','B',3), ('A','C',2), ('A','D',2),
#                            ('A','E',3),('B','J',2),('D','J',2),
#                            ('J','K',1),('E','F',2),('F','G',2),
#                            ('G','I',1),('I','H',1),('F','H',2)])
#

#G = nx.Graph()
#G.add_weighted_edges_from([(1,2,2), (1,4,2), (1,6,2), (2,3,1), (2,4,2),
#                          (2,5,3), (3,5,2), (3,8,1), (4,5,3), (5,6,3),
#                           (5,7,2), (6,7,1), (7,8,1)])


#alpha1, alpha2 = entropy_weigth(G)
#print('The value of alpha1 = {} and alpha2 = {}'.format(alpha1, alpha2))
