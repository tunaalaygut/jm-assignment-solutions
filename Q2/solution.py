def sumOfSimilarities(s):
    '''
    Function that given a string, calculates the sum of similarities
    with each of its suffixes. It uses a variant of the Z-algorithm
    to lower the runtime complexity of the task.
    
    Args
        s: String to find the similarities within.

    Returns
        c: The sum of similarities of a String with its suffixes.
    '''
    n = len(s)  # Get the size of the string.

    c = n  # Number of characters in a string, by definiton,
           # can be considered as similarities. Therefore, start
           # counting from the size of the string.
    
    L, R = 0, 0  # Initialize the boundaries.
    z = [0] * n  # Initialize (with all 0's) the Z-array which is the
                 # core of the Z-algorithm.

    for i in range(1, n):
        if (i > R):
            L = R = i
            
            while ((R < n) and (s[R-L] == s[R])): R+=1
            z[i] = R-L
            R-=1
            c+=z[i]
        else:
            k = i-L
            if(z[k] < R-i+1):
                z[i] = z[k]
                c +=z[i]
            else:
                L = i
                
                while ((R < n) and (s[R-L] == s[R])): R+=1
                z[i] = R-L
                R-=1
                c+=z[i]
                
    return c  # Return the result.
