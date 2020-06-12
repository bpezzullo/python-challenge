import csv

with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    profit_loss_month_count = 0
    line_count = 0
    total_profit_loss = 0
    for row in csv_reader:
        if line_count != 0 :
            if profit_loss_month_count == 0:
                greater_dec_proloss = row
                greater_inc_proloss = row
            elif greater_dec_proloss[1] > row[1]:
                    greater_dec_proloss = row
            elif greater_inc_proloss[1] < row[1]:
                    greater_inc_proloss = row
            profit_loss_month_count += 1
            total_profit_loss = total_profit_loss + int(row[1])
        line_count += 1
    average_profit_loss = total_profit_loss / profit_loss_month_count

    print ("Financial Analysis")

    print("Total Profit / Loss: " + str(total_profit_loss))

    print("Average change: $" + str(average_profit_loss))

    print(greater_inc_proloss)

    print(greater_dec_proloss)



            
        
