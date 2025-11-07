# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_total = sum(week[0] for week in monthly_expenses)
transport_total = sum(week[1] for week in monthly_expenses)
utilities_total = sum(week[2] for week in monthly_expenses)
week_totals = [sum(week) for week in monthly_expenses]
month_total = sum(week_totals)

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', month_total)
