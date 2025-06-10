

# 3 employees id name department salary location

employees=[
    {"id":100,"name":"hari","department":"hr","salary":24000,"location":"ekm"},
    {"id":101,"name":"vipin","department":"hr","salary":34000,"location":"ekm"},
    {"id":102,"name":"james","department":"ba","salary":54000,"location":"tvm"},
    {"id":103,"name":"jhon","department":"ba","salary":64000,"location":"bnr"},
    {"id":104,"name":"james","department":"qa","salary":27000,"location":"tvm"},
    {"id":105,"name":"das","department":"qa","salary":34000,"location":"tsr"},

]


employees_salary_total=sum([ emp.get("salary") for emp in employees])

print(employees_salary_total)

# max(),min(),sorted()
# sum()

#employee_with_highest_salary

def get_employee_salary(dictionary):

    return dictionary.get("salary")


max_salary=max(employees,key=get_employee_salary)

print(max_salary)

min_salary=min(employees,key=get_employee_salary)
print(min_salary)


sorted_employees=sorted(employees,reverse=True,key=get_employee_salary)

print(sorted_employees)

# # total number of employees

# employee_count=len(employees)
# print(employee_count)

# all_employee_names=[emp.get("name") for emp in employees]

# print(all_employee_names)

# all_employee_salary=[emp.get("salary") for emp in employees]

# print(all_employee_salary)

# # display hr employee names


# hr_employees=[emp.get("name") for emp in employees if emp.get("department")== "hr"]

# print(hr_employees)


# # display employees whose salary > 30000


# salary_filter=[emp.get("name") for emp in employees if emp.get("salary") > 30000]
# print("sal > 30k",salary_filter)
# # max,min,sum,sorted

