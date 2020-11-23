from math import floor, log, ceil
import sys
import argparse

# args = sys.argv
principal = 0
payment = 0
interest = 0
periods = 0
overpayment = 0
zeroarray = [principal, payment, interest, periods]
namearr = []
valuearray = []
types = ["annuity", "diff"]
parser = argparse.ArgumentParser()
res = False

parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
type_n = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment

if principal is not None:
    principal = int(principal)
if periods is not None:
    periods = int(periods)
if interest is not None:
    interest = float(interest)
if payment is not None:
    payment = int(payment)

# write your code here
# print(f"{loan_principal}\n{first_month}\n{second_month}\n{third_month}\n{final_output}")

# calc_type = input('''What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# ''')
for ele in valuearray:
    if int(ele) < 0:
        res = True
        break

if type_n not in types or (type_n == types[1] and payment is not None) or interest is None or res:
    print("Incorrect parameters")
    exit()
elif type_n == types[0]:
    if principal and payment and interest:
        i = interest / (12 * 1) * 0.01
        num = ceil(log(payment / (payment - (i * principal)), i + 1))
        res_year = floor(num / 12)
        res_month = num - res_year * 12
        if res_month == 0:
            res_year = ceil(res_year)
        if res_year > 1:
            res_year = str(res_year) + " years"
        elif res_year == 1:
            res_year = str(res_year) + " year"
        if res_month > 1:
            res_month = str(res_month) + " months"
        elif res_month == 1:
            res = str(res_month) + " month"
        if res_year == 0:
            print(f"it will take {res_month} to repay the loan!")
        elif res_month == 0:
            print(f"it will take {res_year} to repay the loan!")
        else:
            print(f"it will take {res_year} and {res_month} to repay the loan!")
        overpayment = floor(num * payment - principal)
        print(f"Overpayment = {overpayment}")
    elif payment and periods and interest:
        i = interest / (12 * 1) * 0.01
        upper = i * pow((1 + i), periods)
        lower = (pow((1 + i), periods) - 1)
        division = upper / lower
        principal = floor(payment / division)
        overpayment = floor(payment * periods - principal)
        print(f"Your loan principal = {principal}!\nOverpayment = {overpayment}")

    elif principal and periods and interest:
        i = (interest / (12 * 1)) * 0.01
        annuity_bef = principal * ((i * (pow(1 + i, periods))) / ((pow(1 + i, periods)) - 1))
        annuity_payment = ceil(annuity_bef)
        overpayment = (periods * annuity_payment) - principal
        print(f"Your annuity payment = {annuity_payment}!\nOverpayment = {overpayment}")
    else:
        i = interest / (12 * 1) * 0.01
        payment = ceil(principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1)))
        print(f"Your monthly payment = {payment}!")
else:
    i = interest / (12 * 1) * 0.01
    diffcount = 0
    for m in range(1, periods + 1):
        diffmonthly = ceil((principal / periods) + i * (principal - (principal * (m - 1) / periods)))
        print("Month", m, ": payment is ", diffmonthly)
        diffcount += diffmonthly
    overpayment = diffcount - principal
    print(f"Overpayment = {overpayment}")
    # loan_principal = int(input("Enter the loan principal: "))
    # monthly_payment = int(input("Enter the monthly payment: "))
    # loan_interest = float(input("Enter the loan interest: ")) * 0.01

# elif calc_type == "a":
# loan_principal = int(input("Enter the loan principal: "))
# periods = int(input("Enter the number of periods: "))
# loan_interest = float(input("Enter the loan interest: ")) * 0.01

#   elif calc_type == "p":
# annuity_payment = float(input("Enter the annuity payment: "))
# periods (n) = int(input("Enter the number of periods: "))
# loan_interest = float(input("Enter the loan interest: ")) * 0.01


# monthnumber = int(input("Enter the number of months: "))
# res = ceil(loan_principal / monthnumber)
# printedres = str(res)
# if loan_principal % monthnumber != 0:
#    final_month = loan_principal - (monthnumber - 1) * res
#    printedres = printedres + f" and last payment is {final_month}"
# print(f"Your monthly payment = {printedres}")
