
expenses=(10000,12000,8000,20000,22000,24000)

#display smallest_expese
min_exp=min(expenses)
print(min_exp)

# diplay highest_expense
max_exp=max(expenses)
print(max_exp)
# display total_expense
total_exp=sum(expenses)
print(total_exp)
# sort all expenses order by desc

sorted_expenses=sorted(expenses,reverse=True)

print(sorted_expenses)