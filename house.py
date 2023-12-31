annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25
current_savings = 0.0
monthly_salary = annual_salary / 12
percentage_of_monthly = monthly_salary * portion_saved
months = 0
while current_savings < portion_down_payment:
    current_savings += percentage_of_monthly
    investment_return = current_savings*0.04 / 12
    current_savings += investment_return
    months += 1
print("Number of months:", months)
