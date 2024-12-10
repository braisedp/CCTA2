import random
from utils.graph import create_example_A, create_graph,add_edges, read_graph_from_csv
from NetworkedAuction import network_division, payment_determination, winner_selection
from Auction import winner_selection_wo_network, payment_determination_wo_network
import igraph as ig



k = 100
g = read_graph_from_csv("graphs/dash.csv")
n = g.vcount()

bids = [random.uniform(0.5,1) for i in range(n)]
skills = [set(random.sample(range(20),random.randint(1,10))) for i in range(n)]
request = set(random.sample(range(20),random.randint(10,20)))

# nodes = random.sample(range(n),k)
# add_edges(g,n,nodes)
# division = network_division(g,n)
# x,market_x = winner_selection(bids,skills,request,division)
# p = payment_determination(bids,skills,request,division,market_x)
x = winner_selection_wo_network(bids,skills,request)
p = payment_determination_wo_network(bids,skills,request,x)
print(x)
S = set()
dict = {}
for i in x:
    S=S.union(skills[i])
    dict[i]=[bids[i],p[i]]
print(request)

print(S)
print(dict)


