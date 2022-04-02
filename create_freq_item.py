#frequent itemsets creation function

def create_freq_item(X, ck, min_support):

    item_count = {}
    for transaction in X:
        for item in ck:
            if item.issubset(transaction):
                if item not in item_count: 
                    item_count[item] = 1
                else: 
                    item_count[item] += 1    
    
    n_row = X.shape[0]
    freq_item = []
    item_support = {}
    
    for item in item_count:
        support = item_count[item] / n_row
        if support >= min_support:
            freq_item.append(item)
        
        item_support[item] = support
        
    return freq_item, item_support
