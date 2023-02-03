def rolling_average(arr,window_size):
    i = 0
    # Initialize an empty list to store moving averages
    moving_averages = []

    # Loop through the array t o
    #consider every window of size 3
    while i < len(arr): #- window_size + 1:

        # Calculate the average of current window
        if (i < len(arr)- window_size + 1):
            window_average = np.sum(arr[i:i+window_size])/window_size
            moving_averages.append(window_average)
            
        if (i >= len(arr)- window_size + 1):
            window_average = np.sum(arr[i:len(arr)]/(len(arr)-i))
            moving_averages.append(window_average)
                                  
        i += 1                              
    
    return moving_averages
