import csv
import sys

with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    profit_loss_month_count = 0
    line_count = 0
    total_profit_loss = 0
    for row in csv_reader:
        if line_count != 0 :
            cur_row = int(row[1])
            
            if profit_loss_month_count == 0:
                greater_dec_proloss = row
                dec = cur_row
                greater_inc_proloss = row
                inc = cur_row
            #else:
            elif dec > cur_row:
                print(str(row[1]) + str(dec))
                greater_dec_proloss = row
                dec = cur_row
            elif inc < cur_row:
                print(str(row[1]))
                greater_inc_proloss = row
                inc = cur_row
                print("inc" + str(greater_inc_proloss))
            print("the number is " + str(cur_row) + " inc " + str(inc) + " dec " + str(dec))
            profit_loss_month_count += 1
            print(str(profit_loss_month_count))
            total_profit_loss = total_profit_loss + int(row[1])
        line_count += 1
    average_profit_loss = total_profit_loss / profit_loss_month_count
    print(line_count)
    print(profit_loss_month_count)
    print("Financial Analysis")


    print("Total Profit / Loss: $" + str(total_profit_loss))

    print("Average change: $" + str(average_profit_loss))

    print(greater_inc_proloss)

    print(greater_dec_proloss)

    f = open("analysis/results","w")
    f.write("Financial Analysis \n")
    
    f.write("Total Profit / Loss: $" + str(total_profit_loss) + "\n")

    f.write("Average change: $" + str(average_profit_loss) + "\n")

    #f.write(greater_inc_proloss)

    #f.write(greater_dec_proloss)
     
    f.close

    f = open("analysis/results","r")
    file_contents = f.read()
    print (file_contents)
    
    f.close



            
        
