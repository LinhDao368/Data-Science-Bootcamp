import math

print("Welcome to the Finance Calculators.\n")

while True:
    try:
        investment_cal = input('''\nWe provide the following calculating services:\n
Investment: \t to calculate the amount of interest you'll earn on your investment.
Bond: \t\t to calculate the amount you'll have to pay on a home loan \n
Please choose the type of calculator you need by typing 'investment' or 'bond': ''').lower()

        if investment_cal not in ['investment', 'bond']:
            raise ValueError("Invalid input. Please enter 'investment' or 'bond'.")

        print(f"\nThank you for choosing the {investment_cal} calculator. Please provide the below information to proceed.")

        if investment_cal == "investment":
            print("Note: Please only type numbers (and decimals where applicable) for deposit amount, interest rate, and year.\n")
            break  # Exit loop if input is valid

        elif investment_cal == "bond":
            print("Note: Please only type numbers (and decimals where applicable).\n")
            break  # Exit loop if input is valid

    except ValueError as error:
        print(error)  # Display error message

while True:
    try:
        if investment_cal == "investment":
            deposit = float(input("Deposit amount (in GBP): "))
            investment_rate = float(input("Interest rate (%): "))
            invest_time = float(input("Years of investing: "))
            interest_type = input("\nPlease specify the type of interest you want by typing 'simple' or 'compound': ").lower()

            if interest_type not in ['simple', 'compound']:
                raise ValueError("Invalid input. Please enter 'simple' or 'compound'.")

            print(f'''\nDeposit amount: \t{deposit} GBP
Interest rate: \t\t{investment_rate}%
Years of investing: \t{invest_time} years''')

            if interest_type == "simple":
                simple_interest = deposit * (1 + (investment_rate / 100) * invest_time)
                print(f"\nWith Simple Interest plan, your interest will be {simple_interest} GBP.")

            elif interest_type == "compound":
                compound_interest = deposit * math.pow((1 + investment_rate / 100), invest_time)
                print(f"\nWith Compound Interest plan, your interest will be {round(compound_interest, 2)} GBP.")

            break  # Exit loop if input is valid

        elif investment_cal == "bond":
            house_value = float(input("Current house value (in GBP): "))
            bond_rate = float(input("Interest rate (%): "))
            bond_time = float(input("Number of months to repay: "))

            print(f'''House value: {house_value} GBP
Interest rate: {bond_rate}%
Repay time: {bond_time} months''')
            monthly_rate = bond_rate / 100 / 12
            repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-bond_time))
            repayment = round(repayment, 2)
            print(f"\nYour bond repayment will be {repayment} GBP per month.")

            break  # Exit loop if input is valid

    except ValueError as error:
        print(error)  # Display error message
