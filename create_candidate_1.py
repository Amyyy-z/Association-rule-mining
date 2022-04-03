def create_candidate_1(X):

    c1 = []  #assign an empty string
    for transaction in X:
        for t in transaction:
            t = frozenset([t]) #identify unique items and set it to frozenset
            if t not in c1:
                c1.append(t)
    return c1
