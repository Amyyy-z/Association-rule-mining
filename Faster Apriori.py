#Faster Apriori function define

def fastapriori(X, min_support, use_colnames=False):
    
    time_start = time.time()
        
    c1 = create_candidate_unique(X) #generate unique itemset named as c1
    
    X_2 = [] #assign an empty dataframe to update transcation database
    
    freq_item, item_support_dict = create_freq_prob(X, c1, min_support = 0.2) #identify frequent items and their pairs by calculating the probability
    
    freq_items = [freq_item]
    
    for j in freq_items[0]:
        a = []
        for item in j:
            for items in item:
                a.append(items) #append unique items to an empty string
    
    for items in X: 
        if a < items: #if the item or its paris are in the original X, then append to the new dataframe
            if items not in X_2:

                X_2.append(items)
           
    X_2 = np.array(X_2)

    
    c11 = create_candidate_1(X_2)
    
    freq_item, item_support_dict = create_freq_item(X_2, c11, min_support = 0.2)
    
    freq_items = [freq_item]
    
    
    k = 0
    while len(freq_items[k]) > 0:
        
        freq_item = freq_items[k]
        ck = create_candidate_k(freq_item, k)       
        freq_item, item_support = create_freq_item(X_2, ck, min_support = 0.2)
        freq_items.append(freq_item)
        item_support_dict.update(item_support)
        
        if freq_items in X:
            if X not in X_2:
                X_2.append(X) 
        
        X = X_2  #update transcation table with probability score
        X = np.array(X) 
        
        k += 1
              
           
    time_end = time.time()
    
    print('end time: ', time_end - time_start, 's')
        
    return freq_items, item_support_dict
