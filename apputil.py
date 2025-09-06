def ways(n):
    """
    Returns the number of ways to make n cents using pennies (1c) and nickels (5c).
    """
    count = 0
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        if pennies >= 0:
            count += 1