#probability-based pattern mining 

def create_freq_prob(X, c1, min_support):

    item_count = {}
    initial_prob = {}
    c1_update = []
    c2 = []
    prob_1 = 1.0
    prob_threshold = 0.001 #define probability threshold
    
    for transaction in X:
        for item in c1:
            if item.issubset(transaction):
                if item not in item_count: 
                    item_count[item] = 1
                else: 
                    item_count[item] += 1    
    
    for item in item_count: 
        ini_prob = item_count[item]/ X.shape[0]  #calculate probability for unique items
        if ini_prob >= prob_threshold:
            initial_prob[item] = ini_prob  
            c1_update.append(item)  

    for subset in itertools.combinations(c1_update, 2):  #identify combinations of unique items
        c2.append(subset)
    
    n_row = X.shape[0]
    freq_item = []
    item_support = {}

    for items in c2:
        for item in items:
            probability = initial_prob[item]
            prob_1 = prob_1 * probability

            if prob_1 >= prob_threshold:  
                freq_item.append(items)

        support = item_count[item] / n_row

        item_support[item] = support

    return freq_item, item_support
