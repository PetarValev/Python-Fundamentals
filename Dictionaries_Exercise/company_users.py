data = input()
companies = {}
while data != "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    data = input()

for company, employees in companies.items():
    print(f"{company}")
    for current_employee in employees:
        print(f"-- {current_employee}")
