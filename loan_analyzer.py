# coding: utf-8
import csv
from pathlib import Path
from statistics import mean

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
number_of_loans = len(loan_costs)
print(f"Number of loans: {number_of_loans}")

# What is the total of all loans?
total_of_loans = sum(loan_costs)
print(f"Sum of all loans: ${total_of_loans}")

# What is the average loan amount from the list?
average_of_loans = mean(loan_costs) # sum(loan_costs) / len(loan_costs)
print(f"Average of loans: ${average_of_loans}")


# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Get future value
future_value = loan['future_value'] # loan.get('future_value')
print(f"Future Value ${future_value}")

# Calculate a "fair value" of the loan.
discount_rate = .20
remaining_months = loan['remaining_months']
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"Present value: ${present_value}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_cost = loan['loan_price']
if present_value >= loan_cost:
    print("Loan is worth at least the cost to buy it.")
else:
    print("Loan is too expensive and not worth the price.")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
def loan_evaluation(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + discount_rate/12) ** remaining_months
    return present_value

# Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
new_future_value = new_loan['future_value']
new_remaining_months = new_loan['remaining_months']
new_discount = .2

loan_evaluation(future_value=new_future_value, remaining_months=new_remaining_months, annual_discount_rate=new_discount)
print(f"The present value of the loan is: {present_value}")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
inexpensive_loans = [loan['loan_price'] for loan in loans if loan['loan_price'] <= 500]
print(inexpensive_loans)

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("resources/inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
