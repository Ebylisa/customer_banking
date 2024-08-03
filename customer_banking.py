# Import the create_cd_account and create_savings_account functions
from cd_account import create

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('Enter your savings balancef: '))
    savings_interest = float(input('Enter your savings account interest rate: '))
    savings_months = int(input('How many months have you had the savings account: '))
   

    # Call the create_savings_account function and pass the variables from the user.
    new_savings_balance = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('Your new savings account balance is $', format(new_savings_balance(), ',.2f'))
                                                                              
    print('The interest earned on the savings account after {savings_months} months is ${interest_earned():.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('Enter your cd balance: '))
    cd_interest = float(input('Enter your cd account interest rate: '))
    cd_months = int(input('How many months have you had the cd account: '))

    # Call the create_cd_account function and pass the variables from the user.
    new_cd_account_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'The interest earned on your CD after {cd_months} months is ${interest_earned:.2f}')
    print(f'Your new CD balance after interest earned is $', format(new_cd_account_balance',.2f'))
        
        
if __name__ == "__main__":
    # Call the main function.
    main() 