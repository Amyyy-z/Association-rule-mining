#Apriori function define

def apriori(X, min_support, use_colnames=False):
    
    time_start = time.time()     #identify the initial starting time

    c1 = create_candidate_1(X)     #create a list of unique items from the transaction table
    freq_item, item_support_dict = create_freq_item(X, c1, min_support = 0.2)     #create a list of items with support value larger than 0.2
    freq_items = [freq_item]
    
    #initialization
    k = 0
    while len(freq_items[k]) > 0: 
      
        freq_item = freq_items[k]
        ck = create_candidate_k(freq_item, k)     #create a list of candidate itemsets       
        freq_item, item_support = create_freq_item(X, ck, min_support = 0.2)     #create a list of frequent itemsets with support larger than 0.2
        freq_items.append(freq_item)  #append frequent itemsets to initial frequent items
        item_support_dict.update(item_support)  #update the support dictionary with support value
        k += 1
        
    print(len(item_support_dict))
    
    time_end = time.time()     #identify the stop time
    print('end time: ', time_end - time_start, 's')     #running time record
        
    return freq_items, item_support_dict
