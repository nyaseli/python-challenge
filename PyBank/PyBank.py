data = []
with open('budget_data.csv') as file:
    for line in file.readlines():
        li = line.split(',')
        try:
            data.append([li[0], int(li[1].rstrip())])
        except ValueError:
            pass


print('Financial Analysis')
print('-'*25)

months = len(data)
print(f'Total months: {months}')

dollars = [n[1] for n in data]
total = sum(dollars)
print(f'Total: ${total}')

profits = [dollars[i + 1] - dollars[i] for i in range(len(dollars) - 1)]
average_profit = round(sum(profits)/len(profits), 2)
print(f'Average change: ${average_profit}')

max_profit = max(profits)
max_profit_date = data[profits.index(max_profit)+1][0]
print(f'Greatest Increase in profits: {max_profit_date} (${max_profit})')

min_profit = min(profits)
min_profit_date = data[profits.index(min_profit)+1][0]
print(f'Greatest Decrease in profits: {min_profit_date} (${min_profit})')
