def knapSack(prices, weights, M): 
    n = len (weights)
    # table of size carry_weight x # of items to hold results of subproblems
    B = [[0 for _ in range(M+1)] for _ in range(n+1)] 
    # hold the items chosen while backtracing after the algorithm has filled in the subproblem table
    items = []
    
    for i in range(n+1): 
        for w in range(M+1): 
            if i==0 or w==0: 
                B[i][w] = 0
            elif weights[i-1] <= w: 
                # if the item will fit, pick it if it maximizes value
                B[i][w] = max(prices[i-1] + B[i-1][w-weights[i-1]],  B[i-1][w]) 
            else: 
                B[i][w] = B[i-1][w] 
    
    val_trace = B[n][M] 
    weight_trace = M  
      
    # trace back through the array getting the indices for the items chosen
    for i in range(n, 0, -1): 
        if val_trace <= 0: 
            break # we're done

        # this item is already accounted for
        if val_trace == B[i - 1][weight_trace]: 
            continue
        else: 
            # don't reuse any items
            if(i - 1) not in items:
                items.append(i - 1)
                #reduce the tracer's price and weight
                val_trace = val_trace - prices[i - 1] 
                weight_trace = weight_trace - weights[i - 1] 
    
    return (B[n][M], items)