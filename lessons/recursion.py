"""Challenge Question 07."""
__author__ = "730469865"


def f(n: int, k: int) -> int:
    """Uses the previous term (n-1) to calculate the current term(n)."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return (f(n - 1, k)) + k