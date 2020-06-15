import csv
import sys

with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')

    # initialize the variables to 0 or empty for the lists
    profit_loss_month_count = 0
    # dec = 0
    # inc = 0
    total_profit_loss = 0
    average_profit_loss = 0
    PFDate = []
    Profloss = []

    # Strip off the header
    header = next(csv_reader)

    for row in csv_reader:
        # store the date into the list Date
        PFDate.append(row[0])

        # store the Profit loss in the list Profloss
        Profloss.append(int(row[1]))

        # second way of calculating the results.  Use programming logice to calculate the 
        # min and max, plus count the entries and total the profits. I commented it out, but 
        # left it to show 2 different ways to calculate the results.  It would depend on the 
        # processing time to calculate between the two on which one is better.

        # if profit_loss_month_count == 0:
        #     # for the first row set the dec and inc variables to compare against
        #     greater_dec_proloss = row
        #     dec = int(row[1])
        #     greater_inc_proloss = row
        #     inc = int(row[1])
        # for the other rows check to see if the profit is greater than the last max value
        # elif dec > int(row[1]):
        #     greater_dec_proloss = row
        #     dec = int(row[1])
        # if not greater check to see if it is the least or the biggest decrease
        # elif inc < int(row[1]):
        #     greater_inc_proloss = row
        #     inc = int(row[1])
        
        # count the number of rows
        # profit_loss_month_count += 1

        # sum the total profit_loss
        # total_profit_loss = total_profit_loss + int(row[1])

# Calculate the average
# average_profit_loss = total_profit_loss / profit_loss_month_count

# second method of calcaulating is using the functions to return the min, max, sum and len
# not sure which method runs faster.

# get the sum of the Profit and loss
total_profit_loss = sum(Profloss)
# get the number of rows in the spreadsheet outside of the header
profit_loss_month_count = len(Profloss)
# calculate the average
average_profit_loss = total_profit_loss/profit_loss_month_count
# find the min and max of the Profloss list
greater_inc_proloss = max(Profloss) 
greater_dec_proloss = min(Profloss)
# once having the values get the month associated to each of the greatest increase or decrease
inc_month = PFDate[Profloss.index(greater_inc_proloss)]
dec_month = PFDate[Profloss.index(greater_dec_proloss)]

# write the information to the file 'results'in the folder 'a'nalysis'
f = open("analysis/results","w",newline='\n')
f.write("Financial Analysis \n")
f.write("-------------------------------\n")
f.write("Total Months: " + str(profit_loss_month_count) + "\n")
f.write("Total Profit / Loss: $" + str(total_profit_loss) + "\n")
f.write("Average change: $" + str(round(average_profit_loss,2)) + "\n")

f.write("Greatest Increast in Profits: " + inc_month + " ($" + str(greater_inc_proloss) + ")\n")
f.write("Greatest Decrease in Profits: " + dec_month + " ($" + str(greater_dec_proloss) + ")\n")

# close the file and then use the file to display the results to the sreen
f.close

# Print the file
f = open("analysis/results","r")
file_contents = f.read()
print (file_contents)
    
f.close
