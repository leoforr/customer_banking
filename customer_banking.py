# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account
    savings_balance = float(input("Enter the starting balance for the Savings Account: "))
    savings_interest = float(input("Enter the interest rate for the Savings Account (APR %): "))
    savings_maturity = int(input("Enter the number of months for the Savings Account: "))

    # Call the create_savings_account function with user-provided values
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print the interest earned and updated balance for the Savings Account
    print(f"\nSavings Account - Interest Earned: ${savings_interest_earned:,.2f}")
    print(f"Savings Account - Updated Balance after {savings_maturity} months: ${updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account
    cd_balance = float(input("\nEnter the starting balance for the CD Account: "))
    cd_interest = float(input("Enter the interest rate for the CD Account (APR %): "))
    cd_maturity = int(input("Enter the number of months for the CD Account: "))

    # Call the create_cd_account function with user-provided values
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print the interest earned and updated balance for the CD Account
    print(f"\nCD Account - Interest Earned: ${cd_interest_earned:,.2f}")
    print(f"CD Account - Updated Balance after {cd_maturity} months: ${updated_cd_balance:,.2f}")

# Run the main function
if __name__ == "__main__":
    main()
