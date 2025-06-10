




















employees={
    "ram":34000,
    "ravi":25000,
    "vipin":18000,
    "vijay":28000,
    "ahana":45000
}

def get_value_by_key(key):

    return employees.get(key)


max_salary=max(employees,key=get_value_by_key)

print(max_salary,employees.get(max_salary))

min_salary=min(employees,key=get_value_by_key)

print(min_salary,employees.get(min_salary))


sorted_employees=sorted(employees,key=get_value_by_key)
print(sorted_employees)


total=sum([sal for sal in employees.values()])

print(total)