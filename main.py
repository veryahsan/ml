monthly_expenses_data = [
  ("JAN", 2000),
  ("FEB", 2300),
  ("MAR", 3300),
  ("APR", 4300),
  ("MAY", 7700),
  ("JUN", 1200),
  ("JUL", 1300),
  ("AUG", 4000),
  ("SEP", 990),
  ("OCT", 2000),
  ("NOV", 1000),
  ("DEC", 2200)
]
def show_monthly_expenses():
  print(monthly_expenses_data)

def show_feb_expenses():
	feb_expense = None
	jan_expense = None

	for month, expense in monthly_expenses_data:
		if month == "JAN":
			jan_expense = expense
		if month == "FEB":
			feb_expense = expense

	if jan_expense is not None and feb_expense is not None:
		print(f"February expense is {feb_expense - jan_expense} dollars more than compared to January\n")

def first_quarter_expense():
	expenses = []
	for month, expense in monthly_expenses_data[0:3]:
		expenses.append(expense)
	print(f"Total quarterly expense is: {sum(expenses)}")
        
def exactly_n_expense(target_amount):
	found_months = []
	for month, amount in monthly_expenses_data:
		if amount == target_amount:
			found_months.append(month)
	return found_months
    

def make_list_comprehension(list):
	return [expense for month, expense in list]

list = make_list_comprehension(monthly_expenses_data)
print(list)

