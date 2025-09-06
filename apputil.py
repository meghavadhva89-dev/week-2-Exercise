def ways(n):
    """
    Returns the number of ways to make n cents using pennies (1c) and nickels (5c).
    """
    count = 0
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        if pennies >= 0:
            count += 1
    return count
print(ways(21)) 
# Output: 5





  

import numpy as np

def lowest_score(names, scores):
    # Find the index of the lowest score
    lowest_index = np.argmin(scores)
    # Return the name corresponding to that index
    return names[lowest_index]

# Example usage
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
print(lowest_score(names, scores))