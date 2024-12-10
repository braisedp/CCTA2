import igraph as ig

def auction(graph,src,bids,skills,request):
    division = network_division(graph,src)
    x,market_x = winner_selection(bids,skills,request,division)
    p = payment_determination(bids,skills,request,division,market_x)
    return x,p

def network_division(graph:ig.Graph,src):
    res = {}
    distances = graph.shortest_paths_dijkstra([src])[0]
    maxdis = 1
    for i,dis in enumerate(distances):
        if dis==float('inf'):
            continue
        maxdis = max(dis,maxdis)
        if dis !=0:
            if dis not in res:
                res[dis] =[i]
            else:
                res[dis].append(i)
    ans = []
    for i in range(1,maxdis+1):
        if i in res:
            ans.append(res[i])
        else:
            ans.append([])
    return ans

def winner_selection(bids, skills, request, division):
    x = []
    market_winners = []
    S = set()
    R = request
    for market in division:
        A = market.copy()
        market_x = []
        while A and R.difference(S):
            selected = None
            maxval = 0
            for worker in A:
                val = len(R.intersection(skills[worker].difference(S))) / bids[worker]
                if val > maxval:
                    selected = worker
                    maxval = val
            if selected is not None:
                market_x.append(selected)
                A.remove(selected)
                S = S.union(skills[selected].intersection(R))
            else:
                break
        x.extend(market_x)
        market_winners.append(market_x)
    return x,market_winners


def winner_selection_CRA(bids,skills,request,division):
    x = []
    market_winners = []
    S = set()
    R = request
    for market in division:
        A = market.copy()
        market_x = []
        while A and R.difference(S):
            selected = None
            maxval = 0
            for worker in A:
                val = len(R.intersection(skills[worker].difference(S))) - bids[worker]
                if val > maxval:
                    selected = worker
                    maxval = val
            if selected is not None:
                market_x.append(selected)
                A.remove(selected)
                S = S.union(skills[selected].intersection(R))
            else:
                break
        x.extend(market_x)
        market_winners.append(market_x)
    return x,market_winners


def payment_determination(bids,skills,request,division,market_x):
    p=[0]*len(bids)
    S = set()
    for i,partial_x in enumerate(market_x):
        for worker in partial_x:
            S_ = S.copy()
            market = division[i].copy()
            market.remove(worker)
            R = request
            while market and R.difference(S_):
                selected = None
                maxval = 0
                for worker_ in market:
                    val = len(R.intersection(skills[worker_].difference(S_))) / bids[worker_]
                    if val > maxval:
                        selected = worker_
                        maxval = val
                if selected is None:
                    p[worker] = 1
                    break
                else:
                    p[worker] = max(len(R.intersection(skills[worker].difference(S_))) / maxval,p[worker])
                    S_ = S_.union(skills[selected].intersection(R))
                    market.remove(selected)
        for worker in partial_x:
            S = S.union(skills[worker].intersection(request))
    return p


def payment_determination_CRA(bids,skills,request,division,market_x):
    p=[0]*len(bids)
    S = set()
    for i,partial_x in enumerate(market_x):
        for worker in partial_x:
            S_ = S.copy()
            market = division[i].copy()
            market.remove(worker)
            R = request
            while market and R.difference(S_):
                selected = None
                maxval = 0
                for worker_ in market:
                    val = len(R.intersection(skills[worker_].difference(S_))) - bids[worker_]
                    if val > maxval:
                        selected = worker_
                        maxval = val
                if selected is None:
                    p[worker] = 1
                    break
                else:
                    p[worker] = max(len(R.intersection(skills[worker].difference(S_)))- maxval,p[worker])
                    S_ = S_.union(skills[selected].intersection(R))
                    market.remove(selected)
        for worker in partial_x:
            S = S.union(skills[worker].intersection(request))
    return p