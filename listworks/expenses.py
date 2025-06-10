
expenses=[12000,13000,14000,21000]
#           0    1     2      3    

# display march month expense
march_month_expense=expenses[2]

# update april month expense as 23000
expenses[3]=23000


# dispaly smallest_expense

smmales_expense=min(expenses)

# display higest_expense

highest_expense=max(expenses)

# display total expense
total_exp=sum(expenses)
# dispaly avg_expense
avg_expense=total_exp/len(expenses)

# display second_largest expense


sorted_expenses=sorted(expenses,reverse=True)

print(sorted_expenses[1])