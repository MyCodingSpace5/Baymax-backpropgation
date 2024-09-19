def baymax_backpropagation(fx, weights, threshold):
    n = len(weights)
    output = 0.0 
    for i in range(n):
        weight = weights[i]
        if fx > threshold:  
            break
        output += (fx * weight) / (i + 1)  
        
    return output



