# Finance calculators
This project aims at creating a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator based on their input:
- **Investment**: to calculate the amount of interest user will earn on their investment 
- **Bond**: to calculate the amount user will have to pay on a home loan
---
### Investment calculator
This calculator asks for user's input and calculate the results:
- The amount of money they are depositing ('P')
- The interest rate (as a percentage) ('r')
- The number of years they plan on investing ('t')
- The type of interest: 'simple' (A=P(1 + rxt)) or 'compound' (A=P(1 + r)^t^)

### Bond calculator
This calculator asks for user's input and calculate the results:
- The present value of the house ('P')
- The interest rate ('i')
- The number of months they plan to take to repay the bond (n')
- Formula: repayment = (i*P)/(1-(1+i)**(-n))
