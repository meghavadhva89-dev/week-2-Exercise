def ways(n):
    """
    Calculate the number of ways to make 'n' cents using any number of
    nickels (5¢) and pennies (1¢).

    Parameters:
        n (int): The total amount of cents to make.

    Returns:
        int: The number of unique combinations of nickels and pennies
             that sum up to 'n' cents.
    """
    count = 0
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        if pennies >= 0:
            count += 1
    return count
print(ways(10))  # Example usage

import numpy as np

def lowest_score(names, scores):
    """
    Returns the name of the student with the lowest score.

    Parameters:
        names (np.array): Array of student names.
        scores (np.array): Array of corresponding scores.

    Returns:
        str: Name of the student with the lowest score.
    """
    lowest_index = np.argmin(scores)  # index of the lowest score
    return names[lowest_index]


def sort_names(names, scores):
    """
    Returns the names sorted by scores in descending order.

    Parameters:
        names (np.array): Array of student names.
        scores (np.array): Array of corresponding scores.

    Returns:
        np.array: Names sorted from highest to lowest score.
    """
    sorted_indices = np.argsort(scores)[::-1]  # indices for sorting descending
    return names[sorted_indices]



names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

print("Lowest scoring student:", lowest_score(names, scores))
print("Students sorted by descending scores:", sort_names(names, scores))