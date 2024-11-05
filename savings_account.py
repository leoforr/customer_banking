"""Import the Account class from the Account.py file."""
from Account import Account  

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class with the initial balance and interest rate (starting with 0 interest)
    account = Account(balance, 0)

    # Calculate total interest earned over the given months
    total_interest_earned = 0
    for _ in range(months):
        monthly_interest = balance * (interest_rate / 100 / 12)  # Assuming interest compounds monthly
        balance += monthly_interest
        total_interest_earned += monthly_interest

    # Pass the updated balance to the set_balance method
    account.set_balance(balance)

    # Pass the total interest earned to the set_interest method
    account.set_interest(total_interest_earned)

    # Return the updated balance and total interest earned
    return balance, total_interest_earned

