def winner_selection_wo_network(bids, skills, request):
    x = []
    S = set()
    R = request
    A = list(range(len(bids)))
    while A and R.difference(S):
        selected = None
        maxval = 0
        for worker in A:
            val = len(R.intersection(skills[worker].difference(S))) / bids[worker]
            if val > maxval:
                selected = worker
                maxval = val
        if selected is not None:
            x.append(selected)
            A.remove(selected)
            S = S.union(skills[selected].intersection(R))
        else:
            break
    return x


def payment_determination_wo_network(bids,skills,request,x):
    p=[0]*len(bids)
    for worker in x:
        S = set()
        R = request
        A = list(range(len(bids)))
        A.remove(worker)
        while A and R.difference(S):
            selected = None
            maxval = 0
            for worker_ in A:
                val = len(R.intersection(skills[worker_].difference(S))) / bids[worker_]
                if val > maxval:
                    selected = worker_
                    maxval = val
            if selected is None:
                p[worker] = 1
                break
            else:
                p[worker] = max(len(R.intersection(skills[worker].difference(S))) / maxval,p[worker])
                S = S.union(skills[selected].intersection(R))
                A.remove(selected)
    return p