def create_candidate_k(freq_item, k):

    ck = []
    
    # for generating candidate of size two (2-itemset)
    if k == 0:
        for f1, f2 in combinations(freq_item, 2):
            item = f1 | f2 # combinations of two sets
            ck.append(item)
    else:    
        for f1, f2 in combinations(freq_item, 2):       
            intersection = f1 & f2
            if len(intersection) == k:
                item = f1 | f2
                if item not in ck:
                    ck.append(item)
    return ck
