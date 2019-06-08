import os
import csv

budget_data = os.path.join("budget_data.csv")
with open (budget_data, newline = "", encoding = "utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    
    date = []
    revenue_change = []
    total_revenue = 0
    total_revenue_change = 0
    rev_start = 0
    count = 0
    
    for row in csv_reader:
        count = count + 1
        date.append(row[0])
        total_revenue += int(row[1])
        rev_end = int(row[1])
        rev_change = rev_end - rev_start
        total_revenue_change += rev_change
        revenue_change.append(rev_change)
        rev_start = rev_end
        
    avg_rev = total_revenue_change / count
    g_increase = max(revenue_change)
    g_decrease = min(revenue_change)
    increase_date = date[revenue_change.index(g_increase)]
    decrease_date = date[revenue_change.index(g_decrease)]
    
with open("Financial_Analysis_Report.txt", "w") as text:
    text.write("Financial Analysis " + "\n")
    text.write("----------------------------------" + "\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total: " + "$" + str(total_revenue) + "\n")
    text.write("Average Change: " + "$" + str(int(avg_rev)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($ " + str(g_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($ " + str(g_decrease) + ")" )
    
    
    
    
    print("Total Months: " + str(count))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(int(avg_rev)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($ " + str(g_increase) + ")" )
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($ " + str(g_decrease) + ")" )
    

