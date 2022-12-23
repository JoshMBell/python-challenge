import csv 

csv_budget_path = "D:\\Bootcamp\\Assignments\\Challenges\\Module_3\\python-challenge\\PyBank\\Resources\\budget_data.csv"

months_count = 0
total_profit = 0
date = []
profit_loss = []
profit_change = []
average_change = 0
previous_change = 0

with open(csv_budget_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        months_count += 1
        total_profit = total_profit + int(row[1])
        profit_change.append(int(row[1]) - int(previous_change))
        date.append(str(row[0]))
        profit_loss.append(int(row[1]))
        previous_change = row[1]

    average_change = sum(profit_change[1:])/len(profit_change[1:])
    max_value = max(profit_change)
    min_value = min(profit_change)
    increase_index = profit_change.index(max_value)
    decrease_index = profit_change.index(min_value)
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months_count}")
    print(f"Total: {sum(profit_loss)}")
    print(f"Average Change: ${format(average_change, '.2f')}")
    print(f"Greatest Increase in Profits: {date[increase_index]} ({profit_change[increase_index]})")
    print(f"Greatest Decrease in Profits: {date[decrease_index]} ({profit_change[decrease_index]})")

with open('analysis//results.txt', 'w') as csv_results:
    csv_writer = csv.writer(csv_results, delimiter = ',')
    csv_results.write("Financial Analysis\n")
    csv_results.write("----------------------------\n")
    csv_results.write(f"Total Months: {months_count}\n")
    csv_results.write(f"Total: {sum(profit_loss)}\n")
    csv_results.write(f"Average Change: ${format(average_change, '.2f')}\n")
    csv_results.write(f"Greatest Increase in Profits: {date[increase_index]} ({profit_change[increase_index]})\n")
    csv_results.write(f"Greatest Decrease in Profits: {date[decrease_index]} ({profit_change[decrease_index]})")
