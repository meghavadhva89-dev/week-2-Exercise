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
    names = np.asarray(names).flatten()
    scores = np.asarray(scores).flatten()
    lowest_index = int(np.argmin(scores))
    return str(names[lowest_index])

def sort_names(names, scores):
    """
    Returns the names sorted by scores in descending order.

    Parameters:
        names (np.array): Array of student names.
        scores (np.array): Array of corresponding scores.

    Returns:
        np.array: Names sorted from highest to lowest score.
    """
    names = np.asarray(names)
    scores = np.asarray(scores)
    sorted_indices = np.argsort(scores)[::-1]
    return names[sorted_indices]