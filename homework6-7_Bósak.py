import json

with open('departments.json', 'r') as f:
    data = json.load(f)

def update_salaries(departments):
    for department in departments:
        expenses = department['expenses']
        income = department['income']
        if expenses < income:
            for employee in department['employees']:
                employee['salary'] = round(employee['salary'] * 1.1, 2)

update_salaries(data['departments'])

with open('new_costs.json', 'w') as new_file:
    json.dump(data, new_file, indent=2)