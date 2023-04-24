#CTI-110
#P4HW2- Salar Calculator
#Faith Rivera
#04/24/2023
#


# Define constants for overtime calculation
MAX_REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

# Initialize variables to store totals
num_employees = 0
total_regular_pay = 0.0
total_overtime_pay = 0.0
total_gross_pay = 0.0

# Loop to calculate pay for multiple employees
while True:
    # Get employee name or exit loop if user enters "Done"
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    # Get employee's hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate regular pay and overtime pay
    if hours_worked > MAX_REGULAR_HOURS:
        overtime_hours = hours_worked - MAX_REGULAR_HOURS
        regular_hours = MAX_REGULAR_HOURS
    else:
        overtime_hours = 0.0
        regular_hours = hours_worked
    overtime_pay = overtime_hours * pay_rate * OVERTIME_MULTIPLIER
    regular_pay = regular_hours * pay_rate

    # Calculate gross pay and update totals
    gross_pay = overtime_pay + regular_pay
    num_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    # Display employee's pay information
    print(f"\nEmployee name:  {employee_name}\n")
    print(f"Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print(f"---------------------------------------------------------------------------------------------------------------------")
    print(f"{hours_worked}\t\t{pay_rate}\t\t{overtime_hours}\t\t{overtime_pay:.2f}\t\t{regular_pay:.2f}\t\t{gross_pay:.2f}\n")

# Display total pay information for all employees
print(f"\nTotal number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: {total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: {total_regular_pay:.2f}")
print(f"Total amount paid in gross: {total_gross_pay:.2f}")
