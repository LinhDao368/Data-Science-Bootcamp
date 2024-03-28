# FINANCE CALCULATORS
# This program ask for user input of the kind of interest they want to calculate and further neccesary details
# and output the results of the interest, either for investment or homeloan

import math

print ("Welcome to the Finance Calculators.\n")

# Function for float input
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Ask for input of which calculator is needed and lowercase input 
while True:
    investment_cal = input('''\nWe provide the following calculating services:\n
    Investment: \t to calculate the amount of interest you'll earn on your investment.
    Bond: \t\t to calculate the amount you'll have to pay on a home loan \n
    Please choose the type of calculator you need by typing 'investment' or 'bond': ''')

    investment_cal = investment_cal.lower()

    # Ask for further details for investment calculator
    if investment_cal == "investment":
        print("\nThank you for choosing the investment calculator. Please provide the below information to proceed.")
        print("Note: Please only type numbers (and decimals where applicable) for deposit amount, interest rate and year.\n")

        deposit = input_float("Deposit amount (in GBP): ")
        investment_rate = input_float("Interest rate (%): ")
        invest_time = input_float("Years of investing: ")
        interest_type = input("\nPlease specify the type of interest you want by typing 'simple' or 'compound': ")
        # Lower case input
        interest_type = interest_type.lower()

    # Display user's input and output the interest amount
        print(f'''\nDeposit amount: \t{deposit} GBP
    Interest rate: \t\t{investment_rate}%
    Years of investing: \t{invest_time} years''')

        if interest_type == "simple":
            simple_interest = deposit * (1 + investment_rate/100) * invest_time
            print(f"\n With Simple Interest plan, your interest will be {simple_interest} GBP.")
        
        elif interest_type == "compound":
            compound_interest = deposit * math.pow((1 + investment_rate/100), invest_time)
            print(f"\n With Coumpound Interest plan, your interest will be {round(compound_interest,2)} GBP.")

        else:
            print("\nYour input is invalid. Please try again.")
        break

    # Ask for further details for bond calculator
    elif investment_cal == "bond":
        print("\nThank you for choosing the bond calculator. Please provide the below information to proceed.")
        print("Note: Please only type numbers (and decimals where applicable).\n")

        house_value = input_float("Current house value (in GBP): ")
        bond_rate = input_float("Interest rate (%): ")
        bond_time = input_float("Number of months to repay: ")

    # Display user's input and output the interest amount
        print(f'''House value: {house_value} GBP
    Interest rate: {bond_rate}%
    Repay time: {bond_time} months''')
        monthly_rate = bond_rate / 100 / 12
        repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate)**(-bond_time))
        repayment = round(repayment,2)
        print(f"\nYour bond repayment will be {repayment} GBP per month.")
        break